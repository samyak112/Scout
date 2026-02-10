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

DATASET_PATH = "train/dataset.jsonl"
PROGRESS_PATH = "train/progress.json"


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
    """
    Takes the specific JSON structure and returns a 7x7 numpy matrix of relevance scores (floats).
    """
    
    # 1. Unpack Sentences
    asym = data['asymmetric']       # Indices 0, 1, 2 (Thread 1)
    sym = data['symmetric']         # Indices 3, 4    (Thread 2)
    neg = data['hard_negatives']    # Indices 5, 6    (Hard Negatives)
    
    # Combine into canonical list
    # [T1_0, T1_1, T1_2, T2_0, T2_1, N1, N2]
    canonical_sentences = asym + sym + neg
    n = len(canonical_sentences)  # Should be 7
    
    # 2. Initialize Matrix (Default to 0.0)
    matrix = np.zeros((n, n), dtype=float)
    
    # 3. Extract Scores
    scores: Scores = data['scores']
    
    # --- POPULATE THREAD 1 INTERNAL (Indices 0, 1, 2) ---
    matrix[0, 1] = scores.thread1_internal.zero_to_one
    matrix[1, 2] = scores.thread1_internal.one_to_two
    matrix[1, 0] = scores.thread1_internal.one_to_zero
    matrix[2, 1] = scores.thread1_internal.two_to_one
    matrix[0, 2] = scores.thread1_internal.zero_to_two
    matrix[2, 0] = scores.thread1_internal.two_to_zero
    
    # --- POPULATE THREAD 2 INTERNAL (Indices 3, 4) ---
    matrix[3, 4] = scores.thread2_internal.zero_to_one
    matrix[4, 3] = scores.thread2_internal.one_to_zero
    
    # --- POPULATE CROSS-THREAD (Thread 1 ↔ Thread 2) ---
    # Broadcast average to all pairs in each direction
    # Thread 1 → Thread 2 (rows 0-2, cols 3-4): 6 pairs
    matrix[0:3, 3:5] = scores.cross_thread_avg.thread1_to_thread2
    
    # Thread 2 → Thread 1 (rows 3-4, cols 0-2): 6 pairs
    matrix[3:5, 0:3] = scores.cross_thread_avg.thread2_to_thread1
    
    # --- HARD NEGATIVES (Indices 5, 6) ---
    # All connections to/from hard negatives remain 0.0 (already initialized)
    
    return matrix.tolist()
    

def generate_dataset():

    with open(PROGRESS_PATH, "r") as f:
        progress = json.load(f)

    with open("train/training_curriculum.json", "r") as f:
        curriculum = json.load(f)

    with open("train/dataset.jsonl", "r") as f:
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
                    asym = parsed.asymmetric
                    sym = parsed.symmetric
                    hard_neg = parsed.hard_negatives

                    sentences = asym + sym + hard_neg

                    matrix = generate_matrix(
                        {
                            "asymmetric": asym,
                            "symmetric": sym,
                            "hard_negatives": hard_neg,
                            "scores": parsed.scores,
                        }
                    )
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