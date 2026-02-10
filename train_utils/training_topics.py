TOPICS = {
  "curriculum": [
    {
      "domain": "PROCEDURAL_TASKS",
      "domain_description": "Teaches temporal sequencing where event order creates directional information flow - later steps depend on earlier ones",
      "batch_allocation": 500,
      
      "information_types": [
        {
          "type_id": "cooking_sequences",
          "type_description": "Multi-step cooking procedures where preparation order determines outcome",
          "batch_count": 150,
          
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - clause order mirrors the physical sequence of cooking actions in time",
            "structure": "preparation_step → cooking_action → result_observation",
            "example": "Dice the onions finely → Sauté them until golden brown → The kitchen fills with sweet aroma",
            "why_asymmetric": "You cannot sauté before dicing, and the aroma depends on completing both prior steps in order",
            "real_world_application": "Recipe instructions, cooking tutorials, meal prep guides"
          },
          
          "symmetric_pattern": {
            "structure": "cooking_technique ↔ ingredient_behavior (mutual explanation of why techniques work)",
            "example": "Marinating tenderizes tough meat ↔ Acidic ingredients break down protein fibers",
            "why_symmetric": "The technique explains the result, and understanding the chemistry explains why the technique works"
          },
          
          "hard_negative_strategy": {
            "description": "Different cooking facts from the same cuisine or ingredient category with no procedural dependency",
            "examples": ["Basil adds freshness to pasta ↔ Oregano is common in pizza", "Boiling pasta takes 10 minutes ↔ Baking bread requires yeast"],
            "why_negative": "Both are cooking knowledge but neither helps execute or understand the other"
          },
          
          "variation_parameters": {
            "cuisine_type": {
              "values": ["Italian", "Chinese", "Mexican", "Indian", "French"],
              "why_this_varies": "Different cuisines have distinct ingredient chains and preparation sequences"
            },
            "cooking_method": {
              "values": ["sautéing", "baking", "grilling", "steaming", "braising"],
              "why_this_varies": "Each method has unique temporal dependencies and heat application sequences"
            },
            "ingredient_category": {
              "values": ["vegetables", "meat", "grains", "seafood", "dairy"],
              "why_this_varies": "Different ingredients require different preparation sequences and timing"
            },
            "complexity": {
              "values": ["simple", "intermediate", "advanced"],
              "why_this_varies": "Complexity changes the number of dependent steps and branching procedures"
            }
          },
          
          "combination_space": 300,
          "notes": "Sample without replacement to ensure diverse cuisine-method-ingredient combinations"
        },
        {
          "type_id": "assembly_instructions",
          "type_description": "Physical assembly sequences where component order is critical",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - assembly language mirrors the physical construction sequence",
            "structure": "component_placement → attachment_action → stability_check",
            "example": "Align the bracket with the mounting holes → Tighten the screws clockwise → The shelf can now hold 50 pounds",
            "why_asymmetric": "Cannot tighten screws before aligning, and load capacity only emerges after proper assembly",
            "real_world_application": "Furniture assembly, electronics setup, mechanical repairs"
          },
          
          "symmetric_pattern": {
            "structure": "assembly_principle ↔ structural_reason (mutual explanation of construction logic)",
            "example": "Triangular bracing prevents wobbling ↔ Diagonal forces distribute weight evenly across joints",
            "why_symmetric": "The bracing technique explains stability, and physics explains why bracing works"
          },
          
          "hard_negative_strategy": {
            "description": "Assembly facts about different products or unrelated components",
            "examples": ["Shelves use L-brackets for support ↔ Desks have adjustable height legs", "Wood screws have coarse threads ↔ Metal bolts require nuts"],
            "why_negative": "Both relate to assembly but are independent facts with no procedural connection"
          },
          
          "variation_parameters": {
            "product_type": {
              "values": ["furniture", "electronics", "appliances", "toys", "fixtures"],
              "why_this_varies": "Different products have unique assembly sequences and component dependencies"
            },
            "fastener_type": {
              "values": ["screws", "bolts", "clips", "adhesive", "dowels"],
              "why_this_varies": "Each fastener requires different installation sequences and tools"
            },
            "material": {
              "values": ["wood", "metal", "plastic", "composite"],
              "why_this_varies": "Materials demand different preparation and connection methods"
            },
            "scale": {
              "values": ["small_item", "medium_furniture", "large_structure"],
              "why_this_varies": "Scale affects the number of components and complexity of assembly order"
            },
            "tool_requirement": {
              "values": ["hand_tools", "power_tools", "no_tools"],
              "why_this_varies": "Tool use creates different action sequences and dependencies"
            }
          },
          
          "combination_space": 240,
          "notes": "Ensure material-fastener combinations are realistic (avoid wood-welding, etc.)"
        },
        {
          "type_id": "daily_routines",
          "type_description": "Habitual action sequences where order creates efficiency or necessity",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - routine descriptions follow the chronological flow of activities",
            "structure": "initiating_action → dependent_action → consequential_state",
            "example": "She set her alarm for 6 AM → She woke up and exercised → She arrived at work energized",
            "why_asymmetric": "Cannot exercise before waking, and arriving energized depends on completing the prior routine",
            "real_world_application": "Habit formation, productivity advice, time management, wellness programs"
          },
          
          "symmetric_pattern": {
            "structure": "habit_benefit ↔ motivation_mechanism (mutual reinforcement)",
            "example": "Morning exercise boosts energy levels ↔ Higher energy motivates consistent morning workouts",
            "why_symmetric": "The benefit explains the motivation, and the motivation sustains the habit that produces the benefit"
          },
          
          "hard_negative_strategy": {
            "description": "Unrelated routine facts from different times of day or contexts",
            "examples": ["Morning coffee improves alertness ↔ Evening reading promotes relaxation", "Commuting by bike saves money ↔ Meal prepping on Sundays saves time"],
            "why_negative": "Both are routine optimizations but operate independently with no sequential dependency"
          },
          
          "variation_parameters": {
            "routine_category": {
              "values": ["morning", "work", "evening", "fitness", "meal"],
              "why_this_varies": "Different routines have distinct temporal structures and constraints"
            },
            "goal_type": {
              "values": ["productivity", "health", "learning", "social", "rest"],
              "why_this_varies": "Goals determine which actions are preparatory vs. terminal in the sequence"
            },
            "time_constraint": {
              "values": ["rushed", "moderate", "leisurely"],
              "why_this_varies": "Time pressure changes which steps are essential vs. optional in the sequence"
            },
            "context": {
              "values": ["weekday", "weekend", "travel", "home"],
              "why_this_varies": "Context changes available resources and necessary preparation steps"
            }
          },
          
          "combination_space": 240,
          "notes": "Focus on routines where temporal order is functionally important, not arbitrary"
        }
      ]
    },
    {
      "domain": "TROUBLESHOOTING",
      "domain_description": "Teaches causal reasoning where problems, mechanisms, and solutions form directional dependency chains",
      "batch_allocation": 500,
      
      "information_types": [
        {
          "type_id": "technical_problems",
          "type_description": "Device malfunctions where symptoms point to causes and causes determine solutions",
          "batch_count": 150,
          
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Explanation and result - the cause is the condition for understanding the effect",
            "structure": "symptom_observed → underlying_cause → corrective_action",
            "example": "The laptop won't charge → The charging port is loose → Reseat the connection firmly",
            "why_asymmetric": "The solution only makes sense after understanding the cause, which explains the symptom",
            "real_world_application": "Tech support, device manuals, diagnostic procedures, repair guides"
          },
          
          "symmetric_pattern": {
            "structure": "problem_indicator ↔ diagnostic_method (mutual explanation)",
            "example": "Slow performance indicates insufficient RAM ↔ Checking RAM usage reveals performance bottlenecks",
            "why_symmetric": "The symptom suggests the diagnostic, and the diagnostic confirms the symptom's cause"
          },
          
          "hard_negative_strategy": {
            "description": "Unrelated technical facts about different devices or failure modes",
            "examples": ["Printers jam with thick paper ↔ Monitors flicker with bad cables", "Batteries drain faster in cold weather ↔ Speakers crackle when volume is too high"],
            "why_negative": "Both are device issues but don't form a causal chain - knowing one doesn't help diagnose or fix the other"
          },
          
          "variation_parameters": {
            "device_type": {
              "values": ["laptop", "smartphone", "printer", "router", "monitor"],
              "why_this_varies": "Different devices have unique failure modes and diagnostic procedures"
            },
            "failure_category": {
              "values": ["power", "connectivity", "performance", "hardware", "software"],
              "why_this_varies": "Each category has distinct symptom-cause-solution chains"
            },
            "severity": {
              "values": ["minor", "moderate", "critical"],
              "why_this_varies": "Severity affects the complexity of the causal chain and intervention needed"
            },
            "user_skill": {
              "values": ["beginner", "intermediate", "advanced"],
              "why_this_varies": "Skill level changes the explanation depth needed to link cause to solution"
            }
          },
          
          "combination_space": 300,
          "notes": "Ensure symptom-cause pairs are realistic based on actual device failure modes"
        },
        {
          "type_id": "household_issues",
          "type_description": "Home maintenance problems with clear causal chains from issue to fix",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Explanation and result - home problems require understanding causes before applying fixes",
            "structure": "household_problem → root_cause → solution_method",
            "example": "Water pools around the sink → The drain seal is cracked → Replace the rubber gasket",
            "why_asymmetric": "The fix targets the cause; reversing gives you a solution without understanding what it solves",
            "real_world_application": "Home repair guides, maintenance checklists, DIY tutorials"
          },
          
          "symmetric_pattern": {
            "structure": "prevention_method ↔ damage_mechanism (mutual explanation)",
            "example": "Regular gutter cleaning prevents water damage ↔ Clogged gutters overflow and rot the fascia",
            "why_symmetric": "Prevention explains how to avoid damage, damage mechanism explains why prevention works"
          },
          
          "hard_negative_strategy": {
            "description": "Different household maintenance facts with no causal connection",
            "examples": ["Leaky faucets waste water ↔ Clogged drains smell bad", "Peeling paint indicates moisture ↔ Squeaky hinges need lubrication"],
            "why_negative": "Both are home issues but independent - fixing one doesn't inform the other"
          },
          
          "variation_parameters": {
            "system_type": {
              "values": ["plumbing", "electrical", "HVAC", "structural", "appliance"],
              "why_this_varies": "Different systems have unique failure mechanisms and repair approaches"
            },
            "problem_source": {
              "values": ["wear_and_tear", "installation_error", "environmental", "misuse"],
              "why_this_varies": "Different sources lead to different diagnostic and repair chains"
            },
            "location": {
              "values": ["kitchen", "bathroom", "basement", "exterior", "living_area"],
              "why_this_varies": "Location affects the problem types and available solutions"
            },
            "fix_complexity": {
              "values": ["simple", "moderate", "requires_professional"],
              "why_this_varies": "Complexity determines the detail needed in the causal explanation"
            },
            "urgency": {
              "values": ["immediate", "soon", "routine_maintenance"],
              "why_this_varies": "Urgency affects whether quick fixes or thorough causal understanding is prioritized"
            }
          },
          
          "combination_space": 300,
          "notes": "Focus on common household issues where cause-effect relationships are clear"
        },
        {
          "type_id": "software_debugging",
          "type_description": "Code errors where bugs, causes, and fixes form logical dependency chains",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Explanation and result - debugging requires understanding error causes before implementing fixes",
            "structure": "error_message → code_issue → fix_implementation",
            "example": "IndexError: list index out of range → Loop counter exceeds list length → Add boundary check before access",
            "why_asymmetric": "The fix addresses the specific cause; knowing the fix without the cause provides no debugging insight",
            "real_world_application": "Debugging sessions, error documentation, programming tutorials, stack overflow answers"
          },
          
          "symmetric_pattern": {
            "structure": "coding_practice ↔ error_prevention (mutual reinforcement)",
            "example": "Input validation prevents type errors ↔ Type errors indicate missing input validation",
            "why_symmetric": "The practice prevents the error class, and the error class reveals gaps in the practice"
          },
          
          "hard_negative_strategy": {
            "description": "Unrelated programming facts or errors from different contexts",
            "examples": ["Python uses dynamic typing ↔ JavaScript has hoisting behavior", "Memory leaks occur in C++ ↔ Syntax errors break Python scripts"],
            "why_negative": "Both are programming knowledge but don't form causal chains - different languages, different error types"
          },
          
          "variation_parameters": {
            "language": {
              "values": ["Python", "JavaScript", "Java", "C++", "SQL"],
              "why_this_varies": "Languages have distinct error types and debugging approaches"
            },
            "error_type": {
              "values": ["runtime", "syntax", "logic", "type", "memory"],
              "why_this_varies": "Different error types have different causal chains from symptom to fix"
            },
            "code_context": {
              "values": ["data_processing", "web_api", "algorithm", "database_query", "UI_component"],
              "why_this_varies": "Context determines what operations are being performed and what can fail"
            },
            "debugging_approach": {
              "values": ["print_statements", "debugger", "logging", "unit_tests"],
              "why_this_varies": "Different approaches reveal causes through different investigation paths"
            }
          },
          
          "combination_space": 240,
          "notes": "Use realistic error-cause-fix triplets based on common programming mistakes"
        }
      ]
    },
    {
      "domain": "KNOWLEDGE_EXPLANATION",
      "domain_description": "Teaches epistemic flow from known context to new information, anchoring novel facts in prior understanding",
      "batch_allocation": 500,
      
      "information_types": [
        {
          "type_id": "science_concepts",
          "type_description": "Scientific explanations that build from familiar phenomena to deeper mechanisms",
          "batch_count": 150,
          
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given to new information - new scientific facts must be anchored in established knowledge",
            "structure": "common_knowledge → scientific_mechanism → advanced_implication",
            "example": "Everyone knows ice floats in water → Water expands when it freezes due to hydrogen bonding → This explains why pipes burst in winter",
            "why_asymmetric": "The mechanism builds on the familiar observation, and the implication requires understanding the mechanism first",
            "real_world_application": "Science education, popular science writing, textbooks, explainer videos"
          },
          
          "symmetric_pattern": {
            "structure": "scientific_principle ↔ practical_application (mutual illumination)",
            "example": "Antibiotics kill bacteria by disrupting cell walls ↔ Bacterial resistance develops when cell walls mutate",
            "why_symmetric": "The principle explains how treatment works, and resistance mechanisms reveal limits of the principle"
          },
          
          "hard_negative_strategy": {
            "description": "Unrelated scientific facts from different domains",
            "examples": ["DNA stores genetic information ↔ Black holes warp spacetime", "Photosynthesis requires sunlight ↔ Metals conduct electricity"],
            "why_negative": "Both are science facts but operate in different domains with no epistemic dependency"
          },
          
          "variation_parameters": {
            "scientific_field": {
              "values": ["physics", "chemistry", "biology", "earth_science", "astronomy"],
              "why_this_varies": "Different fields have distinct explanatory frameworks and knowledge scaffolds"
            },
            "complexity_level": {
              "values": ["elementary", "middle_school", "high_school", "undergraduate"],
              "why_this_varies": "Complexity determines how much prior knowledge is assumed vs. explained"
            },
            "phenomenon_type": {
              "values": ["observable_daily", "lab_experiment", "natural_process", "technological"],
              "why_this_varies": "Different phenomena require different anchoring in prior experience"
            },
            "explanation_style": {
              "values": ["mechanistic", "analogical", "mathematical", "historical"],
              "why_this_varies": "Style changes how new information connects to what's already known"
            }
          },
          
          "combination_space": 240,
          "notes": "Ensure the 'common knowledge' baseline is age-appropriate for the complexity level"
        },
        {
          "type_id": "historical_context",
          "type_description": "Historical narratives where background enables understanding of events and consequences",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given to new information - historical events require context to understand significance",
            "structure": "established_background → historical_event → lasting_consequence",
            "example": "Colonial powers competed for global trade routes → The Suez Canal opened in 1869 → Maritime shipping shifted permanently from around Africa to through the Mediterranean",
            "why_asymmetric": "The event's significance emerges from the prior context, and the consequence depends on understanding both",
            "real_world_application": "History education, documentaries, museum exhibits, historical analysis"
          },
          
          "symmetric_pattern": {
            "structure": "historical_trend ↔ cultural_shift (mutual explanation)",
            "example": "The printing press democratized knowledge access ↔ Widespread literacy enabled the Scientific Revolution",
            "why_symmetric": "Technology explains social change, and social change reveals technology's impact"
          },
          
          "hard_negative_strategy": {
            "description": "Historical facts from different eras or regions with no contextual connection",
            "examples": ["The Roman Empire fell in 476 CE ↔ The Ming Dynasty built the Forbidden City", "Napoleon was exiled to Elba ↔ The Magna Carta limited royal power"],
            "why_negative": "Both are historical facts but independent - knowing one doesn't contextualize the other"
          },
          
          "variation_parameters": {
            "time_period": {
              "values": ["ancient", "medieval", "early_modern", "modern", "contemporary"],
              "why_this_varies": "Different eras have different contextual frameworks and prior knowledge"
            },
            "geographical_region": {
              "values": ["Europe", "Asia", "Americas", "Africa", "Middle_East"],
              "why_this_varies": "Regions have distinct historical narratives and contextual anchors"
            },
            "event_type": {
              "values": ["political", "technological", "cultural", "economic", "military"],
              "why_this_varies": "Event types require different kinds of background context"
            },
            "scope": {
              "values": ["local", "national", "regional", "global"],
              "why_this_varies": "Scope determines what level of context is necessary for understanding"
            },
            "narrative_focus": {
              "values": ["causes", "key_figures", "consequences", "turning_points"],
              "why_this_varies": "Focus shifts what prior knowledge anchors the new information"
            }
          },
          
          "combination_space": 300,
          "notes": "Ensure background-event-consequence chains are historically accurate"
        },
        {
          "type_id": "educational_content",
          "type_description": "Teaching progressions where foundational concepts enable understanding of advanced topics",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given to new information - learning builds from prerequisites to new concepts",
            "structure": "prerequisite_concept → new_topic → application_skill",
            "example": "Students understand basic algebra → Quadratic equations extend the concept of solving for unknowns → This enables modeling projectile motion",
            "why_asymmetric": "New topics depend on prerequisites, and applications require understanding the new topic first",
            "real_world_application": "Curriculum design, online courses, tutoring, instructional materials"
          },
          
          "symmetric_pattern": {
            "structure": "learning_method ↔ skill_development (mutual reinforcement)",
            "example": "Practice problems reinforce conceptual understanding ↔ Strong concepts enable solving harder problems",
            "why_symmetric": "Practice deepens understanding, and understanding enables tackling more complex practice"
          },
          
          "hard_negative_strategy": {
            "description": "Educational facts from unrelated subjects or skill areas",
            "examples": ["Fractions represent parts of wholes ↔ Shakespeare used iambic pentameter", "The periodic table organizes elements ↔ Photosynthesis occurs in chloroplasts"],
            "why_negative": "Both are educational content but from different domains with no prerequisite relationship"
          },
          
          "variation_parameters": {
            "subject_area": {
              "values": ["mathematics", "language_arts", "natural_sciences", "social_studies", "arts"],
              "why_this_varies": "Subjects have different knowledge scaffolds and prerequisite structures"
            },
            "grade_level": {
              "values": ["elementary", "middle", "high_school", "college"],
              "why_this_varies": "Grade level determines assumed prior knowledge and complexity of new information"
            },
            "pedagogical_approach": {
              "values": ["conceptual", "procedural", "inquiry_based", "project_based"],
              "why_this_varies": "Approach changes how new information connects to existing knowledge"
            },
            "learning_objective": {
              "values": ["understanding", "application", "analysis", "synthesis"],
              "why_this_varies": "Objectives determine the depth of prerequisite knowledge needed"
            }
          },
          
          "combination_space": 240,
          "notes": "Align prerequisite-new_topic pairs with standard curriculum sequences"
        }
      ]
    },
    {
      "domain": "CONVERSATIONAL_DIALOGUE",
      "domain_description": "Teaches interactional structure where first utterances create obligations for responses in social exchanges",
      "batch_allocation": 500,
      
      "information_types": [
        {
          "type_id": "customer_service",
          "type_description": "Service interactions where requests create expectations for specific response types",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Adjacency pairs - first utterance establishes the conversational obligation for the second",
            "structure": "customer_request → service_response → follow_up_action",
            "example": "I'd like to return this defective item → Certainly, do you have your receipt? → Yes, here it is",
            "why_asymmetric": "The response is contextually bound to the request; reversing creates conversational incoherence",
            "real_world_application": "Customer service training, chatbot design, service scripts, communication protocols"
          },
          
          "symmetric_pattern": {
            "structure": "service_policy ↔ customer_expectation (mutual understanding)",
            "example": "Returns are accepted within 30 days ↔ Customers expect flexible return windows for satisfaction",
            "why_symmetric": "Policy shapes expectations, and expectations inform policy design"
          },
          
          "hard_negative_strategy": {
            "description": "Service facts that don't form request-response pairs",
            "examples": ["Store hours are 9 AM to 9 PM ↔ We accept credit cards and cash", "The warranty covers manufacturing defects ↔ Free shipping on orders over $50"],
            "why_negative": "Both are service information but neither creates conversational obligation for the other"
          },
          
          "variation_parameters": {
            "service_type": {
              "values": ["retail", "tech_support", "hospitality", "healthcare", "banking"],
              "why_this_varies": "Different services have distinct request-response patterns and protocols"
            },
            "request_category": {
              "values": ["information", "complaint", "transaction", "modification", "assistance"],
              "why_this_varies": "Request types establish different response obligations"
            },
            "customer_tone": {
              "values": ["polite", "urgent", "frustrated", "confused"],
              "why_this_varies": "Tone affects the appropriate response structure while maintaining the adjacency pair"
            },
            "resolution_path": {
              "values": ["immediate", "escalated", "deferred", "alternative_offered"],
              "why_this_varies": "Resolution paths create different follow-up obligations"
            },
            "channel": {
              "values": ["in_person", "phone", "chat", "email"],
              "why_this_varies": "Channels have different conversational norms for the same request-response pair"
            }
          },
          
          "combination_space": 240,
          "notes": "Ensure request-response pairs follow realistic service interaction patterns"
        },
        {
          "type_id": "social_exchanges",
          "type_description": "Everyday social interactions with conventional adjacency pair structures",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Adjacency pairs - social utterances create specific response expectations based on conventions",
            "structure": "social_opening → expected_response → conversation_continuation",
            "example": "How are you doing today? → I'm well, thanks for asking → That's great to hear",
            "why_asymmetric": "The response is socially obligated by the greeting; reversing violates conversational norms",
            "real_world_application": "Social skills training, language learning, politeness research, communication education"
          },
          
          "symmetric_pattern": {
            "structure": "social_norm ↔ relationship_maintenance (mutual reinforcement)",
            "example": "Expressing gratitude strengthens relationships ↔ Strong relationships encourage reciprocal appreciation",
            "why_symmetric": "Norms maintain relationships, and relationships motivate adherence to norms"
          },
          
          "hard_negative_strategy": {
            "description": "Social facts that don't form adjacency pairs",
            "examples": ["Handshakes are common greetings ↔ Business cards are exchanged in meetings", "Eye contact shows engagement ↔ Nodding indicates agreement"],
            "why_negative": "Both are social behaviors but independent - neither creates conversational obligation for the other"
          },
          
          "variation_parameters": {
            "interaction_type": {
              "values": ["greeting", "invitation", "apology", "compliment", "offer"],
              "why_this_varies": "Different interaction types have distinct conventional response structures"
            },
            "relationship": {
              "values": ["strangers", "acquaintances", "friends", "professional", "family"],
              "why_this_varies": "Relationships change the expected formality and content of responses"
            },
            "cultural_context": {
              "values": ["Western", "East_Asian", "Middle_Eastern", "Latin_American"],
              "why_this_varies": "Cultures have different conventions for what responses are obligated"
            },
            "setting": {
              "values": ["casual", "formal", "workplace", "social_event"],
              "why_this_varies": "Settings establish different appropriateness criteria for response pairs"
            }
          },
          
          "combination_space": 192,
          "notes": "Use culturally appropriate adjacency pairs for each cultural context"
        },
        {
          "type_id": "information_requests",
          "type_description": "Questions that obligate specific types of informational responses",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Adjacency pairs - questions establish obligation to provide relevant answers",
            "structure": "information_question → relevant_answer → clarification_or_thanks",
            "example": "What time does the library close? → It closes at 8 PM on weekdays → Perfect, thank you",
            "why_asymmetric": "The answer fulfills the question's information need; reversing provides no useful exchange",
            "real_world_application": "Information services, help desks, educational Q&A, reference systems"
          },
          
          "symmetric_pattern": {
            "structure": "question_clarity ↔ answer_precision (mutual improvement)",
            "example": "Specific questions elicit precise answers ↔ Precise answers encourage more specific follow-up questions",
            "why_symmetric": "Question quality improves answers, and good answers enable better questioning"
          },
          
          "hard_negative_strategy": {
            "description": "Unrelated questions and answers from different information domains",
            "examples": ["What's the weather forecast? ↔ The train arrives at 3 PM", "Where is the nearest ATM? ↔ The museum opens at 10 AM"],
            "why_negative": "Both are Q&A but the answer doesn't address the question - no adjacency pair formed"
          },
          
          "variation_parameters": {
            "question_type": {
              "values": ["location", "time", "process", "definition", "comparison"],
              "why_this_varies": "Question types obligate different information structures in responses"
            },
            "domain": {
              "values": ["navigation", "scheduling", "technical", "academic", "practical"],
              "why_this_varies": "Domains determine the knowledge base needed for appropriate answers"
            },
            "specificity": {
              "values": ["broad", "focused", "detailed"],
              "why_this_varies": "Specificity affects the scope and precision of the expected answer"
            },
            "context": {
              "values": ["public_space", "workplace", "educational", "online"],
              "why_this_varies": "Context changes what information is readily available and how it's delivered"
            },
            "urgency": {
              "values": ["immediate_need", "planning_ahead", "casual_interest"],
              "why_this_varies": "Urgency affects the conciseness expected in the response"
            }
          },
          
          "combination_space": 240,
          "notes": "Ensure question-answer pairs are contextually matched and realistic"
        },
        {
          "type_id": "negotiation_exchanges",
          "type_description": "Proposal-response interactions where offers create expectations for acceptance, rejection, or counter-offers",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Adjacency pairs - proposals obligate specific response types (accept/reject/counter)",
            "structure": "proposal_or_offer → response_move → resolution_or_continuation",
            "example": "I can deliver the project by Friday for $500 → Could you do Thursday for the same price? → Yes, I can make that work",
            "why_asymmetric": "The counter-offer is contextually bound to the initial proposal; reversing breaks the negotiation flow",
            "real_world_application": "Business negotiations, conflict resolution, sales conversations, diplomatic exchanges"
          },
          
          "symmetric_pattern": {
            "structure": "negotiation_tactic ↔ strategic_response (mutual adaptation)",
            "example": "Starting with a higher price leaves negotiation room ↔ Countering low signals willingness to meet in the middle",
            "why_symmetric": "Opening tactics predict responses, and responses reveal the effectiveness of tactics"
          },
          
          "hard_negative_strategy": {
            "description": "Negotiation facts that don't form proposal-response pairs",
            "examples": ["Deadlines create urgency in negotiations ↔ Written contracts formalize agreements", "Building rapport improves outcomes ↔ Market research informs pricing"],
            "why_negative": "Both are negotiation concepts but independent - neither obligates the other in conversation"
          },
          
          "variation_parameters": {
            "negotiation_domain": {
              "values": ["business_deal", "salary", "purchase", "partnership", "conflict_resolution"],
              "why_this_varies": "Domains have different stakes and conventional proposal-response patterns"
            },
            "move_type": {
              "values": ["initial_offer", "counter_offer", "concession", "rejection", "acceptance"],
              "why_this_varies": "Different moves create different obligations for the next conversational turn"
            },
            "power_dynamic": {
              "values": ["equal", "proposer_advantage", "responder_advantage"],
              "why_this_varies": "Power affects what responses are pragmatically available and expected"
            },
            "stakes": {
              "values": ["low", "moderate", "high"],
              "why_this_varies": "Stakes influence the complexity and indirectness of proposal-response sequences"
            }
          },
          
          "combination_space": 192,
          "notes": "Model realistic negotiation turn sequences with appropriate power dynamics"
        }
      ]
    },
    {
      "domain": "TECHNICAL_CLASSIFICATION",
      "domain_description": "Teaches semantic entailment where specific instances logically imply general categories but not vice versa",
      "batch_allocation": 500,
      
      "information_types": [
        {
          "type_id": "biological_taxonomy",
          "type_description": "Species-genus-family hierarchies where specific organisms entail broader classifications",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Entailment and hyponymy - specific instances logically imply general categories",
            "structure": "specific_organism → broader_category → taxonomic_implication",
            "example": "A golden retriever played in the yard → A dog was outside → A mammal was present",
            "why_asymmetric": "Specific instances entail general categories, but general categories don't specify which instance",
            "real_world_application": "Biological classification, biodiversity databases, species identification, ecological surveys"
          },
          
          "symmetric_pattern": {
            "structure": "taxonomic_trait ↔ classification_basis (mutual explanation)",
            "example": "Warm-blooded animals regulate body temperature ↔ Temperature regulation defines the mammal-bird distinction from reptiles",
            "why_symmetric": "The trait explains the classification, and the classification is defined by the trait"
          },
          
          "hard_negative_strategy": {
            "description": "Different organisms from unrelated taxonomic branches",
            "examples": ["Eagles are birds of prey ↔ Salmon are migratory fish", "Roses belong to Rosaceae ↔ Mushrooms are fungi"],
            "why_negative": "Both are taxonomic facts but no entailment relationship - different branches"
          },
          
          "variation_parameters": {
            "taxonomic_level": {
              "values": ["species", "genus", "family", "order", "class"],
              "why_this_varies": "Different levels create different entailment chains and specificity"
            },
            "organism_type": {
              "values": ["mammals", "birds", "fish", "plants", "insects"],
              "why_this_varies": "Different organism types have distinct classification hierarchies"
            },
            "habitat": {
              "values": ["terrestrial", "aquatic", "aerial", "underground"],
              "why_this_varies": "Habitat adds contextual specificity while maintaining entailment structure"
            },
            "trait_focus": {
              "values": ["morphology", "behavior", "reproduction", "diet"],
              "why_this_varies": "Different traits create different paths through the taxonomic hierarchy"
            },
            "observation_context": {
              "values": ["wild", "captive", "fossil_record", "laboratory"],
              "why_this_varies": "Context adds specificity to the instance without breaking the entailment"
            }
          },
          
          "combination_space": 240,
          "notes": "Ensure taxonomic chains are scientifically accurate"
        },
        {
          "type_id": "material_properties",
          "type_description": "Specific materials entailing general property categories",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Entailment and hyponymy - specific materials entail their property classes",
            "structure": "specific_material → material_class → property_implication",
            "example": "The component is made of copper → It's a metal → It conducts electricity",
            "why_asymmetric": "Copper entails 'metal' and inherits properties; 'metal' doesn't specify which one",
            "real_world_application": "Materials engineering, manufacturing specs, product design, quality control"
          },
          
          "symmetric_pattern": {
            "structure": "material_property ↔ application_suitability (mutual determination)",
            "example": "High thermal conductivity enables heat dissipation ↔ Heat sinks require materials with high thermal conductivity",
            "why_symmetric": "Property determines application, and application requirements define needed properties"
          },
          
          "hard_negative_strategy": {
            "description": "Materials from different property classes with no entailment",
            "examples": ["Copper conducts electricity ↔ Glass is transparent", "Steel is strong ↔ Rubber is elastic"],
            "why_negative": "Both are material facts but different property domains - no hierarchical relationship"
          },
          
          "variation_parameters": {
            "material_category": {
              "values": ["metals", "polymers", "ceramics", "composites", "semiconductors"],
              "why_this_varies": "Categories have different property hierarchies and entailment structures"
            },
            "property_type": {
              "values": ["electrical", "thermal", "mechanical", "optical", "chemical"],
              "why_this_varies": "Different properties create different classification and entailment patterns"
            },
            "application_domain": {
              "values": ["construction", "electronics", "automotive", "aerospace", "medical"],
              "why_this_varies": "Applications highlight different property implications of the material class"
            },
            "specificity_level": {
              "values": ["alloy", "base_material", "general_class"],
              "why_this_varies": "Specificity determines the length of the entailment chain"
            }
          },
          
          "combination_space": 192,
          "notes": "Use accurate material science classifications and property relationships"
        },
        {
          "type_id": "geographic_containment",
          "type_description": "Specific locations entailing broader geographic regions",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Entailment and hyponymy - specific locations logically entail containing regions",
            "structure": "specific_location → containing_region → geographic_implication",
            "example": "The Eiffel Tower is a famous landmark → It's in Paris → It's in France",
            "why_asymmetric": "Specific location entails the broader region; the region doesn't specify the landmark",
            "real_world_application": "Geographic information systems, location-based services, travel planning, logistics"
          },
          
          "symmetric_pattern": {
            "structure": "regional_characteristic ↔ location_identity (mutual definition)",
            "example": "Paris is known for artistic heritage ↔ Artistic heritage defines Paris's cultural identity",
            "why_symmetric": "Characteristics define the region, and the region exemplifies those characteristics"
          },
          
          "hard_negative_strategy": {
            "description": "Locations in different geographic hierarchies with no containment",
            "examples": ["Tokyo is in Japan ↔ London is in England", "The Alps are in Europe ↔ The Andes are in South America"],
            "why_negative": "Both are geographic facts but no containment relationship - parallel hierarchies"
          },
          
          "variation_parameters": {
            "location_type": {
              "values": ["landmark", "city", "region", "country", "continent"],
              "why_this_varies": "Different types create different levels in the containment hierarchy"
            },
            "geographic_scale": {
              "values": ["neighborhood", "metropolitan", "national", "international"],
              "why_this_varies": "Scale determines the number of entailment steps in the hierarchy"
            },
            "feature_category": {
              "values": ["cultural", "natural", "political", "economic"],
              "why_this_varies": "Category affects what implications follow from the geographic containment"
            },
            "specificity": {
              "values": ["address", "district", "city", "region"],
              "why_this_varies": "Specificity creates longer or shorter entailment chains"
            }
          },
          
          "combination_space": 192,
          "notes": "Ensure geographic containment relationships are factually correct"
        },
        {
          "type_id": "technical_hierarchies",
          "type_description": "Specific technologies or methods entailing broader technical categories",
          "batch_count": 125,
          
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Entailment and hyponymy - specific technologies entail their superordinate categories",
            "structure": "specific_technology → technology_class → capability_implication",
            "example": "The system uses convolutional neural networks → It employs deep learning → It can process images automatically",
            "why_asymmetric": "Specific tech entails the broader category and inherits capabilities; category doesn't specify which tech",
            "real_world_application": "Technology assessment, patent classification, requirements analysis, vendor selection"
          },
          
          "symmetric_pattern": {
            "structure": "technical_capability ↔ problem_suitability (mutual alignment)",
            "example": "Neural networks excel at pattern recognition ↔ Pattern recognition problems benefit from neural network approaches",
            "why_symmetric": "Capability determines problem fit, and problem requirements reveal needed capabilities"
          },
          
          "hard_negative_strategy": {
            "description": "Technologies from different categorical hierarchies",
            "examples": ["Blockchain ensures transaction immutability ↔ Solar panels convert sunlight to electricity", "5G enables low-latency communication ↔ CRISPR edits genetic sequences"],
            "why_negative": "Both are technologies but from unrelated categories - no entailment relationship"
          },
          
          "variation_parameters": {
            "technology_domain": {
              "values": ["AI_ML", "networking", "data_storage", "manufacturing", "energy"],
              "why_this_varies": "Domains have different technical hierarchies and entailment structures"
            },
            "abstraction_level": {
              "values": ["implementation", "method", "approach", "paradigm"],
              "why_this_varies": "Abstraction level determines the position in the entailment hierarchy"
            },
            "capability_type": {
              "values": ["processing", "storage", "communication", "automation", "analysis"],
              "why_this_varies": "Different capabilities create different implication chains from the specific instance"
            },
            "maturity": {
              "values": ["emerging", "established", "mature", "legacy"],
              "why_this_varies": "Maturity affects the richness of the entailment context"
            }
          },
          
          "combination_space": 192,
          "notes": "Maintain accurate technical hierarchies and avoid mixing incompatible abstraction levels"
        }
      ]
    },
    {
      "domain": "QUERY_RESPONSE",
      "domain_description": "Teaches directional knowledge gain where answers provide functional value to queries, but queries provide minimal value to answers",
      "batch_allocation": 500,
      
      "information_types": [
        {
          "type_id": "how_to_queries",
          "type_description": "Procedural questions where answers provide actionable steps that directly address the query",
          "batch_count": 150,
          
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Directional knowledge gain - answers satisfy information needs established by queries",
            "structure": "how_to_question → actionable_answer → detailed_explanation",
            "example": "How do I improve my credit score? → Pay bills on time and reduce credit utilization → These actions demonstrate financial responsibility to lenders",
            "why_asymmetric": "The answer provides functional value for the question; the question without the answer provides no actionable information",
            "real_world_application": "FAQ systems, knowledge bases, tutorial platforms, customer support, search engines"
          },
          
          "symmetric_pattern": {
            "structure": "question_quality ↔ answer_usefulness (mutual improvement)",
            "example": "Specific questions yield targeted solutions ↔ Detailed answers encourage more precise follow-up questions",
            "why_symmetric": "Question specificity improves answer quality, and comprehensive answers enable better questioning"
          },
          
          "hard_negative_strategy": {
            "description": "Questions and answers from different procedural domains with no relevance",
            "examples": ["How do I bake bread? ↔ Water the plants weekly", "How do I change a tire? ↔ Install the software from the app store"],
            "why_negative": "Both are Q&A but the answer doesn't address the question - no directional gain"
          },
          
          "variation_parameters": {
            "task_domain": {
              "values": ["personal_finance", "home_improvement", "cooking", "technology", "health"],
              "why_this_varies": "Different domains require different procedural knowledge and step structures"
            },
            "complexity": {
              "values": ["simple", "moderate", "complex"],
              "why_this_varies": "Complexity affects the detail needed in the answer to provide functional value"
            },
            "user_expertise": {
              "values": ["beginner", "intermediate", "advanced"],
              "why_this_varies": "Expertise level changes what explanatory depth the answer must provide"
            },
            "constraint_type": {
              "values": ["time", "budget", "resources", "skills"],
              "why_this_varies": "Constraints modify what counts as a useful answer to the how-to question"
            },
            "outcome_specificity": {
              "values": ["general_goal", "specific_target", "optimization"],
              "why_this_varies": "Specificity determines how targeted the answer must be"
            }
          },
          
          "combination_space": 300,
          "notes": "Ensure answers provide genuinely actionable steps, not just general advice"
        },
        {
          "type_id": "why_queries",
          "type_description": "Explanatory questions where answers provide causal or mechanistic understanding",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Directional knowledge gain - explanations satisfy understanding needs posed by why-questions",
            "structure": "why_question → explanatory_answer → supporting_detail",
            "example": "Why do plants need sunlight? → Sunlight powers photosynthesis → Chlorophyll absorbs light energy to convert CO2 and water into glucose",
            "why_asymmetric": "The explanation provides understanding for the question; the question alone provides no explanatory insight",
            "real_world_application": "Educational content, scientific communication, troubleshooting guides, curiosity-driven search"
          },
          
          "symmetric_pattern": {
            "structure": "explanation_depth ↔ comprehension_level (mutual calibration)",
            "example": "Detailed explanations build deeper understanding ↔ Strong understanding enables asking more sophisticated why-questions",
            "why_symmetric": "Explanation quality improves comprehension, and comprehension depth enables better questions"
          },
          
          "hard_negative_strategy": {
            "description": "Why-questions paired with unrelated explanations from different domains",
            "examples": ["Why do batteries die? ↔ Earthquakes occur due to tectonic shifts", "Why is the sky blue? ↔ Markets fluctuate based on supply and demand"],
            "why_negative": "Both are explanatory but the answer doesn't address the question's causal inquiry"
          },
          
          "variation_parameters": {
            "explanation_domain": {
              "values": ["natural_science", "technology", "social_phenomena", "economics", "human_behavior"],
              "why_this_varies": "Domains have different types of causal mechanisms and explanatory frameworks"
            },
            "causal_depth": {
              "values": ["immediate_cause", "mechanism", "fundamental_principle"],
              "why_this_varies": "Depth determines how far the explanation must go to provide functional value"
            },
            "audience_background": {
              "values": ["general_public", "educated_non_expert", "domain_expert"],
              "why_this_varies": "Background affects what level of explanation provides value vs. being redundant"
            },
            "phenomenon_type": {
              "values": ["observable", "abstract", "counterintuitive", "everyday"],
              "why_this_varies": "Phenomenon type changes what explanatory approach is most valuable"
            }
          },
          
          "combination_space": 240,
          "notes": "Match explanation depth to the implicit sophistication level of the why-question"
        },
        {
          "type_id": "what_queries",
          "type_description": "Definitional or factual questions where answers provide identifying information",
          "batch_count": 175,
          
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Directional knowledge gain - definitions and facts satisfy information needs of what-questions",
            "structure": "what_question → definitional_answer → contextual_elaboration",
            "example": "What is blockchain? → A distributed ledger technology → It ensures transaction transparency and immutability through cryptographic hashing",
            "why_asymmetric": "The answer identifies and explains what was asked; the question alone provides no identifying information",
            "real_world_application": "Glossaries, encyclopedias, search queries, onboarding materials, reference systems"
          },
          
          "symmetric_pattern": {
            "structure": "term_clarity ↔ concept_accessibility (mutual facilitation)",
            "example": "Clear definitions enable concept application ↔ Practical use reinforces definitional understanding",
            "why_symmetric": "Definitions make concepts usable, and usage deepens definitional grasp"
          },
          
          "hard_negative_strategy": {
            "description": "What-questions paired with definitions of unrelated concepts",
            "examples": ["What is machine learning? ↔ Photosynthesis is how plants create energy", "What is inflation? ↔ Democracy is a system of government"],
            "why_negative": "Both are definitional but the answer defines something other than what was asked"
          },
          
          "variation_parameters": {
            "concept_domain": {
              "values": ["technology", "science", "business", "politics", "culture"],
              "why_this_varies": "Domains have different definitional styles and contexts"
            },
            "concept_familiarity": {
              "values": ["technical_jargon", "emerging_term", "common_concept", "specialized"],
              "why_this_varies": "Familiarity determines how much context the definition must provide"
            },
            "definition_style": {
              "values": ["formal", "functional", "analogical", "example_based"],
              "why_this_varies": "Style affects how the answer provides value to different query contexts"
            },
            "use_case": {
              "values": ["academic", "practical", "conversational", "professional"],
              "why_this_varies": "Use case determines what level of precision and elaboration adds value"
            },
            "abstraction_level": {
              "values": ["concrete", "intermediate", "abstract"],
              "why_this_varies": "Abstraction affects what kind of elaboration is needed beyond the core definition"
            }
          },
          
          "combination_space": 300,
          "notes": "Ensure definitions are accurate and elaborations genuinely add functional understanding"
        }
      ]
    }
  ],
  
  "validation": {
    "total_batches": 3000,
    "total_domains": 6,
    "total_information_types": 20,
    "asymmetry_type_distribution": {
      "TEMPORAL": 500,
      "CAUSAL": 500,
      "EPISTEMIC": 500,
      "INTERACTIONAL": 500,
      "SEMANTIC": 500,
      "QUERY-RESPONSE": 500
    },
    "batch_distribution": {
      "asymmetric_focused": 1800,
      "symmetric_focused": 900,
      "balanced": 300
    }
  },
  
  "coverage_rationale": {
    "asymmetric_patterns": "All 6 linguistic asymmetry types are equally represented with exactly 500 batches each, ensuring comprehensive coverage of directional information flow patterns grounded in linguistic theory: TEMPORAL (iconicity), CAUSAL (explanation-result), EPISTEMIC (given-new), INTERACTIONAL (adjacency pairs), SEMANTIC (entailment), and QUERY-RESPONSE (directional knowledge gain)",
    "symmetric_patterns": [
      "Mutual causal relationships (feedback loops)",
      "Bidirectional explanation (property-application, concept-practice)",
      "Reciprocal reinforcement (habit-benefit, norm-relationship)",
      "Complementary understanding (question-answer quality, definition-usage)",
      "Mutual determination (technical capability-problem fit, material property-application)"
    ],
    "hard_negative_types": [
      "Same domain, different contexts (no functional dependency)",
      "Parallel hierarchies (no entailment relationship)",
      "Independent facts (shared keywords, zero value transfer)",
      "Mismatched Q&A (question-answer domain mismatch)",
      "Non-sequential procedures (unrelated steps from same activity domain)"
    ],
    "why_complete": "This curriculum systematically teaches directional information gain by grounding each pattern in established linguistic principles. The equal distribution of 500 batches across all 6 asymmetry types ensures the model learns to distinguish: (1) temporal iconicity where clause order mirrors reality, (2) causal chains where effects depend on understanding causes, (3) epistemic flow from known to new information, (4) interactional obligations in adjacency pairs, (5) semantic entailment in hierarchies, and (6) query-response directionality. With 20 diverse information types across 6 domains, rich variation parameters creating unique combinations, and carefully designed symmetric patterns and hard negatives, the curriculum provides comprehensive training data for learning when and why information flows directionally versus bidirectionally."
  }
}
