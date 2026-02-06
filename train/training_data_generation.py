import itertools
import random
import hashlib
import json
from prompts import PROMPTS
from google import genai
from training_topics import TOPICS
from response_type import SentenceChain
import os

client = genai.Client(api_key=os.environ.get("API_KEY"))



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


def generate_dataset():

    progress = None
    with open("train/progress.json", "r") as f:
            progress = json.load(f)

    curriculum = None
    with open("train/training_curriculum.json", "r") as f:
            curriculum = json.load(f)

    local_progress = progress.copy()

    for i in range(progress['index'], len(curriculum)):
         content = curriculum[i]

         domain_name = content['meta']['domain_name']
         information_type_description = content['meta']['type_name']
         assymmetric_info = content['patterns'][0]
         symmetric_info = content['patterns'][1]
         hard_neagative_data = content['patterns'][2]

         # variation_index is scoped to progress["index"] only; reset for all subsequent items just for crash safety
         start_j = progress["variation_index"] if i == progress["index"] else 0

         for j in range (start_j,len(content['variations'])):
              variation = content['variations'][j]
              prompt = PROMPTS['generate_dataset'].format(
                   domain = domain_name,
                   information_type = information_type_description,
                   parameters = variation,
                   asymmetric_data = assymmetric_info,
                   symmetric_data = symmetric_info,
                   hard_negative_data = hard_neagative_data
              )

              response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_json_schema": SentenceChain.model_json_schema(),
                },
            )
              recipe = SentenceChain.model_validate_json(response.text)
              print(recipe)
              break
         break 

generate_dataset()