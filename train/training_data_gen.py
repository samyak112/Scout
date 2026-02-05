import itertools
import random
import math
import hashlib
import json

from training_topics import Topics

final_arr = []


# added variations so that i have some control during the data generation that if am creating X array of an information type then there is difference in the information which is being created

final_arr = []

def generate_variation_id(domain_idx, type_idx, params_tuple):
    unique_str = f"{domain_idx}|{type_idx}|{str(params_tuple)}"
    return hashlib.md5(unique_str.encode('utf-8')).hexdigest()


# OUTER LAYER LOOP (Domains)
for d_idx, topic in enumerate(Topics['curriculum']):
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

        # 3. Calculate Limit
        max_combinations = math.prod(len(v) for v in variation_parameters.values())
        if max_combinations > 400:
            max_combinations = 400
        
        # 4. Random Sample
        sample_size = min(len(all_combinations), max_combinations)
        selected_tuples = random.sample(all_combinations, sample_size)
        
        # 5. Assign IDs to Variations
        variations_with_ids = []
        for v_tuple in selected_tuples:
            v_id = generate_variation_id(d_idx, t_idx, v_tuple)
            variations_with_ids.append({
                "id": v_id,
                "params": list(v_tuple) # Convert tuple to list for JSON compatibility
            })

        # 6. Append to Final Array with INDEXES
        final_arr.append({
            "ids": {
                "global_index": len(final_arr), # 0, 1, 2, 3...
                "domain_index": d_idx,          # 0, 1, 2...
                "type_index": t_idx             # 0, 1, 2...
            },
            "meta": {
                "domain_name": domain,
                "type_name": type_desc
            },
            "patterns": patterns,
            "variations": variations_with_ids
        })

# Save to JSON
output_filename = 'training_curriculum.json'
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(final_arr, f, indent=2)