PROMPTS = {
    "generate_curriculum":"""
You are designing a complete training curriculum for a model that learns directional information gain between sentences.

BACKGROUND:
The model learns to answer: "Does sentence B add functional value after reading sentence A?"
This is directional and NOT about similarity:
- "My faucet leaks" → "Tighten the valve nut" = HIGH (solution adds value to problem)
- "Tighten the valve nut" → "My faucet leaks" = LOW (problem doesn't add value to solution)

But sometimes it's symmetric:
- "Python handles data well" ↔ "Python has rich ML libraries" = BOTH HIGH (mutual explanation)

TRAINING DATA STRUCTURE:
Each batch contains 7 sentences:
- 3 sentences: ASYMMETRIC pattern (A→B→C where direction matters)
- 2 sentences: SYMMETRIC pair (X↔Y where both add value to each other)
- 2 sentences: HARD NEGATIVES (same domain, zero functional value)

ASYMMETRY TYPES (Based on Linguistic Principles):
Your curriculum must cover these 5 fundamental asymmetric patterns:

1. TEMPORAL (Iconicity Principle)
   Language mirrors the physical flow of time. Clause order reflects event order.
   - Structure: earlier_event → later_event → consequence
   - Example: "He opened the door" → "He walked inside" → "He closed it behind him"
   - Why asymmetric: Reversing breaks the temporal reality of what happened
   - Real-world: Sequential actions, procedural steps, chronological events

2. CAUSAL (Explanation & Result)
   One idea is the condition for understanding the other. Cause must precede effect.
   - Structure: cause/need → mechanism/explanation → effect/action
   - Example: "The server crashed" → "Memory usage hit 100%" → "Restart with more RAM"
   - Why asymmetric: Effect cannot be understood without establishing cause first
   - Real-world: Problem-solution, diagnosis, scientific explanations

3. EPISTEMIC (Given → New Information)
   Communication flows from shared knowledge to novel facts. Old info anchors new info.
   - Structure: known_context → new_information → elaboration
   - Example: "You know Redis caches data" → "It uses in-memory storage" → "That's why it's microsecond-fast"
   - Why asymmetric: New information needs anchor; reversing leaves listener lost
   - Real-world: Teaching, documentation, explanatory writing

4. INTERACTIONAL (Adjacency Pairs)
   Social/discourse structure where first utterance creates obligation for second.
   - Structure: first_pair_part → second_pair_part → follow_up
   - Example: "How do I center a div?" → "Use flexbox on the parent" → "Set justify-content: center"
   - Why asymmetric: Answer cannot precede question in coherent discourse
   - Real-world: Q&A, dialogue, conversational exchanges

5. SEMANTIC (Entailment/Hyponymy)
   Logical asymmetry in word meanings. Specifics entail generalities, not vice versa.
   - Structure: specific_instance → general_category → implication
   - Example: "PostgreSQL is down" → "The database service is unavailable" → "API calls will fail"
   - Why asymmetric: Specific implies general (Honda→car), but general doesn't imply specific (car→Honda)
   - Real-world: Classification, categorization, logical reasoning

YOUR TASK:
Design a curriculum specification that enables generating exactly 3000 unique training batches.

OUTPUT THIS EXACT JSON STRUCTURE:

{
  "curriculum": [
    {
      "domain": "DOMAIN_NAME",
      "domain_description": "What this domain teaches about directional information gain",
      "batch_allocation": 600,
      
      "information_types": [
        {
          "type_id": "unique_identifier",
          "type_description": "What pattern this teaches",
          "batch_count": 150,
          
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - clause order mirrors event order in reality",
            "structure": "sentence_A → sentence_B → sentence_C (describe what each represents)",
            "example": "Concrete example of this 3-sentence pattern",
            "why_asymmetric": "Why forward direction adds value but backward doesn't",
            "real_world_application": "Where this pattern appears in actual usage"
          },
          
          "symmetric_pattern": {
            "structure": "sentence_X ↔ sentence_Y (describe the mutual relationship)",
            "example": "Concrete example of mutual information gain",
            "why_symmetric": "Why both directions add value"
          },
          
          "hard_negative_strategy": {
            "description": "What makes something look relevant but isn't",
            "examples": ["Example 1", "Example 2"],
            "why_negative": "Why these add zero functional value"
          },
          
          "variation_parameters": {
            "parameter_name_1": {
              "values": ["value1", "value2", "value3", "value4", "value5"],
              "why_this_varies": "How changing this creates genuinely different scenarios"
            },
            "parameter_name_2": {
              "values": ["value1", "value2", "value3", "value4"],
              "why_this_varies": "How changing this creates genuinely different scenarios"
            },
            "parameter_name_3": {
              "values": ["value1", "value2", "value3"],
              "why_this_varies": "How changing this creates genuinely different scenarios"
            }
          },
          
          "combination_space": 300,
          "notes": "Any special sampling considerations"
        }
      ]
    }
  ],
  
  "validation": {
    "total_batches": 3000,
    "total_domains": 6,
    "total_information_types": 20,
    "asymmetry_type_distribution": {
      "TEMPORAL": 600,
      "CAUSAL": 600,
      "EPISTEMIC": 600,
      "INTERACTIONAL": 600,
      "SEMANTIC": 600
    },
    "batch_distribution": {
      "asymmetric_focused": 1800,
      "symmetric_focused": 900,
      "balanced": 300
    }
  },
  
  "coverage_rationale": {
    "asymmetric_patterns": "All 5 linguistic asymmetry types equally represented with 600 batches each",
    "symmetric_patterns": ["List of symmetric patterns covered"],
    "hard_negative_types": ["List of hard negative strategies"],
    "why_complete": "Why this curriculum comprehensively teaches directional information gain using linguistic foundations"
  }
}

STRICT REQUIREMENTS:

1. DOMAINS (6-8 total)
   - Each domain should enable different types of linguistic asymmetry
   - Distribute asymmetry types across multiple domains (don't cluster all TEMPORAL in one domain)
   - Examples: 
     * PROCEDURAL_TASKS (good for TEMPORAL - steps in order)
     * TROUBLESHOOTING (good for CAUSAL - problem/solution)
     * KNOWLEDGE_EXPLANATION (good for EPISTEMIC - teaching new concepts)
     * CONVERSATIONAL_DIALOGUE (good for INTERACTIONAL - Q&A, adjacency pairs)
     * TECHNICAL_CLASSIFICATION (good for SEMANTIC - specific→general)
   
2. INFORMATION TYPES (20 total across all domains)
   - Each domain has 3-4 information types
   - Each information type gets 100-200 batches
   - All batch_counts must sum to exactly 3000
   - CRITICAL: Each information type must specify which asymmetry_type it uses from the 5 linguistic types

3. ASYMMETRY DISTRIBUTION (MUST BE EQUAL)
   - Each of the 5 asymmetry types should get exactly 600 batches (3000 ÷ 5 = 600)
   - TEMPORAL: 600 batches
   - CAUSAL: 600 batches
   - EPISTEMIC: 600 batches
   - INTERACTIONAL: 600 batches
   - SEMANTIC: 600 batches
   - No asymmetry type should have more than 650 or fewer than 550 batches

4. VARIATION PARAMETERS (for each information type)
   - Provide 3-5 parameters per information type
   - Each parameter has 3-7 distinct values
   - Parameters must be orthogonal (changing one doesn't force changing another)
   - combination_space = product of all parameter values (should be >= batch_count)
   - Focus on parameters that create FUNCTIONAL distinctness, not just keyword swapping

5. PATTERNS (for each information type)
   - asymmetric_pattern: Must show clear directional flow matching the specified linguistic asymmetry type
   - symmetric_pattern: Must show mutual information gain where both X→Y and Y→X are high
   - hard_negative_strategy: Must specify what shares domain/keywords but adds no value

6. BALANCE
   - 60% of batches should be asymmetric-focused (testing directional flow)
   - 30% of batches should be symmetric-focused (testing mutual relationships)
   - 10% of batches should be balanced/mixed

DESIGN PRINCIPLES:
- **EQUAL REPRESENTATION**: Each of the 5 linguistic asymmetry types gets exactly 600 batches
- Each asymmetry type should appear in multiple domains (distribute across curriculum)
- Include both concrete domains (cooking, repairs) and abstract domains (theory, concepts)
- Include both professional domains (technical, medical) and everyday domains (conversation, advice)
- Ensure hard negatives test keyword overlap without functional value
- Variation parameters should create genuinely different learning signals

EXAMPLES OF INFORMATION TYPES WITH LINGUISTIC ASYMMETRY SPECIFICATION:

Example 1 - TEMPORAL:
{
  "type_id": "recipe_execution",
  "batch_count": 150,
  "asymmetric_pattern": {
    "asymmetry_type": "TEMPORAL",
    "linguistic_principle": "Iconicity - cooking steps mirror actual sequence of actions",
    "structure": "preparation_step → cooking_action → result_check",
    "example": "Preheat oven to 350°F" → "Place dough on baking sheet" → "Bake until golden brown, about 15 minutes",
    "why_asymmetric": "Steps must occur in physical time order; reversing breaks procedural logic",
    "real_world_application": "Recipes, assembly instructions, procedural documentation"
  }
}

Example 2 - CAUSAL:
{
  "type_id": "system_troubleshooting",
  "batch_count": 150,
  "asymmetric_pattern": {
    "asymmetry_type": "CAUSAL",
    "linguistic_principle": "Cause must be established to understand effect and solution",
    "structure": "observed_problem → root_cause_diagnosis → corrective_action",
    "example": "API returns 500 errors" → "Database connection pool exhausted" → "Increase max_connections from 20 to 100",
    "why_asymmetric": "Solution only makes sense after understanding cause; problem doesn't help implement solution",
    "real_world_application": "Debugging, medical diagnosis, technical support"
  }
}

Example 3 - EPISTEMIC:
{
  "type_id": "concept_explanation",
  "batch_count": 150,
  "asymmetric_pattern": {
    "asymmetry_type": "EPISTEMIC",
    "linguistic_principle": "Given→New - anchor known concept, then introduce novel information",
    "structure": "familiar_concept → new_related_concept → technical_detail",
    "example": "You know arrays store data sequentially" → "Hash tables store data by computed keys" → "They use modulo operation to map keys to array indices",
    "why_asymmetric": "New information needs familiar anchor; starting with technical detail loses audience",
    "real_world_application": "Teaching, documentation, explanatory articles"
  }
}

Example 4 - INTERACTIONAL:
{
  "type_id": "technical_qa",
  "batch_count": 150,
  "asymmetric_pattern": {
    "asymmetry_type": "INTERACTIONAL",
    "linguistic_principle": "Adjacency pairs - question creates obligation for answer",
    "structure": "user_question → direct_answer → implementation_detail",
    "example": "How do I prevent SQL injection in Node.js?" → "Use parameterized queries with prepared statements" → "Example: db.query('SELECT * FROM users WHERE id = ?', [userId])",
    "why_asymmetric": "Answer addresses question; question doesn't help someone implementing the answer",
    "real_world_application": "Q&A forums, chatbots, customer support, documentation FAQs"
  }
}

Example 5 - SEMANTIC:
{
  "type_id": "error_classification",
  "batch_count": 150,
  "asymmetric_pattern": {
    "asymmetry_type": "SEMANTIC",
    "linguistic_principle": "Entailment - specific instance implies general category, not vice versa",
    "structure": "specific_error → general_category → system_implication",
    "example": "ECONNREFUSED on port 5432" → "Database connection failure" → "All data-dependent endpoints will return errors",
    "why_asymmetric": "Specific error entails general failure; general failure doesn't specify which error occurred",
    "real_world_application": "Error handling, logging systems, diagnostic tools"
  }
}

VALIDATION REQUIREMENT:
The asymmetry_type_distribution in your validation section MUST show equal distribution:
- Each of the 5 types gets exactly 600 batches
- Total across all 5 types must equal 3000

Return ONLY valid JSON. No explanation before or after.
"""
}