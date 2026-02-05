import itertools
import random

from training_topics import Topics

final_arr = []


# added variations so that i have some control during the data generation that if am creating X array of an information type then there is difference in the information which is being created

for topic in Topics['curriculum']:
    domain = topic['domain']
    for information_type in topic['information_types']:
        variation_parametrs = {}
        patterns = [information_type['asymmetric_pattern'],information_type['symmetric_pattern'],information_type['hard_negative_strategy']]
        batch = information_type['batch_count']
        for key,value in information_type['variation_parameters'].items():
            variation_parametrs[key] = value['values']

        all_combinations = list(itertools.product(
            *variation_parametrs.values()
        ))
        import math

        max_combinations = math.prod(
            len(v) for v in variation_parametrs.values()
        )
        if(max_combinations>400):
            max_combinations = 400

        variations = random.sample(all_combinations, max_combinations)
        final_arr.append({
            'domain':domain,
            "information_type":information_type['type_description'],
            "variations":variations,
            "patterns":patterns,
        })