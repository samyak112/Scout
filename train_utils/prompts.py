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

**ASYMMETRY TYPES (Based on Linguistic Principles):**  
Your curriculum must cover these 5 fundamental asymmetric patterns:

1. **TEMPORAL (Iconicity Principle)**  
    Language mirrors the physical flow of time. Clause order reflects event order.
    
    - **Structure:** earlier_event → later_event → consequence
    - **Examples:**
        
        - "She woke up" → "She made coffee" → "She left for work"
        - "The volcano erupted" → "Ash covered the village" → "Flights were canceled"
        - "The movie started" → "The audience watched silently" → "Applause erupted at the end"
            
    - **Why asymmetric:** Reversing the order breaks the natural chronological flow of events
    - **Real-world:** Daily routines, historical events, sequences in storytelling
        
2. **CAUSAL (Explanation & Result)**  
    One idea is the condition for understanding the other. Cause must precede effect.
    
    - **Structure:** cause/need → mechanism/explanation → effect/action
    - **Examples:**
        
        - "Heavy rainfall flooded the streets" → "Cars were stuck" → "Commuters were delayed"
        - "She forgot her umbrella" → "She got wet in the rain" → "She caught a cold"
        - "The cake batter lacked sugar" → "The cake was bland" → "Guests asked for extra frosting"
            
    - **Why asymmetric:** The effect cannot be fully understood without knowing the cause first
    - **Real-world:** Natural phenomena, problem-solving, consequences of decisions
        
3. **EPISTEMIC (Given → New Information)**  
    Communication flows from shared knowledge to novel facts. Old info anchors new info.
    
    - **Structure:** known_context → new_information → elaboration
    - **Examples:**
        
        - "We know plants need sunlight" → "Sunlight powers photosynthesis" → "This explains why indoor plants grow slower"
        - "Everyone knows the Earth orbits the Sun" → "The orbit is slightly elliptical" → "This causes the variation in seasons"
        - "Dogs are mammals" → "They have specialized teeth for chewing" → "This explains why some dogs prefer bones over soft food"
            
    - **Why asymmetric:** New information depends on prior context; reversing may confuse the listener
    - **Real-world:** Teaching, news articles, instructional writing, science explanations
        
4. **INTERACTIONAL (Adjacency Pairs)**  
    Social/discourse structure where first utterance creates obligation for the second.
    
    - **Structure:** first_pair_part → second_pair_part → follow_up
    - **Examples:**
        
        - "Can I borrow your book?" → "Sure, here it is" → "Thanks, I’ll return it tomorrow"
        - "Would you like some tea?" → "Yes, please" → "Here you go"
        - "What time is the meeting?" → "It starts at 3 PM" → "Great, I’ll be ready"
            
    - **Why asymmetric:** Responses depend on the initial utterance; reversing creates incoherence
    - **Real-world:** Conversations, service interactions, social etiquette, chatbots
        
5. **SEMANTIC (Entailment/Hyponymy)**  
    Logical asymmetry in word meanings. Specifics entail generalities, not vice versa.
    
    - **Structure:** specific_instance → general_category → implication
        
    - **Examples:**
        
        - "A robin perched on the branch" → "The tree has birds" → "The birds may chirp loudly"
        - "Salmon swim upstream to spawn" → "Fish migrate seasonally" → "This affects local ecosystems"
        - "The Eiffel Tower is in Paris" → "Paris has famous landmarks" → "Tourists visit these landmarks"
            
    - **Why asymmetric:** Specific instances imply general categories, but not vice versa
    - **Real-world:** Observation, categorization, logical inference

###6. **QUERY-RESPONSE (Directional Knowledge Gain)**

Directional structure where the answer provides functional value to the query, but the query provides little to the answer.

- **Structure:** query → answer → elaboration/explanation
- **Examples:**
    
    - "What programming languages are best for web development?" → "JavaScript is widely used for frontend and backend frameworks" → "Frameworks like React and Node.js simplify development, increasing productivity"
    - "How can I reduce my electricity bill?" → "Switch to LED bulbs and smart thermostats" → "Smart thermostats adjust heating/cooling automatically based on usage patterns"
    - "Why do indoor plants grow slower than outdoor plants?" → "They receive less sunlight" → "Supplemental grow lights can improve growth rates"
        
- **Why asymmetric:** The answer and elaboration depend on the query; reversing direction provides minimal functional insight.
- **Real-world:** FAQs, customer support, tutoring systems, chatbots

---

**Mutual Value (Symmetric) (High→High):**  
This is what "symmetric" SHOULD be, but NOT paraphrases. Both sentences explain, elaborate, or complement each other.

- "Reading improves vocabulary" ↔ "Having a large vocabulary helps reading comprehension"
- "Exercising regularly boosts mood" ↔ "A better mood motivates consistent exercise"
- "Cooking at home saves money" ↔ "Saving money allows buying better ingredients"
- "Recycling reduces landfill waste" ↔ "Reducing landfill waste protects the environment"
- "Which languages are popular for machine learning?" ↔ "Python has rich libraries like TensorFlow and PyTorch"
- "How can I improve my sleep quality?" ↔ "Maintaining a consistent bedtime improves circadian rhythm"
    
**Use cases:** Segmentation, clustering, mutual explanation, complementary understanding.

**BAD SYMMETRIC EXAMPLES (DO NOT USE):**
"Triangular bracing increases stability" ↔ "Stable structures use triangular geometry"
   - This is just rewording the same fact

"Python is good for data science" ↔ "Data science benefits from Python"
   - Active/passive voice of same statement

"Exercise burns calories" ↔ "Calorie burning happens during exercise"
   - Paraphrase with no new information

**GOOD SYMMETRIC EXAMPLES:**
"Exercise burns calories" ↔ "Calorie deficits require consistent exercise"
   - Two different facts that support each other

"Python has rich data libraries" ↔ "Rich libraries attract data scientists to Python"
   - Complementary cause-effect that forms feedback loop

---

**No Value (Low→Low):**  
Sentences share a domain but do not provide functional value to each other. They may be topically related but don’t help one another.

- **Domain: Astronomy**
    
    - "The Moon orbits the Earth" ↔ "Mars has two moons"
    - Reason: Both are about celestial bodies, but knowing one does not help understand or act on the other.
        
- **Domain: Literature**
    
    - "Shakespeare wrote Hamlet" ↔ "Jane Austen wrote Pride and Prejudice"
    - Reason: Both are authors/works, but one sentence doesn’t explain or give context for the other.
        
- **Domain: Programming**
    
    - "Python uses indentation to define blocks" ↔ "Java supports multiple inheritance via interfaces"
    - Reason: Both are programming language facts, but neither provides functional value for understanding the other.
        
- **Domain: Cooking**
    
    - "Boiling pasta takes 10 minutes" ↔ "Using olive oil enhances salad flavor"
    - Reason: Both are culinary facts, but unrelated actions, no functional dependency.


STRICT REQUIREMENTS:

1. **DOMAINS (6-8 total)**
    
- Each domain should enable different types of linguistic asymmetry.
- Distribute asymmetry types across multiple domains (don’t cluster all TEMPORAL in one domain).
    
- Examples:
    
    - **PROCEDURAL_TASKS** (good for TEMPORAL – steps in order)
    - **TROUBLESHOOTING** (good for CAUSAL – problem/solution)
    - **KNOWLEDGE_EXPLANATION** (good for EPISTEMIC – teaching new concepts)
    - **CONVERSATIONAL_DIALOGUE** (good for INTERACTIONAL – Q&A, adjacency pairs)
    - **TECHNICAL_CLASSIFICATION** (good for SEMANTIC – specific → general)
    - **QUERY-RESPONSE** (good for directional knowledge gain – question → answer → elaboration)
            
2. **INFORMATION TYPES (20 total across all domains)**
    
    - Each domain has 3–4 information types.
    - Each information type gets 100–200 batches.
    - All batch_counts must sum to exactly 3000.
    - CRITICAL: Each information type must specify which **asymmetry_type** it uses from the 6 linguistic types (TEMPORAL, CAUSAL, EPISTEMIC, INTERACTIONAL, SEMANTIC, QUERY-RESPONSE).
        
3. **ASYMMETRY DISTRIBUTION (MUST BE EQUAL)**
    
    - Each of the 6 asymmetry types should get **exactly 500 batches** (3000 ÷ 6 = 500)
        
        - TEMPORAL: 500 batches
        - CAUSAL: 500 batches
        - EPISTEMIC: 500 batches
        - INTERACTIONAL: 500 batches
        - SEMANTIC: 500 batches
        - QUERY-RESPONSE: 500 batches
            
    - No asymmetry type should have more than 550 or fewer than 450 batches

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
- **EQUAL REPRESENTATION**: Each of the 6 linguistic asymmetry types gets exactly 600 batches
- Each asymmetry type should appear in multiple domains (distribute across curriculum)
- Ensure hard negatives test keyword overlap without functional value
- Variation parameters should create genuinely different learning signals

VALIDATION REQUIREMENT:
The asymmetry_type_distribution in your validation section MUST show equal distribution:
- Each of the 5 types gets exactly 600 batches
- Total across all 5 types must equal 3000

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



Return ONLY valid JSON. No explanation before or after.
""",
"generate_dataset":"""

You are generating a single training batch for a directional information gain model.

BATCH METADATA:
- Domain: {domain}
- Information Type: {information_type}

VARIATION PARAMETERS:
{parameters}

PATTERNS TO FOLLOW:
Asymmetric Pattern:
{asymmetric_data}

Symmetric Pattern:
{symmetric_data}

Hard Negative Strategy:
{hard_negative_data}

---

YOUR TASK:
Generate exactly 7 sentences that form one training batch.

The batch should contain diverse directional patterns so the model learns to score based on actual functional value, not patterns.

BATCH STRUCTURE:

**CHAIN (3 sentences): Train directional evaluation**
Follow the asymmetric pattern above. Create a 3-sentence chain where:
- A→B: score based on "does B add functional value to A?"
- B→C: score based on "does C add functional value to B?"
- Reverse directions: score based on actual functional value (often low, but not forced)
- Use ALL variation parameters to make sentences specific and concrete
- Must demonstrate the linguistic principle given above

Example chain:
- "My sink is clogged" → "Hair accumulates in P-traps" → "Remove the P-trap and clear it"
  - Forward (problem→cause→solution): each adds high functional value
  - Backward (solution→cause→problem): each adds little functional value
  - But score based on what you actually observe, not this pattern

**BIDIRECTIONAL PAIR (2 sentences): Train mutual information gain**  
Follow the bidirectional pattern above. Create 2 sentences where:

- A→B: B adds functional value to A (score appropriately)
- B→A: A adds functional value to B (score appropriately)
- Both directions should naturally have high scores
- Each sentence elaborates, explains, or complements the other
- Use variation parameters where relevant

**What makes a pair bidirectional:**

- "Water boils at 100°C at standard pressure" ↔ "The boiling point of water at 1 atm is 100°C"
    
    - A→B: HIGH (B clarifies the same fact in different wording)
    - B→A: HIGH (A reinforces the same fact)
        
- "Photosynthesis converts sunlight into chemical energy" ↔ "Plants use sunlight to produce sugars during photosynthesis"
    
    - A→B: HIGH (B elaborates the process described in A)
    - B→A: HIGH (A explains the underlying principle behind B)
        
- "A polygon is a closed figure with straight sides" ↔ "Polygons are flat shapes bounded by line segments"
    
    - A→B: HIGH (B restates A with equivalent clarity)
    - B→A: HIGH (A reinforces B’s definition)
        

**Guidelines:**

- Sentences must add **mutual, functional value**, not just be topically related
- Avoid hierarchical or causal relationships; focus on **pure equivalence / mutual elaboration**
  

**HARD NEGATIVES (2 sentences): Train to score low when appropriate**
Follow the hard negative strategy above. Create 2 sentences that:
- Share domain keywords/context with other sentences
- Add near-zero functional value to any other sentence
- Look topically related but provide no functional utility

---

CRITICAL REQUIREMENTS:

1. **Use variation parameters**: Incorporate ALL provided parameters
2. **Be specific**: Use concrete details, numbers, names, actions - no vague generalities
3. **Score each direction independently based on actual functional value**:
   - Don't force asymmetry or symmetry
   - Evaluate: "Given that I'm reading A, does B help me understand/execute/apply it?"
   - Then separately: "Given that I'm reading B, does A help me understand/execute/apply it?"

4. **Functional value means the reader can**:
   - Better understand the sentence
   - Execute instructions in the sentence
   - Make decisions based on the sentence
   - Fill in critical missing context

6. Keep sentences concise (one-liners)

---

FUNCTIONAL VALUE DEFINITION:

Sentence A adds functional value to sentence B if knowing A improves your ability to:
- Understand B correctly
- Execute or apply B
- Make decisions based on B
- Fill in missing context for B

**This is directional:** A→B asks "does A help me with B?"
Evaluate each direction independently.

SCORING SCALE (0.0 to 1.0):
- 0.0: No functional value (unrelated or redundant)
- 0.3: Weak connection (same topic, minimal help)
- 0.5: Moderate value (provides partial insight)
- 0.7: Strong value (meaningfully improves understanding)
- 0.9: Critical value (essential for correct interpretation)
- 1.0: Absolute dependency (B is meaningless without A)

**Score each directional relationship based on the actual functional value you observe.**
Don't target specific scores - let the relationships determine the scores naturally.

---

WHY THIS STRUCTURE:

The model learns to evaluate "does B add value to A?" in one direction at a time.
- Chain sentences: often create high forward, low backward (but score what you see)
- Bidirectional pairs: both directions naturally high (mutual elaboration)
- Hard negatives: all directions low (topic overlap without utility)

This teaches the model that **relevance is about utility, not similarity**.

OUTPUT FORMAT:

Return ONLY valid JSON:

{{
  "sentences": {{
    "thread1": [
      "First sentence in chain",
      "Second sentence in chain",
      "Third sentence in chain"
    ],
    "thread2": [
      "First concept sentence",
      "Second concept sentence"
    ],
    "hard_negatives": [
      "First hard negative",
      "Second hard negative"
    ]
  }},
  "scores": {{
    "thread1_internal": {{
      "zero_to_one": <score>,
      "one_to_two": <score>,
      "one_to_zero": <score>,
      "two_to_one": <score>,
      "zero_to_two": <score>,
      "two_to_zero": <score>
    }},
    "thread2_internal": {{
      "zero_to_one": <score>,
      "one_to_zero": <score>
    }},
    "cross_thread_avg": {{
      "thread1_to_thread2": <average score from any thread1 sentence to any thread2 sentence>,
      "thread2_to_thread1": <average score from any thread2 sentence to any thread1 sentence>
    }}
  }}
}}


NOTES:
- Hard negatives have 0.0 scores to everything (no need to list explicitly)
- Diagonal (sentence to itself) is always 0.0
- Score each pair honestly based on functional value
- Don't force specific score ranges - use the full 0.0-1.0 scale
- do not generate anything other than the given JSON done even write json

Now generate your batch using the provided metadata and parameters.
"""
}