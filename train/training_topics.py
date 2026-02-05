Topics = {
  "curriculum": [
    {
      "domain": "TROUBLESHOOTING",
      "domain_description": "Teaches directional gain in problem-solution relationships where solutions add high value to problems but problems add low value to solutions",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "tech_debugging",
          "type_description": "Software errors and their fixes - tests asymmetric problem→solution flow",
          "batch_count": 200,
          "asymmetric_pattern": {
            "description": "error_message → diagnostic_step → solution_code",
            "example": "AttributeError: 'NoneType' object has no attribute 'get' → Check if variable was initialized → Add null check before method call",
            "why_asymmetric": "Solution adds actionable value to error; error doesn't help someone already implementing the solution"
          },
          "symmetric_pattern": {
            "description": "root_cause ↔ prevention_strategy",
            "example": "Race condition in thread pool ↔ Use thread-safe queue with locks",
            "why_symmetric": "Understanding cause helps choose prevention; prevention validates cause hypothesis"
          },
          "hard_negative_strategy": {
            "description": "Same technology/framework mentioned but wrong error type or unrelated feature",
            "examples": [
              "Django authentication error paired with Django ORM optimization tip",
              "React useState error paired with React routing configuration"
            ],
            "why_negative": "Shares keywords but solution doesn't address the actual problem type"
          },
          "variation_parameters": {
            "language": {
              "values": ["python", "javascript", "java", "rust", "sql"],
              "why_this_varies": "Different type systems, error reporting, and debugging approaches"
            },
            "error_category": {
              "values": ["type_error", "null_reference", "async_timing", "import_resolution"],
              "why_this_varies": "Each requires fundamentally different diagnostic reasoning"
            },
            "context": {
              "values": ["web_backend", "data_pipeline", "frontend_ui", "cli_tool"],
              "why_this_varies": "Different constraints and debugging tools available"
            },
            "complexity": {
              "values": ["syntax_level", "logic_level", "architecture_level"],
              "why_this_varies": "Solution detail and abstraction level differs significantly"
            }
          },
          "combination_space": 240,
          "notes": "Sample evenly across languages to avoid bias"
        },
        {
          "type_id": "home_repair",
          "type_description": "Household problems and fixes - tests practical troubleshooting across physical systems",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "symptom → diagnosis → repair_action",
            "example": "Water pools under sink → Check P-trap seal → Replace worn rubber gasket",
            "why_asymmetric": "Repair instruction adds value to symptom; symptom doesn't help someone already repairing"
          },
          "symmetric_pattern": {
            "description": "maintenance_task ↔ failure_it_prevents",
            "example": "Clean HVAC filter monthly ↔ Prevents compressor overheating",
            "why_symmetric": "Maintenance makes sense given failure; failure justifies maintenance effort"
          },
          "hard_negative_strategy": {
            "description": "Same room/appliance but completely different system",
            "examples": [
              "Leaky faucet paired with electrical outlet not working",
              "Refrigerator ice maker issue paired with refrigerator light bulb replacement"
            ],
            "why_negative": "Same appliance keywords but functionally independent systems"
          },
          "variation_parameters": {
            "system": {
              "values": ["plumbing", "electrical", "hvac", "appliance", "structural"],
              "why_this_varies": "Completely different tools, skills, and safety considerations"
            },
            "urgency": {
              "values": ["emergency", "needs_attention", "preventive"],
              "why_this_varies": "Changes solution approach and detail level"
            },
            "skill_required": {
              "values": ["diy_simple", "diy_moderate", "call_professional"],
              "why_this_varies": "Affects solution specificity and safety warnings"
            },
            "location": {
              "values": ["kitchen", "bathroom", "basement", "exterior"],
              "why_this_varies": "Different environmental factors and system types"
            }
          },
          "combination_space": 240,
          "notes": "Include safety warnings in emergency scenarios"
        },
        {
          "type_id": "medical_symptoms",
          "type_description": "Symptoms and their clinical responses - tests diagnostic reasoning flows",
          "batch_count": 125,
          "asymmetric_pattern": {
            "description": "presenting_symptom → clinical_assessment → intervention",
            "example": "Persistent dry cough over 3 weeks → Check for postnasal drip and GERD → Elevate bed head, avoid late meals",
            "why_asymmetric": "Intervention addresses symptom; symptom doesn't guide someone already treating"
          },
          "symmetric_pattern": {
            "description": "risk_factor ↔ screening_recommendation",
            "example": "Family history of colon cancer ↔ Colonoscopy starting age 40",
            "why_symmetric": "Risk factor justifies screening; screening targets risk factor"
          },
          "hard_negative_strategy": {
            "description": "Same body system but unrelated conditions",
            "examples": [
              "Chest pain from heartburn paired with advice for asthma management",
              "Knee arthritis paired with ankle sprain treatment"
            ],
            "why_negative": "Same anatomical area but different pathophysiology"
          },
          "variation_parameters": {
            "body_system": {
              "values": ["respiratory", "digestive", "musculoskeletal", "cardiovascular", "neurological"],
              "why_this_varies": "Different diagnostic approaches and treatment modalities"
            },
            "severity": {
              "values": ["seek_emergency", "schedule_appointment", "self_care"],
              "why_this_varies": "Dramatically changes appropriate response"
            },
            "chronicity": {
              "values": ["acute_new", "chronic_stable", "chronic_worsening"],
              "why_this_varies": "Affects urgency and investigation depth"
            },
            "age_group": {
              "values": ["pediatric", "adult", "geriatric"],
              "why_this_varies": "Different differential diagnoses and treatment considerations"
            }
          },
          "combination_space": 180,
          "notes": "Always include appropriate medical disclaimers"
        },
        {
          "type_id": "device_troubleshooting",
          "type_description": "Consumer electronics issues and solutions",
          "batch_count": 125,
          "asymmetric_pattern": {
            "description": "malfunction → diagnostic_test → fix_procedure",
            "example": "Laptop won't charge → Check LED indicator and try different outlet → Replace AC adapter",
            "why_asymmetric": "Fix procedure resolves malfunction; malfunction doesn't help someone already fixing"
          },
          "symmetric_pattern": {
            "description": "feature_limitation ↔ workaround_method",
            "example": "Smart TV doesn't support VPN apps ↔ Configure VPN on router level",
            "why_symmetric": "Limitation explains why workaround needed; workaround addresses limitation"
          },
          "hard_negative_strategy": {
            "description": "Same device brand/model but different component issue",
            "examples": [
              "iPhone battery drain paired with iPhone speaker distortion fix",
              "Printer paper jam paired with printer WiFi connection troubleshooting"
            ],
            "why_negative": "Same device but independent hardware/software systems"
          },
          "variation_parameters": {
            "device_category": {
              "values": ["smartphone", "laptop", "printer", "smart_home", "audio"],
              "why_this_varies": "Different interfaces, components, and user expectations"
            },
            "issue_type": {
              "values": ["hardware_failure", "software_bug", "connectivity", "performance"],
              "why_this_varies": "Requires different diagnostic and solution approaches"
            },
            "warranty_status": {
              "values": ["under_warranty", "out_of_warranty", "diy_only"],
              "why_this_varies": "Changes whether to suggest repair vs replacement vs DIY"
            }
          },
          "combination_space": 180,
          "notes": "Consider warranty implications in solutions"
        }
      ]
    },
    {
      "domain": "PROCEDURAL_KNOWLEDGE",
      "domain_description": "Teaches directional gain in goal-method relationships where methods add value to goals but goals don't add value to methods already being executed",
      "batch_allocation": 500,
      "information_types": [
        {
          "type_id": "cooking_techniques",
          "type_description": "Culinary goals and execution methods",
          "batch_count": 175,
          "asymmetric_pattern": {
            "description": "desired_outcome → technique → execution_detail",
            "example": "Achieve crispy chicken skin → Use dry brine overnight → Pat dry, refrigerate uncovered 8 hours",
            "why_asymmetric": "Execution detail enables outcome; outcome doesn't help someone already executing"
          },
          "symmetric_pattern": {
            "description": "ingredient_property ↔ cooking_method",
            "example": "High-starch potatoes ↔ Best for fluffy mashed potatoes",
            "why_symmetric": "Property explains why method works; method leverages property"
          },
          "hard_negative_strategy": {
            "description": "Same cuisine or ingredient but different dish goals",
            "examples": [
              "Making pasta al dente paired with making pasta dough from scratch",
              "Grilling steak paired with making beef stock"
            ],
            "why_negative": "Same ingredient domain but functionally unrelated preparations"
          },
          "variation_parameters": {
            "cuisine": {
              "values": ["italian", "chinese", "french", "indian", "mexican"],
              "why_this_varies": "Different flavor principles and techniques"
            },
            "cooking_method": {
              "values": ["sauté", "roast", "braise", "steam", "grill"],
              "why_this_varies": "Fundamentally different heat transfer and timing"
            },
            "main_ingredient": {
              "values": ["poultry", "seafood", "vegetables", "grains", "beef"],
              "why_this_varies": "Different textures, cooking times, and doneness indicators"
            },
            "skill_level": {
              "values": ["beginner", "intermediate", "advanced"],
              "why_this_varies": "Changes technique complexity and assumed knowledge"
            },
            "goal_type": {
              "values": ["texture", "flavor", "presentation", "timing"],
              "why_this_varies": "Different success criteria require different techniques"
            }
          },
          "combination_space": 300,
          "notes": "Include food safety where relevant"
        },
        {
          "type_id": "learning_strategies",
          "type_description": "Educational goals and study methods",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "learning_goal → study_strategy → implementation",
            "example": "Master organic chemistry reactions → Use mechanism mapping → Draw electron flow for each step daily",
            "why_asymmetric": "Implementation enables goal; goal doesn't help someone already implementing"
          },
          "symmetric_pattern": {
            "description": "cognitive_principle ↔ technique_application",
            "example": "Spaced repetition strengthens memory ↔ Review flashcards at increasing intervals",
            "why_symmetric": "Principle explains why technique works; technique applies principle"
          },
          "hard_negative_strategy": {
            "description": "Same subject area but different skill being developed",
            "examples": [
              "Memorizing vocabulary paired with improving pronunciation",
              "Understanding calculus concepts paired with improving calculation speed"
            ],
            "why_negative": "Same subject but orthogonal skills requiring different approaches"
          },
          "variation_parameters": {
            "subject_domain": {
              "values": ["stem", "language", "humanities", "arts", "professional_skills"],
              "why_this_varies": "Different types of knowledge require different encoding strategies"
            },
            "learning_phase": {
              "values": ["initial_acquisition", "comprehension", "mastery", "retention"],
              "why_this_varies": "Different phases need different study approaches"
            },
            "resource_availability": {
              "values": ["self_study", "with_instructor", "peer_group", "online_course"],
              "why_this_varies": "Changes what methods are practical"
            },
            "time_constraint": {
              "values": ["intensive_weeks", "regular_semester", "long_term_years"],
              "why_this_varies": "Affects pacing and technique selection"
            }
          },
          "combination_space": 240,
          "notes": "Consider learning science research backing"
        },
        {
          "type_id": "project_planning",
          "type_description": "Project goals and execution workflows",
          "batch_count": 175,
          "asymmetric_pattern": {
            "description": "project_objective → planning_approach → execution_steps",
            "example": "Launch product in 6 months → Use agile sprints → 2-week iterations with daily standups",
            "why_asymmetric": "Execution steps achieve objective; objective doesn't guide someone mid-execution"
          },
          "symmetric_pattern": {
            "description": "constraint ↔ mitigation_strategy",
            "example": "Limited budget ↔ Prioritize MVP features only",
            "why_symmetric": "Constraint necessitates strategy; strategy addresses constraint"
          },
          "hard_negative_strategy": {
            "description": "Same project type but different phase or concern",
            "examples": [
              "User research methods paired with deployment infrastructure planning",
              "Team formation advice paired with post-launch metrics tracking"
            ],
            "why_negative": "Same project domain but non-overlapping lifecycle phases"
          },
          "variation_parameters": {
            "project_type": {
              "values": ["software_development", "marketing_campaign", "construction", "research_study", "event_planning"],
              "why_this_varies": "Different deliverables and success metrics"
            },
            "team_size": {
              "values": ["solo", "small_team_5", "medium_team_20", "large_team_50plus"],
              "why_this_varies": "Different coordination and communication needs"
            },
            "uncertainty_level": {
              "values": ["well_defined", "some_unknowns", "highly_exploratory"],
              "why_this_varies": "Affects planning approach and flexibility needed"
            },
            "timeline": {
              "values": ["sprint_weeks", "quarter_months", "annual_longterm"],
              "why_this_varies": "Changes planning granularity and checkpoints"
            }
          },
          "combination_space": 240,
          "notes": "Include risk management considerations"
        }
      ]
    },
    {
      "domain": "CONCEPTUAL_KNOWLEDGE",
      "domain_description": "Teaches symmetric information gain where abstract concepts and concrete examples mutually reinforce understanding",
      "batch_allocation": 450,
      "information_types": [
        {
          "type_id": "theory_examples",
          "type_description": "Abstract principles and concrete instantiations",
          "batch_count": 175,
          "asymmetric_pattern": {
            "description": "abstract_principle → application_context → concrete_implementation",
            "example": "Compound interest grows exponentially → Retirement savings → $500 monthly at 7% becomes $1.2M in 30 years",
            "why_asymmetric": "Implementation makes principle tangible; principle doesn't add value to someone already implementing"
          },
          "symmetric_pattern": {
            "description": "theory ↔ illustrative_example",
            "example": "Supply and demand determine price ↔ Concert ticket prices spike when popular artist announced",
            "why_symmetric": "Theory explains example; example demonstrates theory"
          },
          "hard_negative_strategy": {
            "description": "Same conceptual domain but unrelated principles",
            "examples": [
              "Marginal utility theory paired with example of comparative advantage",
              "Newton's first law paired with example of wave interference"
            ],
            "why_negative": "Same field but principle doesn't explain the example"
          },
          "variation_parameters": {
            "field": {
              "values": ["economics", "physics", "psychology", "biology", "mathematics"],
              "why_this_varies": "Different types of models and evidence"
            },
            "abstraction_level": {
              "values": ["fundamental_law", "derived_principle", "emergent_pattern"],
              "why_this_varies": "Changes how directly theory connects to examples"
            },
            "example_context": {
              "values": ["everyday_life", "historical_event", "thought_experiment", "lab_result"],
              "why_this_varies": "Different types of evidence and applicability"
            },
            "complexity": {
              "values": ["introductory", "intermediate", "advanced"],
              "why_this_varies": "Changes mathematical sophistication and prerequisite knowledge"
            },
            "domain_specificity": {
              "values": ["universal_principle", "domain_specific", "special_case"],
              "why_this_varies": "Affects generalizability of the relationship"
            }
          },
          "combination_space": 360,
          "notes": "Ensure examples genuinely illustrate stated principles"
        },
        {
          "type_id": "definitional_relationships",
          "type_description": "Technical terms and their formal definitions",
          "batch_count": 125,
          "asymmetric_pattern": {
            "description": "informal_understanding → formal_definition → rigorous_criterion",
            "example": "Function that 'doesn't jump' → Continuous function → For all ε>0 exists δ>0 such that |x-a|<δ implies |f(x)-f(a)|<ε",
            "why_asymmetric": "Rigor refines understanding; informal notion doesn't add precision to formal definition"
          },
          "symmetric_pattern": {
            "description": "technical_term ↔ defining_property",
            "example": "Prime number ↔ Divisible only by 1 and itself",
            "why_symmetric": "Term requires property; property defines term"
          },
          "hard_negative_strategy": {
            "description": "Same field but unrelated definitions",
            "examples": [
              "Definition of median paired with definition of variance",
              "Definition of mammal paired with definition of ecosystem"
            ],
            "why_negative": "Same domain vocabulary but independent concepts"
          },
          "variation_parameters": {
            "discipline": {
              "values": ["mathematics", "computer_science", "law", "medicine", "linguistics"],
              "why_this_varies": "Different standards of rigor and definition types"
            },
            "formality": {
              "values": ["colloquial", "technical", "axiomatic"],
              "why_this_varies": "Different precision levels and use cases"
            },
            "concept_type": {
              "values": ["object", "property", "relation", "operation"],
              "why_this_varies": "Different logical structures and definition patterns"
            }
          },
          "combination_space": 135,
          "notes": "Include both necessary and sufficient conditions where applicable"
        },
        {
          "type_id": "analogical_reasoning",
          "type_description": "Cross-domain analogies that transfer understanding",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "unfamiliar_concept → analogical_bridge → familiar_domain",
            "example": "Quantum superposition → Like coin spinning in air → Not heads or tails until observed",
            "why_asymmetric": "Analogy clarifies unfamiliar; familiar domain doesn't add to someone already understanding target"
          },
          "symmetric_pattern": {
            "description": "structural_similarity ↔ parallel_domains",
            "example": "Natural selection in biology ↔ Algorithm evolution in genetic programming",
            "why_symmetric": "Each domain illuminates mechanisms in the other"
          },
          "hard_negative_strategy": {
            "description": "Surface similarity without structural mapping",
            "examples": [
              "Atom structure paired with solar system (outdated analogy)",
              "Brain as computer paired with actual neural network architecture details"
            ],
            "why_negative": "Superficial resemblance but analogy breaks down functionally"
          },
          "variation_parameters": {
            "source_domain": {
              "values": ["physical_systems", "social_systems", "biological_systems", "computational_systems"],
              "why_this_varies": "Different types of mappable relationships"
            },
            "target_domain": {
              "values": ["abstract_math", "quantum_physics", "economics", "cognition"],
              "why_this_varies": "Different unfamiliar concepts needing explanation"
            },
            "mapping_quality": {
              "values": ["strong_isomorphism", "partial_mapping", "metaphorical"],
              "why_this_varies": "Affects pedagogical value and limitations"
            },
            "audience": {
              "values": ["lay_public", "students", "interdisciplinary_experts"],
              "why_this_varies": "Changes appropriate source domain familiarity"
            }
          },
          "combination_space": 256,
          "notes": "Note where analogies break down"
        }
      ]
    },
    {
      "domain": "CAUSAL_RELATIONSHIPS",
      "domain_description": "Teaches directional gain in cause-effect flows where effects explain causes but causes don't derive from effects",
      "batch_allocation": 400,
      "information_types": [
        {
          "type_id": "physical_causation",
          "type_description": "Physical mechanisms and their observable outcomes",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "mechanism → intermediate_process → observable_effect",
            "example": "Friction generates heat → Kinetic energy converts to thermal → Brake pads glow red when stopping",
            "why_asymmetric": "Effect demonstrates mechanism; mechanism doesn't follow from observing effect alone"
          },
          "symmetric_pattern": {
            "description": "physical_condition ↔ equilibrium_state",
            "example": "Pressure increases ↔ Boiling point rises",
            "why_symmetric": "Condition determines state; state implies condition"
          },
          "hard_negative_strategy": {
            "description": "Same physical domain but unrelated causal chains",
            "examples": [
              "Why ice floats paired with why magnets attract",
              "Thermal expansion explanation paired with sound wave propagation"
            ],
            "why_negative": "Same physics domain but independent mechanisms"
          },
          "variation_parameters": {
            "physics_domain": {
              "values": ["thermodynamics", "mechanics", "electromagnetism", "optics", "fluid_dynamics"],
              "why_this_varies": "Different fundamental forces and equations"
            },
            "scale": {
              "values": ["molecular", "everyday", "planetary", "cosmological"],
              "why_this_varies": "Different dominant effects at different scales"
            },
            "observability": {
              "values": ["directly_visible", "requires_instruments", "inferred_from_data"],
              "why_this_varies": "Changes how cause-effect is established"
            },
            "reversibility": {
              "values": ["reversible", "irreversible", "partially_reversible"],
              "why_this_varies": "Affects whether effect can be undone"
            }
          },
          "combination_space": 240,
          "notes": "Include energy conservation principles"
        },
        {
          "type_id": "behavioral_causation",
          "type_description": "Psychological/social causes and behavioral outcomes",
          "batch_count": 125,
          "asymmetric_pattern": {
            "description": "underlying_motivation → decision_process → observable_behavior",
            "example": "Loss aversion bias → Overweight risks vs benefits → Hold losing stocks too long",
            "why_asymmetric": "Behavior evidences motivation; motivation isn't deducible from behavior alone"
          },
          "symmetric_pattern": {
            "description": "social_norm ↔ compliance_behavior",
            "example": "Turn-taking in conversation ↔ People wait for pauses to speak",
            "why_symmetric": "Norm shapes behavior; behavior reinforces norm"
          },
          "hard_negative_strategy": {
            "description": "Same behavioral domain but unrelated mechanisms",
            "examples": [
              "Confirmation bias explanation paired with example of anchoring effect",
              "Groupthink dynamics paired with individual procrastination"
            ],
            "why_negative": "Same psychology domain but different causal mechanisms"
          },
          "variation_parameters": {
            "psych_mechanism": {
              "values": ["cognitive_bias", "motivation", "emotion", "social_influence", "habit"],
              "why_this_varies": "Different psychological drivers and interventions"
            },
            "context": {
              "values": ["individual_decision", "group_dynamics", "organizational", "societal"],
              "why_this_varies": "Different levels of analysis and factors"
            },
            "outcome_type": {
              "values": ["choice", "judgment", "action", "belief_formation"],
              "why_this_varies": "Different behavioral endpoints"
            },
            "evidence_strength": {
              "values": ["well_established", "emerging_research", "theoretical"],
              "why_this_varies": "Different levels of scientific consensus"
            }
          },
          "combination_space": 256,
          "notes": "Acknowledge individual differences in applicability"
        },
        {
          "type_id": "systemic_causation",
          "type_description": "Complex system dynamics and emergent outcomes",
          "batch_count": 125,
          "asymmetric_pattern": {
            "description": "system_structure → feedback_dynamics → emergent_behavior",
            "example": "Positive feedback in housing market → Prices rising attracts speculators → Bubble formation",
            "why_asymmetric": "Emergence follows from structure; structure isn't derivable from outcome alone"
          },
          "symmetric_pattern": {
            "description": "system_component ↔ network_effect",
            "example": "More users on platform ↔ Platform becomes more valuable",
            "why_symmetric": "Components create effect; effect reinforces components"
          },
          "hard_negative_strategy": {
            "description": "Same system type but different dynamics",
            "examples": [
              "Traffic congestion causes paired with traffic safety statistics",
              "Ecosystem predator-prey dynamics paired with nutrient cycling"
            ],
            "why_negative": "Same system but independent causal pathways"
          },
          "variation_parameters": {
            "system_type": {
              "values": ["economic", "ecological", "technological", "social", "biological"],
              "why_this_varies": "Different components and interaction rules"
            },
            "feedback_type": {
              "values": ["positive_reinforcing", "negative_balancing", "delayed", "nonlinear"],
              "why_this_varies": "Different stability and prediction characteristics"
            },
            "scale": {
              "values": ["micro_local", "meso_regional", "macro_global"],
              "why_this_varies": "Different relevant factors and timescales"
            },
            "predictability": {
              "values": ["deterministic", "stochastic", "chaotic"],
              "why_this_varies": "Different ability to forecast outcomes"
            }
          },
          "combination_space": 240,
          "notes": "Highlight feedback loops and non-obvious effects"
        }
      ]
    },
    {
      "domain": "CONVERSATIONAL_PRAGMATICS",
      "domain_description": "Teaches directional gain in dialogue where responses add value to questions but questions don't add value to responses",
      "batch_allocation": 350,
      "information_types": [
        {
          "type_id": "question_answering",
          "type_description": "Information requests and relevant responses",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "question → clarifying_context → informative_answer",
            "example": "What time does the store close? → During weekdays → 9 PM Monday-Friday, 10 PM weekends",
            "why_asymmetric": "Answer satisfies question; question doesn't help someone already knowing answer"
          },
          "symmetric_pattern": {
            "description": "question_constraint ↔ answer_qualification",
            "example": "Need gluten-free options? ↔ All items marked with GF symbol",
            "why_symmetric": "Constraint explains qualification; qualification addresses constraint"
          },
          "hard_negative_strategy": {
            "description": "Same topic domain but answer addresses different question",
            "examples": [
              "Store hours question paired with store location directions",
              "Product price question paired with product return policy"
            ],
            "why_negative": "Same business but answer doesn't address the actual question"
          },
          "variation_parameters": {
            "question_type": {
              "values": ["factual", "procedural", "recommendation", "comparison", "troubleshooting"],
              "why_this_varies": "Different answer structures and completeness criteria"
            },
            "domain": {
              "values": ["customer_service", "technical_support", "health_info", "directions", "scheduling"],
              "why_this_varies": "Different background knowledge assumed and precision needed"
            },
            "specificity": {
              "values": ["broad_general", "specific_constrained", "highly_personalized"],
              "why_this_varies": "Changes answer detail and context needed"
            },
            "urgency": {
              "values": ["time_sensitive", "planning_ahead", "casual_inquiry"],
              "why_this_varies": "Affects answer prioritization and detail"
            }
          },
          "combination_space": 240,
          "notes": "Ensure answers are complete and actionable"
        },
        {
          "type_id": "advice_seeking",
          "type_description": "Situation descriptions and actionable guidance",
          "batch_count": 125,
          "asymmetric_pattern": {
            "description": "situation → analysis → recommended_action",
            "example": "Job offer but hesitant about relocation → Weigh career growth vs personal ties → Request remote work hybrid option",
            "why_asymmetric": "Action addresses situation; situation doesn't guide someone already acting"
          },
          "symmetric_pattern": {
            "description": "constraint ↔ adapted_strategy",
            "example": "Limited time to exercise ↔ High-intensity 20-minute workouts",
            "why_symmetric": "Constraint necessitates adaptation; adaptation acknowledges constraint"
          },
          "hard_negative_strategy": {
            "description": "Same life domain but unrelated concern",
            "examples": [
              "Career decision advice paired with salary negotiation tactics",
              "Relationship conflict paired with dating profile tips"
            ],
            "why_negative": "Same general domain but advice doesn't address the specific situation"
          },
          "variation_parameters": {
            "life_domain": {
              "values": ["career", "relationships", "finance", "health", "education"],
              "why_this_varies": "Different values and decision factors"
            },
            "decision_type": {
              "values": ["binary_choice", "optimization", "conflict_resolution", "goal_setting"],
              "why_this_varies": "Different advice structures and frameworks"
            },
            "stakes": {
              "values": ["low_reversible", "moderate_significant", "high_irreversible"],
              "why_this_varies": "Changes risk tolerance and deliberation depth"
            },
            "information_state": {
              "values": ["well_informed", "some_unknowns", "highly_uncertain"],
              "why_this_varies": "Affects whether advice focuses on decision or information gathering"
            }
          },
          "combination_space": 240,
          "notes": "Acknowledge personal values in advice framing"
        },
        {
          "type_id": "clarification_dialogue",
          "type_description": "Ambiguous statements and disambiguating follow-ups",
          "batch_count": 75,
          "asymmetric_pattern": {
            "description": "ambiguous_statement → clarifying_question → specific_resolution",
            "example": "The meeting was moved → To earlier or later? → Moved to 2 PM from 4 PM",
            "why_asymmetric": "Resolution answers clarification; clarification doesn't help someone already resolved"
          },
          "symmetric_pattern": {
            "description": "vague_reference ↔ context_that_resolves",
            "example": "Send it to the client ↔ Which client - the Smith account?",
            "why_symmetric": "Vagueness prompts specification; specification resolves vagueness"
          },
          "hard_negative_strategy": {
            "description": "Same conversation topic but orthogonal ambiguity",
            "examples": [
              "Time ambiguity paired with location clarification",
              "Person reference ambiguity paired with document version clarification"
            ],
            "why_negative": "Same conversation but clarification addresses different ambiguity"
          },
          "variation_parameters": {
            "ambiguity_type": {
              "values": ["referential", "temporal", "quantitative", "modal", "scope"],
              "why_this_varies": "Different types of clarifying questions needed"
            },
            "context": {
              "values": ["work_coordination", "social_plans", "technical_specs", "instructions"],
              "why_this_varies": "Different stakes and precision requirements"
            },
            "resolution_method": {
              "values": ["binary_choice", "specification", "example", "definition"],
              "why_this_varies": "Different clarification strategies"
            }
          },
          "combination_space": 108,
          "notes": "Model realistic conversational repair patterns"
        }
      ]
    },
    {
      "domain": "OPTIMIZATION_AND_IMPROVEMENT",
      "domain_description": "Teaches directional gain where improvements add value to baseline states but baseline states don't add value to improvements",
      "batch_allocation": 350,
      "information_types": [
        {
          "type_id": "performance_optimization",
          "type_description": "Baseline performance and enhancement techniques",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "performance_metric → bottleneck_analysis → optimization_technique",
            "example": "Database queries slow → N+1 query problem identified → Implement eager loading",
            "why_asymmetric": "Optimization improves metric; metric doesn't guide someone already optimizing"
          },
          "symmetric_pattern": {
            "description": "resource_constraint ↔ efficiency_approach",
            "example": "Limited memory available ↔ Use streaming instead of loading full dataset",
            "why_symmetric": "Constraint necessitates efficiency; efficiency addresses constraint"
          },
          "hard_negative_strategy": {
            "description": "Same system but unrelated performance dimension",
            "examples": [
              "Speed optimization paired with security hardening",
              "Memory efficiency paired with user interface improvements"
            ],
            "why_negative": "Same system but optimization doesn't address stated metric"
          },
          "variation_parameters": {
            "system_type": {
              "values": ["web_application", "data_processing", "mobile_app", "algorithm", "infrastructure"],
              "why_this_varies": "Different performance bottlenecks and optimization techniques"
            },
            "metric": {
              "values": ["latency", "throughput", "resource_usage", "cost", "scalability"],
              "why_this_varies": "Different optimization targets and tradeoffs"
            },
            "optimization_approach": {
              "values": ["caching", "parallelization", "algorithm_improvement", "architecture_change"],
              "why_this_varies": "Different implementation complexity and gains"
            },
            "constraint": {
              "values": ["backwards_compatible", "no_new_dependencies", "zero_downtime", "budget_limited"],
              "why_this_varies": "Different viable optimization strategies"
            }
          },
          "combination_space": 256,
          "notes": "Include measurement before/after optimization"
        },
        {
          "type_id": "skill_improvement",
          "type_description": "Current skill level and advancement techniques",
          "batch_count": 100,
          "asymmetric_pattern": {
            "description": "skill_plateau → weakness_diagnosis → targeted_practice",
            "example": "Chess rating stuck at 1400 → Weak endgame knowledge → Study rook endgames 30 min daily",
            "why_asymmetric": "Practice advances skill; plateau doesn't guide someone already practicing"
          },
          "symmetric_pattern": {
            "description": "skill_component ↔ development_exercise",
            "example": "Finger independence in guitar ↔ Spider walking exercises",
            "why_symmetric": "Component explains exercise choice; exercise develops component"
          },
          "hard_negative_strategy": {
            "description": "Same skill domain but different sub-skill",
            "examples": [
              "Chess tactics improvement paired with chess opening theory study",
              "Guitar speed paired with guitar music theory knowledge"
            ],
            "why_negative": "Same overall skill but practice doesn't address stated weakness"
          },
          "variation_parameters": {
            "skill_domain": {
              "values": ["musical_instrument", "sport", "language", "craft", "intellectual_game"],
              "why_this_varies": "Different learning modalities and progression paths"
            },
            "current_level": {
              "values": ["beginner_fundamentals", "intermediate_consolidation", "advanced_refinement"],
              "why_this_varies": "Different appropriate practice methods and goals"
            },
            "limiting_factor": {
              "values": ["technical", "strategic", "physical", "mental"],
              "why_this_varies": "Different intervention approaches"
            },
            "practice_structure": {
              "values": ["deliberate_isolated", "integrated_application", "coached_feedback"],
              "why_this_varies": "Different learning effectiveness and accessibility"
            }
          },
          "combination_space": 240,
          "notes": "Include progression milestones"
        },
        {
          "type_id": "process_improvement",
          "type_description": "Current workflows and efficiency enhancements",
          "batch_count": 100,
          "asymmetric_pattern": {
            "description": "workflow_issue → root_cause → process_redesign",
            "example": "Email responses take too long → Frequent context switching → Batch process emails at set times",
            "why_asymmetric": "Redesign fixes issue; issue doesn't guide someone already redesigning"
          },
          "symmetric_pattern": {
            "description": "workflow_characteristic ↔ tool_solution",
            "example": "Repetitive data entry ↔ Use form automation with validation",
            "why_symmetric": "Characteristic justifies tool; tool addresses characteristic"
          },
          "hard_negative_strategy": {
            "description": "Same work domain but different process pain point",
            "examples": [
              "Time management improvement paired with communication clarity improvement",
              "Meeting efficiency paired with documentation organization"
            ],
            "why_negative": "Same workplace but improvement doesn't address stated issue"
          },
          "variation_parameters": {
            "work_context": {
              "values": ["individual_productivity", "team_collaboration", "customer_service", "manufacturing", "creative_workflow"],
              "why_this_varies": "Different process types and stakeholders"
            },
            "inefficiency_type": {
              "values": ["time_waste", "error_prone", "knowledge_loss", "coordination_overhead"],
              "why_this_varies": "Different improvement strategies"
            },
            "improvement_approach": {
              "values": ["automation", "standardization", "elimination", "reorganization"],
              "why_this_varies": "Different implementation effort and impact"
            },
            "adoption_challenge": {
              "values": ["individual_habit", "team_coordination", "system_integration", "cultural_change"],
              "why_this_varies": "Different change management needs"
            }
          },
          "combination_space": 240,
          "notes": "Consider change management in improvements"
        }
      ]
    },
    {
      "domain": "COMPARATIVE_EVALUATION",
      "domain_description": "Teaches symmetric and asymmetric patterns in comparisons, where evaluation criteria flow bidirectionally but recommendations flow unidirectionally",
      "batch_allocation": 350,
      "information_types": [
        {
          "type_id": "product_selection",
          "type_description": "Selection criteria and product recommendations",
          "batch_count": 150,
          "asymmetric_pattern": {
            "description": "requirements → evaluation → specific_recommendation",
            "example": "Need laptop for video editing → 32GB RAM, GPU priority → Recommend MacBook Pro M3 Max",
            "why_asymmetric": "Recommendation satisfies requirements; requirements don't derive from recommendation"
          },
          "symmetric_pattern": {
            "description": "product_feature ↔ use_case_fit",
            "example": "All-day battery life ↔ Ideal for field work without charging access",
            "why_symmetric": "Feature enables use case; use case necessitates feature"
          },
          "hard_negative_strategy": {
            "description": "Same product category but mismatched priorities",
            "examples": [
              "Budget laptop needs paired with gaming laptop recommendations",
              "Portability priority paired with desktop workstation specs"
            ],
            "why_negative": "Same category but recommendation doesn't match stated criteria"
          },
          "variation_parameters": {
            "product_category": {
              "values": ["electronics", "appliances", "vehicles", "software", "services"],
              "why_this_varies": "Different evaluation criteria and longevity"
            },
            "priority_dimension": {
              "values": ["performance", "budget", "portability", "durability", "ecosystem"],
              "why_this_varies": "Different tradeoffs and optimal choices"
            },
            "user_expertise": {
              "values": ["novice_needs_simple", "intermediate_wants_value", "expert_seeks_specific"],
              "why_this_varies": "Different feature importance and terminology"
            },
            "purchase_context": {
              "values": ["personal", "business", "gift", "educational"],
              "why_this_varies": "Different decision factors and constraints"
            }
          },
          "combination_space": 240,
          "notes": "Include clear decision rationale"
        },
        {
          "type_id": "tradeoff_analysis",
          "type_description": "Competing objectives and balanced solutions",
          "batch_count": 100,
          "asymmetric_pattern": {
            "description": "competing_goals → constraint_analysis → compromise_solution",
            "example": "Want fast delivery and low cost → Shipping speed vs price → Choose 3-day shipping at mid-tier cost",
            "why_asymmetric": "Solution balances goals; goals don't specify solution"
          },
          "symmetric_pattern": {
            "description": "advantage ↔ disadvantage",
            "example": "Remote work flexibility ↔ Reduced spontaneous collaboration",
            "why_symmetric": "Each aspect implies the other in the tradeoff"
          },
          "hard_negative_strategy": {
            "description": "Same decision domain but unrelated tradeoff dimensions",
            "examples": [
              "Speed vs cost tradeoff paired with quality vs quantity tradeoff",
              "Security vs convenience paired with customization vs simplicity"
            ],
            "why_negative": "Same domain but tradeoffs are independent dimensions"
          },
          "variation_parameters": {
            "decision_domain": {
              "values": ["business_strategy", "personal_lifestyle", "technical_architecture", "policy_design"],
              "why_this_varies": "Different stakeholders and reversibility"
            },
            "tradeoff_type": {
              "values": ["binary_choice", "spectrum_optimization", "multi_objective", "sequential_decision"],
              "why_this_varies": "Different decision frameworks applicable"
            },
            "information_quality": {
              "values": ["data_driven", "experience_based", "uncertain_estimate"],
              "why_this_varies": "Different confidence in tradeoff quantification"
            },
            "stakes": {
              "values": ["low_easily_reversible", "medium_commitment", "high_irreversible"],
              "why_this_varies": "Different acceptable risk levels"
            }
          },
          "combination_space": 240,
          "notes": "Acknowledge uncertainty in tradeoff estimates"
        },
        {
          "type_id": "alternative_comparison",
          "type_description": "Multiple options and distinguishing characteristics",
          "batch_count": 100,
          "asymmetric_pattern": {
            "description": "comparison_request → key_differentiators → selection_guidance",
            "example": "Python vs JavaScript for web backend → Async model and typing → Python for data-heavy, JS for real-time",
            "why_asymmetric": "Guidance uses differentiators; differentiators don't imply guidance"
          },
          "symmetric_pattern": {
            "description": "strength_of_option_A ↔ weakness_of_option_B",
            "example": "SQL's declarative queries ↔ NoSQL's rigid schema requirements",
            "why_symmetric": "Each highlights the contrast from both perspectives"
          },
          "hard_negative_strategy": {
            "description": "Comparison in same domain but orthogonal attributes",
            "examples": [
              "Performance comparison paired with community ecosystem comparison",
              "Learning curve comparison paired with enterprise support comparison"
            ],
            "why_negative": "Same alternatives but attributes don't address stated comparison"
          },
          "variation_parameters": {
            "comparison_domain": {
              "values": ["technology_stack", "service_provider", "methodology", "location", "career_path"],
              "why_this_varies": "Different comparison dimensions relevant"
            },
            "number_of_options": {
              "values": ["binary_two", "small_set_three_to_five", "large_set_many"],
              "why_this_varies": "Different comparison presentation strategies"
            },
            "comparison_basis": {
              "values": ["objective_metrics", "subjective_fit", "contextual_suitability"],
              "why_this_varies": "Different types of evidence and reasoning"
            },
            "decision_reversibility": {
              "values": ["easily_switched", "moderate_switching_cost", "locked_in"],
              "why_this_varies": "Different importance of getting it right initially"
            }
          },
          "combination_space": 240,
          "notes": "Avoid false dichotomies when multiple options viable"
        }
      ]
    }
  ],
  "validation": {
    "total_batches": 3000,
    "total_domains": 7,
    "total_information_types": 25,
    "batch_distribution": {
      "asymmetric_focused": 1800,
      "symmetric_focused": 900,
      "balanced": 300
    }
  },
  "coverage_rationale": {
    "asymmetric_patterns": [
      "Problem→Solution (troubleshooting)",
      "Goal→Method (procedural)",
      "Cause→Effect (causal)",
      "Question→Answer (conversational)",
      "Baseline→Improvement (optimization)",
      "Requirements→Recommendation (comparative)",
      "Ambiguous→Clarified (dialogue)",
      "Abstract→Concrete (conceptual)"
    ],
    "symmetric_patterns": [
      "Theory↔Example (conceptual)",
      "Definition↔Property (definitional)",
      "Constraint↔Mitigation (strategic)",
      "Feature↔UseCase (functional)",
      "Advantage↔Disadvantage (tradeoff)",
      "Cause↔Prevention (bidirectional)",
      "Norm↔Behavior (social)",
      "Component↔NetworkEffect (systemic)"
    ],
    "hard_negative_types": [
      "Same domain, different subsystem",
      "Same keywords, wrong relationship type",
      "Same context, orthogonal concern",
      "Surface similarity, no structural mapping",
      "Same entity, independent attributes",
      "Related field, unconnected principles",
      "Same lifecycle, different phase",
      "Shared vocabulary, distinct mechanisms"
    ],
    "why_complete": "This curriculum systematically covers the spectrum of directional information gain relationships. It balances concrete troubleshooting domains (where problem→solution asymmetry is clear) with abstract conceptual domains (where theory↔example symmetry is evident). The 3000 batches span practical scenarios (home repair, cooking, device troubleshooting), professional contexts (software debugging, project planning, medical diagnosis), theoretical understanding (physics, economics, psychology), and everyday communication (Q&A, advice, clarification). Each domain contributes unique patterns: troubleshooting teaches problem-solution asymmetry, procedural knowledge teaches goal-method flow, conceptual knowledge teaches mutual reinforcement, causation teaches mechanism-outcome directionality, conversation teaches request-response pragmatics, optimization teaches baseline-improvement gain, and comparison teaches both symmetric tradeoffs and asymmetric recommendations. The hard negatives systematically test that the model learns functional relevance rather than keyword matching, ensuring it distinguishes between topical similarity and actual information gain. The variation parameters create genuine diversity within each information type by varying functional dimensions (error types, skill levels, system scales, decision stakes) rather than superficial attributes, ensuring each batch provides distinct learning signal about when and how information adds directional value."
  }
}