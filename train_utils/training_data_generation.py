import itertools
import random
import hashlib
import json
from prompts import PROMPTS
from google import genai
from training_topics import TOPICS
from response_type import SentenceChain,Scores
import os
from tqdm import tqdm
from copy import deepcopy
import numpy as np
import time

client = genai.Client(
    vertexai=True, project=os.environ.get("project_id"), location='us-central1'
)

DATASET_PATH = "train_utils/dataset.jsonl"
PROGRESS_PATH = "train_utils/progress.json"


def generate_variation_id(domain_idx, type_idx, params_tuple):
    unique_str = f"{domain_idx}|{type_idx}|{str(params_tuple)}"
    return hashlib.md5(unique_str.encode('utf-8')).hexdigest()

# added variations so that i have some control during the data generation that if am creating X array of an information type then there is difference in the information which is being created

def generate_curriculum(data):
    
    final_arr = []
    # OUTER LAYER LOOP (Domains)
    for d_idx, topic in enumerate(data['curriculum']):
        domain = topic['domain']
        
        # INNER LAYER LOOP (Information Types)
        for t_idx, information_type in enumerate(topic['information_types']):
            
            type_desc = information_type['type_description']
            patterns = [
                information_type['asymmetric_pattern'],
                information_type['symmetric_pattern'],
                information_type['hard_negative_strategy']
            ]
            
            # 1. Gather Parameters
            variation_parameters = {}
            for key, value in information_type['variation_parameters'].items():
                variation_parameters[key] = value['values']

            # 2. Cartesian Product
            all_combinations = list(itertools.product(
                *variation_parameters.values()
            ))
            
            # 4. Random Sample
            sample_size = min(len(all_combinations), information_type['combination_space'])
            selected_tuples = random.sample(all_combinations, sample_size)
            
            # 5. Assign IDs to Variations
            variations = []
            for v_tuple in selected_tuples:
                variations.append(list(v_tuple))

            # 6. Append to Final Array with INDEXES
            final_arr.append({
                "ids": {
                    "global_index": len(final_arr), 
                    "domain_index": d_idx,          
                    "type_index": t_idx             
                },
                "meta": {
                    "domain_name": domain,
                    "type_name": type_desc
                },
                "patterns": patterns,
                "variations": variations
            })

    output_filename = 'training_curriculum.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(final_arr, f, indent=2)

def generate_matrix(data):
    sentences_dict = data['sentences']
    scores = data['scores']

    # Build canonical list and track index ranges per thread
    # chains: thread1, thread2 | pairs: thread3, thread4 | negatives last
    segments = []  # (thread_name, type)

    for key in ['thread1', 'thread2']:
        if key in sentences_dict:
            segments.append((key, 'chain'))

    for key in ['thread3', 'thread4']:
        if key in sentences_dict:
            segments.append((key, 'pair'))

    canonical = []
    thread_ranges = {}  # thread_name → (start, end)

    for thread_name, thread_type in segments:
        start = len(canonical)
        canonical.extend(sentences_dict[thread_name])
        thread_ranges[thread_name] = (start, len(canonical))

    canonical.extend(sentences_dict.get('hard_negatives', []))

    n = len(canonical)
    matrix = np.zeros((n, n), dtype=float)

    # Populate internal scores
    for thread_name, thread_type in segments:
        s, e = thread_ranges[thread_name]
        internal = getattr(scores, f"{thread_name}_internal", None)
        if internal is None:
            continue

        if thread_type == 'chain':
            matrix[s,   s+1] = internal.zero_to_one
            matrix[s+1, s+2] = internal.one_to_two
            matrix[s+1, s]   = internal.one_to_zero
            matrix[s+2, s+1] = internal.two_to_one
            matrix[s,   s+2] = internal.zero_to_two
            matrix[s+2, s]   = internal.two_to_zero

        elif thread_type == 'pair':
            matrix[s,   s+1] = internal.zero_to_one
            matrix[s+1, s]   = internal.one_to_zero

    # Populate cross-thread scores
    cross = scores.cross_thread_avg
    thread_names = [t[0] for t in segments]

    for i, t1 in enumerate(thread_names):
        for t2 in thread_names[i+1:]:
            fwd_val = getattr(cross, f"{t1}_to_{t2}", 0.0) or 0.0
            bwd_val = getattr(cross, f"{t2}_to_{t1}", 0.0) or 0.0

            s1, e1 = thread_ranges[t1]
            s2, e2 = thread_ranges[t2]

            matrix[s1:e1, s2:e2] = fwd_val
            matrix[s2:e2, s1:e1] = bwd_val

    # Hard negatives stay 0.0 — already initialized
    return matrix.tolist()
    

def generate_dataset():

    with open(PROGRESS_PATH, "r") as f:
        progress = json.load(f)

    with open("train_utils/training_curriculum.json", "r") as f:
        curriculum = json.load(f)

    with open(DATASET_PATH, "r") as f:
        total_data_set = [json.loads(line) for line in f]

    local_progress = deepcopy(progress)

    total_steps = sum(
        len(c["variations"]) for c in curriculum[progress["index"]:]
    )


    pbar = tqdm(total=total_steps, desc="Generating dataset")

    for i in range(progress["index"], len(curriculum)):
        content = curriculum[i]

        domain_name = content["meta"]["domain_name"]
        information_type_description = content["meta"]["type_name"]

        asymmetric_info = content["patterns"][0]
        symmetric_info = content["patterns"][1]
        hard_negative_data = content["patterns"][2]

        start_j = progress["variation_index"] if i == progress["index"] else 0

        for j in range(start_j, len(content["variations"])):

            variation = content["variations"][j]

            prompt = PROMPTS["generate_dataset"].format(
                domain=domain_name,
                information_type=information_type_description,
                parameters=variation,
                asymmetric_data=asymmetric_info,
                symmetric_data=symmetric_info,
                hard_negative_data=hard_negative_data,
            )

            BASE_DELAY = 6        # seconds
            MAX_DELAY = 60        # cap
            MAX_RETRIES = 10      # safety valve

            retry = 0


            while True:
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=prompt,
                        config={
                            "response_mime_type": "application/json",
                            "response_json_schema": SentenceChain.model_json_schema(),
                        },
                    )

                    parsed = SentenceChain.model_validate_json(response.text)
                    sentences_dict = parsed.sentences

                    # Flatten in canonical order
                    sentences = []
                    for key in ['thread1', 'thread2', 'thread3', 'thread4']:
                        if key in sentences_dict:
                            sentences.extend(sentences_dict[key])
                    sentences.extend(sentences_dict.get('hard_negatives', []))

                    matrix = generate_matrix({
                        "sentences": sentences_dict,
                        "scores": parsed.scores,
                    })
                    break  # success

                except Exception as e:
                    retry += 1
                    if retry > MAX_RETRIES:
                        raise

                    # exponential backoff with jitter - https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff
                    delay = min(MAX_DELAY, BASE_DELAY * (2 ** (retry - 1)))
                    jitter = random.uniform(0, delay * 0.3)
                    sleep_time = delay + jitter

                    print(
                        f"[retry={retry}] {e} → sleeping {sleep_time:.1f}s"
                    )

                    time.sleep(sleep_time)

            

            final_set = {
                "len_sentences":len(sentences),
                "sentences": sentences,
                "target": matrix,
                "domain_name":domain_name,
                "information_type_description":information_type_description,
                "outer_index": i,
                "inner_index": j,
            }

            # 1. append sample immediately (streaming)
            with open(DATASET_PATH, "a") as f:
                f.write(json.dumps(final_set) + "\n")

            # 2. update progress AFTER successful write
            local_progress["index"] = i
            local_progress["variation_index"] = j + 1

            with open(PROGRESS_PATH, "w") as f:
                json.dump(local_progress, f, indent=2)

            pbar.update(1)

        # reset variation index when moving to next curriculum item
        local_progress["variation_index"] = 0

    pbar.close()
    

generate_dataset()
# generate_curriculum(data=TOPICS)