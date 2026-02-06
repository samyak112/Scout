TOPICS = {
  "curriculum": [
    {
      "domain": "PROCEDURAL_TASKS",
      "domain_description": "Sequential actions where order creates functional value - strong temporal and causal asymmetry",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "recipe_execution",
          "type_description": "Cooking steps where temporal sequence determines outcome",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - cooking steps mirror actual sequence of physical actions",
            "structure": "preparation_step → cooking_action → result_verification",
            "example": "Preheat oven to 350°F → Place dough on baking sheet → Bake until golden brown, about 15 minutes",
            "why_asymmetric": "Steps must occur in physical time order; reversing breaks procedural logic and causes failure",
            "real_world_application": "Recipes, assembly instructions, procedural documentation"
          },
          "symmetric_pattern": {
            "structure": "complementary_technique ↔ alternative_technique (different methods achieving same goal)",
            "example": "Whisk egg whites until stiff peaks form ↔ Use stand mixer on high for 3-4 minutes",
            "why_symmetric": "Both provide actionable methods; each elaborates on the other's approach"
          },
          "hard_negative_strategy": {
            "description": "Cooking facts that share ingredients/tools but provide no procedural value",
            "examples": ["Butter contains 80% fat", "Ovens were invented in 1490"],
            "why_negative": "Domain-relevant facts that don't advance the cooking procedure"
          },
          "variation_parameters": {
            "dish_type": {
              "values": ["baking", "sautéing", "grilling", "boiling", "roasting"],
              "why_this_varies": "Different cooking methods have fundamentally different temporal sequences"
            },
            "complexity_level": {
              "values": ["single_step", "multi_component", "advanced_technique", "restaurant_quality"],
              "why_this_varies": "Complexity changes the number and dependency structure of steps"
            },
            "cuisine_tradition": {
              "values": ["french", "italian", "asian", "mexican", "american"],
              "why_this_varies": "Different traditions have unique technique sequences and ingredient preparations"
            },
            "temperature_dependency": {
              "values": ["precise_temp_critical", "range_acceptable", "room_temp", "chilled"],
              "why_this_varies": "Temperature requirements create different temporal constraints"
            }
          },
          "combination_space": 400,
          "notes": "Sample evenly across complexity levels to ensure temporal dependency variety"
        },
        {
          "type_id": "assembly_instructions",
          "type_description": "Physical construction where component order determines structural integrity",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - assembly sequence mirrors physical construction reality",
            "structure": "foundation_component → connecting_component → securing_action",
            "example": "Attach metal frame to base plate → Slide wooden panel into frame slots → Tighten corner screws clockwise until snug",
            "why_asymmetric": "Later steps physically depend on earlier completion; reverse order is impossible",
            "real_world_application": "Furniture assembly, device setup, construction manuals"
          },
          "symmetric_pattern": {
            "structure": "tool_option_A ↔ tool_option_B (interchangeable tools for same step)",
            "example": "Use Phillips screwdriver for cross-head screws ↔ Power drill with PH2 bit works faster",
            "why_symmetric": "Both explain tool selection; each helps understand the other's trade-offs"
          },
          "hard_negative_strategy": {
            "description": "Component specifications that don't guide assembly sequence",
            "examples": ["Frame is powder-coated steel", "Panel dimensions: 24x36 inches"],
            "why_negative": "Material facts relevant to domain but useless for step execution"
          },
          "variation_parameters": {
            "product_category": {
              "values": ["furniture", "electronics", "toys", "shelving", "machinery"],
              "why_this_varies": "Different products have unique structural dependencies"
            },
            "fastener_type": {
              "values": ["screws", "bolts", "snap_fit", "adhesive", "welding"],
              "why_this_varies": "Different fastening methods create different temporal sequences"
            },
            "component_count": {
              "values": ["simple_3_parts", "moderate_8_parts", "complex_15_parts"],
              "why_this_varies": "More components create more potential dependency orderings"
            },
            "tool_requirement": {
              "values": ["hand_tools_only", "power_tools_optional", "specialized_tools_required"],
              "why_this_varies": "Tool availability affects viable assembly sequences"
            }
          },
          "combination_space": 180,
          "notes": "Ensure variation in dependency depth (linear vs branching assembly trees)"
        },
        {
          "type_id": "repair_procedures",
          "type_description": "Diagnostic and fix sequences where causal understanding drives action",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Cause must precede effect - diagnosis enables targeted solution",
            "structure": "symptom_observation → root_cause_identification → corrective_action",
            "example": "Faucet drips constantly → Worn rubber washer in valve seat → Replace washer with 1/2-inch neoprene washer",
            "why_asymmetric": "Solution makes sense only after cause; symptom alone doesn't enable action",
            "real_world_application": "Home repair, automotive troubleshooting, appliance fixes"
          },
          "symmetric_pattern": {
            "structure": "diagnostic_method_A ↔ diagnostic_method_B (alternative ways to identify cause)",
            "example": "Check for water pooling under sink ↔ Run water and observe valve stem for leaks",
            "why_symmetric": "Both diagnostic approaches inform each other; provide complementary evidence"
          },
          "hard_negative_strategy": {
            "description": "Related maintenance facts that don't solve the current problem",
            "examples": ["Faucets should be cleaned monthly", "Chrome finish resists corrosion"],
            "why_negative": "General maintenance advice that doesn't address specific failure"
          },
          "variation_parameters": {
            "system_type": {
              "values": ["plumbing", "electrical", "hvac", "appliance", "structural"],
              "why_this_varies": "Different systems have different failure modes and causal chains"
            },
            "failure_severity": {
              "values": ["minor_annoyance", "functionality_impaired", "safety_hazard", "complete_failure"],
              "why_this_varies": "Severity changes urgency and acceptable diagnostic shortcuts"
            },
            "skill_level_required": {
              "values": ["beginner_diy", "intermediate_homeowner", "experienced_handyman", "professional_only"],
              "why_this_varies": "Complexity affects diagnostic depth and solution approach"
            },
            "diagnostic_accessibility": {
              "values": ["visible_inspection", "requires_disassembly", "needs_testing_equipment"],
              "why_this_varies": "Access difficulty changes the causal reasoning path"
            }
          },
          "combination_space": 240,
          "notes": "Balance simple cause-effect with multi-step causal chains"
        },
        {
          "type_id": "emergency_response",
          "type_description": "Critical procedures where temporal order prevents harm escalation",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - response steps mirror time-critical physical reality",
            "structure": "immediate_safety_action → stabilization_action → follow_up_action",
            "example": "Turn off gas valve at meter → Open windows for ventilation → Call gas company from outside the building",
            "why_asymmetric": "Safety requires specific order; reversing creates danger or wastes critical time",
            "real_world_application": "First aid, emergency procedures, safety protocols"
          },
          "symmetric_pattern": {
            "structure": "warning_sign_A ↔ warning_sign_B (correlated indicators of same emergency)",
            "example": "Strong sulfur odor indicates gas leak ↔ Hissing sound near gas lines indicates leak",
            "why_symmetric": "Both signs help recognize emergency; each validates the other"
          },
          "hard_negative_strategy": {
            "description": "Safety facts that don't guide immediate emergency response",
            "examples": ["Natural gas is odorless; mercaptan is added for detection", "Gas explosions cause 15 deaths annually"],
            "why_negative": "Educational context that doesn't help in time-critical situations"
          },
          "variation_parameters": {
            "emergency_type": {
              "values": ["fire", "gas_leak", "electrical", "choking", "bleeding", "poisoning"],
              "why_this_varies": "Different emergencies have completely different response sequences"
            },
            "environment": {
              "values": ["home", "workplace", "vehicle", "public_space", "outdoor"],
              "why_this_varies": "Environment changes available resources and priority actions"
            },
            "victim_status": {
              "values": ["conscious_mobile", "conscious_immobile", "unconscious_breathing", "not_breathing"],
              "why_this_varies": "Victim state determines which actions are possible and prioritized"
            }
          },
          "combination_space": 216,
          "notes": "Emphasize time-criticality to strengthen temporal asymmetry signal"
        }
      ]
    },
    {
      "domain": "TROUBLESHOOTING_TECHNICAL",
      "domain_description": "Problem-diagnosis-solution chains with strong causal asymmetry",
      "batch_allocation": 450,
      "information_types": [
        {
          "type_id": "software_debugging",
          "type_description": "Code errors where understanding cause enables targeted fixes",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Cause-effect - root cause must be understood before solution makes sense",
            "structure": "error_manifestation → underlying_cause → code_fix",
            "example": "API returns 500 errors intermittently → Database connection pool exhausted under load → Increase pool size from 10 to 50 and add connection timeout",
            "why_asymmetric": "Fix only makes sense after diagnosis; error alone doesn't reveal what to change",
            "real_world_application": "Software debugging, log analysis, performance optimization"
          },
          "symmetric_pattern": {
            "structure": "debugging_technique_A ↔ debugging_technique_B (complementary diagnostic methods)",
            "example": "Add logging statements to trace execution flow ↔ Use debugger breakpoints to inspect state",
            "why_symmetric": "Both techniques aid diagnosis; each illuminates strengths of the other"
          },
          "hard_negative_strategy": {
            "description": "Code architecture facts that don't solve the specific error",
            "examples": ["API uses Express.js framework", "Database is PostgreSQL 14"],
            "why_negative": "Tech stack information relevant to domain but useless for this specific bug"
          },
          "variation_parameters": {
            "error_category": {
              "values": ["performance", "crash", "data_corruption", "security", "integration"],
              "why_this_varies": "Different error types have different diagnostic and solution patterns"
            },
            "system_component": {
              "values": ["frontend", "backend_api", "database", "cache", "message_queue", "auth"],
              "why_this_varies": "Component determines relevant diagnostic tools and fix locations"
            },
            "trigger_condition": {
              "values": ["always_fails", "intermittent", "load_dependent", "data_dependent", "timing_race"],
              "why_this_varies": "Trigger patterns require different causal reasoning approaches"
            },
            "investigation_depth": {
              "values": ["surface_symptom", "immediate_cause", "root_cause", "systemic_issue"],
              "why_this_varies": "Depth changes the causal chain length and solution scope"
            }
          },
          "combination_space": 240,
          "notes": "Include multi-hop causal chains for complex scenarios"
        },
        {
          "type_id": "network_diagnostics",
          "type_description": "Connectivity issues where layer-by-layer diagnosis reveals cause",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Causal chain - each diagnostic step reveals deeper cause",
            "structure": "connectivity_symptom → diagnostic_finding → resolution_action",
            "example": "Cannot reach website at example.com → DNS lookup fails; /etc/resolv.conf points to wrong nameserver → Update nameserver to 8.8.8.8 in resolv.conf",
            "why_asymmetric": "Resolution requires knowing what's broken; symptom doesn't indicate fix location",
            "real_world_application": "Network administration, IT support, DevOps troubleshooting"
          },
          "symmetric_pattern": {
            "structure": "diagnostic_tool_A ↔ diagnostic_tool_B (tools revealing same layer's status)",
            "example": "Use ping to test IP connectivity ↔ Use traceroute to identify routing path",
            "why_symmetric": "Both diagnose network layer; results complement each other's findings"
          },
          "hard_negative_strategy": {
            "description": "Network architecture facts that don't diagnose current problem",
            "examples": ["Network uses VLAN segmentation", "Firewall is Cisco ASA 5500"],
            "why_negative": "Infrastructure details that don't reveal this specific failure point"
          },
          "variation_parameters": {
            "osi_layer": {
              "values": ["physical_layer", "data_link", "network_layer", "transport_layer", "application_layer"],
              "why_this_varies": "Layer determines diagnostic approach and solution type"
            },
            "failure_scope": {
              "values": ["single_host", "subnet", "entire_network", "internet_gateway", "specific_service"],
              "why_this_varies": "Scope changes diagnostic strategy and likely causes"
            },
            "protocol_involved": {
              "values": ["dns", "dhcp", "tcp", "http", "ssl_tls"],
              "why_this_varies": "Protocol determines relevant diagnostic commands and config files"
            },
            "environment_type": {
              "values": ["home_network", "enterprise_lan", "cloud_vpc", "hybrid_network"],
              "why_this_varies": "Environment affects available diagnostic tools and fix permissions"
            }
          },
          "combination_space": 200,
          "notes": "Vary causal depth from single-cause to multi-layer failures"
        },
        {
          "type_id": "hardware_failure_diagnosis",
          "type_description": "Physical component failures requiring cause identification before replacement",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Diagnostic causation - symptoms lead to component identification",
            "structure": "device_malfunction → failed_component_identified → replacement_procedure",
            "example": "Laptop won't power on → Power supply unit outputs 0V; internal fuse blown → Replace PSU with 65W 19V adapter matching original specs",
            "why_asymmetric": "Knowing what failed enables targeted replacement; symptom alone could be multiple causes",
            "real_world_application": "Electronics repair, computer maintenance, appliance servicing"
          },
          "symmetric_pattern": {
            "structure": "test_method_A ↔ test_method_B (alternative ways to confirm component failure)",
            "example": "Use multimeter to test PSU voltage output ↔ Swap PSU with known-good unit to verify",
            "why_symmetric": "Both confirm diagnosis; each method validates the other's conclusion"
          },
          "hard_negative_strategy": {
            "description": "Hardware specifications that don't identify failed component",
            "examples": ["Laptop has Intel Core i5 processor", "Device uses lithium-ion battery"],
            "why_negative": "Specs relevant to device but don't diagnose which part failed"
          },
          "variation_parameters": {
            "device_category": {
              "values": ["computer", "smartphone", "printer", "gaming_console", "networking_equipment"],
              "why_this_varies": "Device type determines component types and failure modes"
            },
            "failure_mode": {
              "values": ["no_power", "intermittent_operation", "performance_degraded", "physical_damage"],
              "why_this_varies": "Failure type changes diagnostic approach and likely components"
            },
            "diagnostic_equipment": {
              "values": ["visual_inspection", "multimeter_testing", "diagnostic_software", "component_substitution"],
              "why_this_varies": "Available tools determine how cause is identified"
            },
            "repair_complexity": {
              "values": ["user_replaceable", "requires_disassembly", "soldering_needed", "professional_only"],
              "why_this_varies": "Complexity affects whether diagnosis leads to user action or referral"
            }
          },
          "combination_space": 192,
          "notes": "Include cases where multiple symptoms point to single cause"
        }
      ]
    },
    {
      "domain": "KNOWLEDGE_EXPLANATION",
      "domain_description": "Teaching new concepts by anchoring to known information - epistemic asymmetry",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "technical_concept_teaching",
          "type_description": "Explaining complex ideas by building from familiar foundations",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given→New - anchor familiar concept before introducing novel information",
            "structure": "familiar_anchor → new_concept → technical_elaboration",
            "example": "You know arrays store data in sequential memory → Hash tables store data using computed key positions → They use hash function modulo table size to map keys to indices",
            "why_asymmetric": "New concept needs familiar foundation; starting with technical detail loses audience",
            "real_world_application": "Technical documentation, educational content, onboarding materials"
          },
          "symmetric_pattern": {
            "structure": "concept_aspect_A ↔ concept_aspect_B (complementary facets of same concept)",
            "example": "Hash tables offer O(1) average lookup time ↔ Hash tables trade memory for speed with load factor management",
            "why_symmetric": "Both illuminate trade-offs; each property helps understand the other"
          },
          "hard_negative_strategy": {
            "description": "Related technical facts that don't build understanding from current foundation",
            "examples": ["Hash tables were invented in 1953", "Python dict uses hash tables internally"],
            "why_negative": "Historical or implementation trivia that doesn't teach the concept"
          },
          "variation_parameters": {
            "knowledge_domain": {
              "values": ["algorithms", "systems_design", "networking", "databases", "security"],
              "why_this_varies": "Different domains have different familiar anchors and concept structures"
            },
            "audience_level": {
              "values": ["beginner_programmer", "intermediate_developer", "advanced_engineer", "domain_expert"],
              "why_this_varies": "Audience determines what counts as 'familiar' vs 'new' information"
            },
            "explanation_approach": {
              "values": ["analogy_based", "contrast_with_alternative", "build_from_simple_case", "show_evolution"],
              "why_this_varies": "Approach changes the epistemic structure of given→new flow"
            },
            "abstraction_level": {
              "values": ["concrete_implementation", "conceptual_model", "mathematical_theory", "practical_pattern"],
              "why_this_varies": "Abstraction affects how new information relates to anchor"
            }
          },
          "combination_space": 240,
          "notes": "Ensure variation in what constitutes 'given' knowledge across examples"
        },
        {
          "type_id": "scientific_principle_explanation",
          "type_description": "Teaching scientific concepts from observable phenomena to theory",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given→New - start with observable experience, build to principle",
            "structure": "common_observation → underlying_mechanism → theoretical_principle",
            "example": "Ice floats on water → Water molecules form crystalline structure when frozen, increasing volume → This hydrogen bonding anomaly makes water less dense as solid than liquid",
            "why_asymmetric": "Abstract principle makes sense after observable anchor; reversing loses intuition",
            "real_world_application": "Science education, popular science writing, explanatory journalism"
          },
          "symmetric_pattern": {
            "structure": "evidence_type_A ↔ evidence_type_B (different evidence supporting same principle)",
            "example": "Ice expansion cracks rocks in freeze-thaw cycles ↔ Frozen water pipes burst from pressure buildup",
            "why_symmetric": "Both demonstrate same principle; each example reinforces the other"
          },
          "hard_negative_strategy": {
            "description": "Related science facts that don't explain the principle being taught",
            "examples": ["Water covers 71% of Earth's surface", "Ice has been found on Mars"],
            "why_negative": "Topically related but doesn't build epistemic understanding"
          },
          "variation_parameters": {
            "science_field": {
              "values": ["physics", "chemistry", "biology", "earth_science", "astronomy"],
              "why_this_varies": "Field determines types of observations and explanatory frameworks"
            },
            "phenomenon_scale": {
              "values": ["everyday_observable", "requires_instruments", "microscopic", "cosmic"],
              "why_this_varies": "Scale changes what serves as accessible 'given' information"
            },
            "explanation_depth": {
              "values": ["descriptive_pattern", "mechanistic_how", "theoretical_why", "mathematical_model"],
              "why_this_varies": "Depth determines how far new information extends from anchor"
            },
            "real_world_connection": {
              "values": ["common_experience", "industrial_application", "natural_phenomenon", "technological_use"],
              "why_this_varies": "Connection type affects familiarity of the anchor point"
            }
          },
          "combination_space": 192,
          "notes": "Vary the gap between given and new information"
        },
        {
          "type_id": "business_concept_education",
          "type_description": "Teaching business frameworks by connecting to familiar contexts",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given→New - relate abstract business concept to concrete experience",
            "structure": "relatable_scenario → business_framework → strategic_application",
            "example": "You've chosen restaurants based on reviews and convenience → This is evaluating switching costs and network effects → Businesses use these same factors to analyze competitive moats",
            "why_asymmetric": "Framework makes sense after concrete grounding; abstract term first is opaque",
            "real_world_application": "Business education, management training, strategy consulting"
          },
          "symmetric_pattern": {
            "structure": "framework_component_A ↔ framework_component_B (interacting elements)",
            "example": "High switching costs retain customers longer ↔ Network effects increase value for all users",
            "why_symmetric": "Both create competitive advantage; each mechanism amplifies the other"
          },
          "hard_negative_strategy": {
            "description": "Business jargon or facts that don't teach the framework",
            "examples": ["Porter introduced Five Forces in 1979", "Most startups use freemium models"],
            "why_negative": "Business trivia that doesn't build conceptual understanding"
          },
          "variation_parameters": {
            "business_area": {
              "values": ["strategy", "marketing", "operations", "finance", "organizational_behavior"],
              "why_this_varies": "Area determines relevant frameworks and anchor experiences"
            },
            "framework_complexity": {
              "values": ["single_concept", "two_factor_model", "multi_component_framework", "integrated_system"],
              "why_this_varies": "Complexity changes how much new information builds on given"
            },
            "industry_context": {
              "values": ["consumer_tech", "b2b_services", "manufacturing", "retail", "financial_services"],
              "why_this_varies": "Industry affects which concrete examples serve as anchors"
            },
            "application_level": {
              "values": ["individual_decision", "team_tactic", "company_strategy", "market_analysis"],
              "why_this_varies": "Level determines scale of new information being introduced"
            }
          },
          "combination_space": 192,
          "notes": "Ensure anchors are genuinely familiar across diverse backgrounds"
        },
        {
          "type_id": "historical_context_building",
          "type_description": "Teaching history by connecting events to familiar narratives",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given→New - anchor to known history before introducing new events",
            "structure": "familiar_historical_event → new_related_event → causal_connection",
            "example": "You know the Cold War involved US-Soviet tensions → The Berlin Airlift was a 1948 crisis when Soviets blocked West Berlin → This event crystallized the policy of containment that defined the next 40 years",
            "why_asymmetric": "New event makes sense within known context; isolated fact lacks meaning",
            "real_world_application": "History education, documentary narratives, museum exhibits"
          },
          "symmetric_pattern": {
            "structure": "perspective_A ↔ perspective_B (different viewpoints on same event)",
            "example": "Western powers saw airlift as defending freedom ↔ Soviet Union viewed it as provocative interference in their sphere",
            "why_symmetric": "Both perspectives illuminate motivations; each clarifies the other's reasoning"
          },
          "hard_negative_strategy": {
            "description": "Historical facts that don't connect to the narrative being built",
            "examples": ["Berlin's population was 3.3 million in 1948", "Airlift used C-47 aircraft"],
            "why_negative": "Factual details that don't build epistemic understanding of significance"
          },
          "variation_parameters": {
            "historical_period": {
              "values": ["ancient", "medieval", "early_modern", "19th_century", "20th_century", "contemporary"],
              "why_this_varies": "Period determines what events can serve as known anchors"
            },
            "geographic_scope": {
              "values": ["local_regional", "national", "continental", "global"],
              "why_this_varies": "Scope affects which contexts are familiar vs new"
            },
            "narrative_type": {
              "values": ["political_history", "social_movement", "technological_change", "cultural_shift", "economic_development"],
              "why_this_varies": "Narrative type changes the framework for connecting events"
            },
            "connection_strength": {
              "values": ["direct_causation", "parallel_development", "contrasting_approach", "long_term_influence"],
              "why_this_varies": "Connection type affects epistemic relationship between given and new"
            }
          },
          "combination_space": 216,
          "notes": "Vary familiarity assumptions to test epistemic anchoring"
        }
      ]
    },
    {
      "domain": "CONVERSATIONAL_DIALOGUE",
      "domain_description": "Interactive exchanges with adjacency pair structure - interactional asymmetry",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "technical_qa_forums",
          "type_description": "Question-answer pairs where question creates expectation for response",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Adjacency pairs - question creates obligation for answer",
            "structure": "specific_question → direct_answer → implementation_detail",
            "example": "How do I prevent SQL injection in Node.js? → Use parameterized queries with prepared statements → Example: db.query('SELECT * FROM users WHERE id = ?', [userId])",
            "why_asymmetric": "Answer addresses question; question doesn't help someone implementing answer",
            "real_world_application": "Stack Overflow, support forums, documentation FAQs"
          },
          "symmetric_pattern": {
            "structure": "clarifying_question ↔ clarifying_answer (back-and-forth refinement)",
            "example": "Are you using PostgreSQL or MySQL? ↔ I'm using PostgreSQL 13 with pg library",
            "why_symmetric": "Both refine context; each response enables more specific help"
          },
          "hard_negative_strategy": {
            "description": "Related technical information that doesn't answer the question",
            "examples": ["SQL injection is in OWASP Top 10", "Parameterized queries were introduced in 1990s"],
            "why_negative": "Background information that doesn't fulfill answer obligation"
          },
          "variation_parameters": {
            "question_type": {
              "values": ["how_to", "why_does", "what_is_best", "troubleshooting", "comparison"],
              "why_this_varies": "Question type determines appropriate answer structure"
            },
            "technical_domain": {
              "values": ["web_development", "data_science", "mobile_apps", "devops", "system_design"],
              "why_this_varies": "Domain changes the knowledge required and answer format"
            },
            "specificity_level": {
              "values": ["general_approach", "specific_tool", "code_example", "complete_solution"],
              "why_this_varies": "Specificity affects what constitutes adequate answer"
            },
            "asker_expertise": {
              "values": ["complete_beginner", "some_background", "experienced_different_stack", "expert_edge_case"],
              "why_this_varies": "Expertise level changes what answer detail is needed"
            }
          },
          "combination_space": 192,
          "notes": "Include multi-turn exchanges to test extended adjacency structure"
        },
        {
          "type_id": "customer_support_interactions",
          "type_description": "Service requests and responses following interactional norms",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Request-response pairs - request creates expectation for fulfillment",
            "structure": "customer_request → support_response → confirmation_action",
            "example": "I need to cancel my subscription → I can help with that. Can you confirm your account email? → Once confirmed, I'll process cancellation effective immediately",
            "why_asymmetric": "Response addresses request; request doesn't help execute the action",
            "real_world_application": "Customer service chats, help desk tickets, support calls"
          },
          "symmetric_pattern": {
            "structure": "information_exchange_A ↔ information_exchange_B (mutual information gathering)",
            "example": "What's your order number? ↔ It's #12345, placed on January 15th",
            "why_symmetric": "Both pieces needed for resolution; each enables the other's usefulness"
          },
          "hard_negative_strategy": {
            "description": "Company policies that don't address the specific request",
            "examples": ["We value customer satisfaction", "Our platform has 99.9% uptime"],
            "why_negative": "Generic statements that don't fulfill interactional obligation"
          },
          "variation_parameters": {
            "request_category": {
              "values": ["account_modification", "billing_issue", "technical_problem", "product_inquiry", "complaint"],
              "why_this_varies": "Category determines expected response structure"
            },
            "urgency_level": {
              "values": ["routine_inquiry", "time_sensitive", "service_disrupted", "critical_blocker"],
              "why_this_varies": "Urgency changes response obligations and priorities"
            },
            "resolution_path": {
              "values": ["immediate_resolution", "requires_investigation", "needs_escalation", "external_dependency"],
              "why_this_varies": "Path affects how interactional obligation is fulfilled"
            },
            "customer_emotion": {
              "values": ["neutral_transactional", "frustrated", "confused", "appreciative"],
              "why_this_varies": "Emotion affects interactional dynamics and response approach"
            }
          },
          "combination_space": 192,
          "notes": "Vary how requests are framed to test obligation recognition"
        },
        {
          "type_id": "advice_seeking_responses",
          "type_description": "Seeking and providing guidance following conversational norms",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Advice-seeking creates expectation for recommendation",
            "structure": "situation_description → advice_recommendation → rationale",
            "example": "I have $10k to invest and I'm 25 years old → Consider low-cost index funds for long-term growth → At your age, you can ride out market volatility for decades of compound growth",
            "why_asymmetric": "Advice responds to situation; situation doesn't help implement advice",
            "real_world_application": "Reddit advice forums, mentorship conversations, consulting"
          },
          "symmetric_pattern": {
            "structure": "context_detail_A ↔ context_detail_B (both refine the situation)",
            "example": "I'm risk-averse and need emergency access ↔ I have stable income and no debt",
            "why_symmetric": "Both constraints shape advice; each detail refines the other's relevance"
          },
          "hard_negative_strategy": {
            "description": "General wisdom that doesn't address specific situation",
            "examples": ["Investing carries risk", "Past performance doesn't guarantee future returns"],
            "why_negative": "Generic disclaimers that don't fulfill advice obligation"
          },
          "variation_parameters": {
            "advice_domain": {
              "values": ["career", "relationships", "finance", "health", "education", "technology"],
              "why_this_varies": "Domain determines relevant advice frameworks"
            },
            "situation_complexity": {
              "values": ["straightforward_decision", "multiple_constraints", "conflicting_priorities", "uncertain_factors"],
              "why_this_varies": "Complexity affects what constitutes adequate advice response"
            },
            "advice_style": {
              "values": ["directive_prescription", "options_presentation", "framework_guidance", "question_reflection"],
              "why_this_varies": "Style changes how interactional obligation is satisfied"
            },
            "follow_up_depth": {
              "values": ["initial_response_only", "one_clarification", "extended_dialogue"],
              "why_this_varies": "Depth tests multi-turn interactional structure"
            }
          },
          "combination_space": 216,
          "notes": "Balance directive vs exploratory advice patterns"
        },
        {
          "type_id": "scheduling_coordination",
          "type_description": "Proposal-response pairs for arranging meetings and events",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Proposal creates expectation for acceptance/counter-proposal",
            "structure": "scheduling_proposal → response_to_proposal → confirmation_detail",
            "example": "Can we meet Tuesday at 2pm to discuss the project? → Tuesday works, but I'm free after 3pm → Perfect, I'll send a 3pm calendar invite for Conference Room B",
            "why_asymmetric": "Response addresses proposal; proposal doesn't contain logistics details",
            "real_world_application": "Email coordination, calendar scheduling, meeting planning"
          },
          "symmetric_pattern": {
            "structure": "constraint_A ↔ constraint_B (both parties share availability)",
            "example": "I'm available Monday through Wednesday ↔ I can do Tuesday or Wednesday afternoons",
            "why_symmetric": "Both constraints needed for resolution; each narrows viable options"
          },
          "hard_negative_strategy": {
            "description": "Meeting context that doesn't address scheduling logistics",
            "examples": ["This project is high priority", "We should invite the design team"],
            "why_negative": "Topically related but doesn't fulfill proposal-response obligation"
          },
          "variation_parameters": {
            "coordination_complexity": {
              "values": ["two_person_simple", "small_group", "large_meeting", "multi_party_dependencies"],
              "why_this_varies": "Complexity changes the interactional structure of proposals"
            },
            "urgency_timeframe": {
              "values": ["same_day", "this_week", "next_few_weeks", "flexible_timing"],
              "why_this_varies": "Timeframe affects what constitutes adequate response"
            },
            "constraint_type": {
              "values": ["time_availability", "location_preference", "attendee_requirements", "resource_booking"],
              "why_this_varies": "Constraint type changes what proposals and responses must address"
            },
            "formality_level": {
              "values": ["casual_colleague", "professional_formal", "client_facing", "executive_level"],
              "why_this_varies": "Formality affects interactional norms and response expectations"
            }
          },
          "combination_space": 192,
          "notes": "Include counter-proposals to test extended adjacency sequences"
        }
      ]
    },
    {
      "domain": "CLASSIFICATION_TAXONOMY",
      "domain_description": "Categorization with semantic entailment - specific implies general but not reverse",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "error_categorization",
          "type_description": "Specific errors entailing general categories with system implications",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Entailment - specific instance implies general category, not vice versa",
            "structure": "specific_error_code → general_error_category → system_impact",
            "example": "ECONNREFUSED on port 5432 → Database connection failure → All data-dependent endpoints will return 503 errors",
            "why_asymmetric": "Specific error entails general failure; general category doesn't specify which error",
            "real_world_application": "Error handling systems, logging infrastructure, monitoring dashboards"
          },
          "symmetric_pattern": {
            "structure": "error_indicator_A ↔ error_indicator_B (correlated symptoms of same root issue)",
            "example": "Connection timeout after 30 seconds ↔ No TCP handshake completion logged",
            "why_symmetric": "Both indicate same underlying issue; each validates the other's diagnosis"
          },
          "hard_negative_strategy": {
            "description": "Error information that doesn't reveal category or impact",
            "examples": ["Error occurred at 14:23:45 UTC", "PostgreSQL version is 13.2"],
            "why_negative": "Contextual details that don't enable semantic categorization"
          },
          "variation_parameters": {
            "error_domain": {
              "values": ["network_errors", "database_errors", "file_system_errors", "authentication_errors", "resource_errors"],
              "why_this_varies": "Domain determines the taxonomy structure and entailment relationships"
            },
            "specificity_level": {
              "values": ["precise_error_code", "component_level", "subsystem_level", "system_wide"],
              "why_this_varies": "Specificity determines strength of entailment relationship"
            },
            "impact_scope": {
              "values": ["single_operation", "user_session", "service_component", "entire_system"],
              "why_this_varies": "Scope changes what the general category implies"
            },
            "diagnostic_certainty": {
              "values": ["definitive_failure", "likely_cause", "possible_contributor", "correlated_event"],
              "why_this_varies": "Certainty affects semantic relationship strength"
            }
          },
          "combination_space": 192,
          "notes": "Emphasize one-way entailment from specific to general"
        },
        {
          "type_id": "product_taxonomy",
          "type_description": "Specific products belonging to general categories with attribute inheritance",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Hyponymy - specific item inherits properties of general category",
            "structure": "specific_product → product_category → category_attribute",
            "example": "MacBook Air M2 → Laptop computer → Requires charging, portable computing device",
            "why_asymmetric": "Specific product IS-A laptop; laptop category doesn't specify which product",
            "real_world_application": "E-commerce categorization, inventory systems, search filtering"
          },
          "symmetric_pattern": {
            "structure": "product_feature_A ↔ product_feature_B (complementary attributes)",
            "example": "Has 13-inch Retina display ↔ Weighs 2.7 pounds for portability",
            "why_symmetric": "Both features describe the product; each attribute complements the other"
          },
          "hard_negative_strategy": {
            "description": "Product facts that don't establish categorical relationships",
            "examples": ["Released in June 2022", "Available in four colors"],
            "why_negative": "Product details that don't reveal taxonomic position or inherited attributes"
          },
          "variation_parameters": {
            "product_domain": {
              "values": ["electronics", "clothing", "furniture", "food_items", "tools"],
              "why_this_varies": "Domain determines relevant taxonomic hierarchies"
            },
            "taxonomy_depth": {
              "values": ["broad_category", "subcategory", "specific_type", "exact_model"],
              "why_this_varies": "Depth changes the entailment chain length"
            },
            "attribute_type": {
              "values": ["functional_property", "physical_characteristic", "usage_context", "technical_spec"],
              "why_this_varies": "Attribute type affects what's inherited from category"
            },
            "categorization_basis": {
              "values": ["function_based", "material_based", "use_case_based", "form_factor_based"],
              "why_this_varies": "Basis determines which attributes are category-level vs instance-level"
            }
          },
          "combination_space": 192,
          "notes": "Vary taxonomy depth to test multi-level entailment"
        },
        {
          "type_id": "medical_diagnosis_hierarchy",
          "type_description": "Specific conditions as instances of general diagnostic categories",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Taxonomic entailment - specific diagnosis implies general condition class",
            "structure": "specific_diagnosis → condition_category → treatment_class",
            "example": "Type 2 diabetes mellitus → Metabolic disorder → Requires lifestyle modification and possible medication management",
            "why_asymmetric": "Specific diagnosis entails metabolic disorder; category doesn't specify diabetes",
            "real_world_application": "Medical coding, clinical decision support, health records"
          },
          "symmetric_pattern": {
            "structure": "symptom_A ↔ symptom_B (co-occurring indicators of condition)",
            "example": "Elevated fasting blood glucose levels ↔ Increased thirst and urination",
            "why_symmetric": "Both symptoms indicate condition; each finding supports the other"
          },
          "hard_negative_strategy": {
            "description": "Medical facts that don't establish diagnostic hierarchy",
            "examples": ["Affects 10% of US adults", "First described in ancient Egypt"],
            "why_negative": "Epidemiological or historical info that doesn't reveal categorical relationship"
          },
          "variation_parameters": {
            "medical_system": {
              "values": ["endocrine", "cardiovascular", "respiratory", "neurological", "musculoskeletal"],
              "why_this_varies": "Body system determines diagnostic taxonomy structure"
            },
            "condition_severity": {
              "values": ["acute", "chronic", "progressive", "reversible"],
              "why_this_varies": "Severity affects categorization and treatment implications"
            },
            "diagnostic_certainty": {
              "values": ["confirmed_diagnosis", "probable", "differential", "rule_out"],
              "why_this_varies": "Certainty affects strength of category membership"
            },
            "classification_system": {
              "values": ["icd_symptom_based", "pathophysiology_based", "anatomical", "etiological"],
              "why_this_varies": "System determines which taxonomic relationships exist"
            }
          },
          "combination_space": 192,
          "notes": "Ensure examples show genuine medical entailment, not just association"
        },
        {
          "type_id": "legal_case_precedent",
          "type_description": "Specific rulings as instances of general legal principles",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Legal entailment - specific case exemplifies general principle",
            "structure": "specific_case_ruling → general_legal_principle → application_scope",
            "example": "Miranda v. Arizona (1966) → Fifth Amendment protection against self-incrimination → Police must inform suspects of rights before custodial interrogation",
            "why_asymmetric": "Specific case establishes principle; principle doesn't uniquely identify case",
            "real_world_application": "Legal research, case law databases, judicial reasoning"
          },
          "symmetric_pattern": {
            "structure": "case_element_A ↔ case_element_B (mutually reinforcing precedents)",
            "example": "Right to remain silent ↔ Right to attorney before questioning",
            "why_symmetric": "Both rights work together; each clarifies scope of the other"
          },
          "hard_negative_strategy": {
            "description": "Legal facts that don't establish principle-case relationship",
            "examples": ["Case heard by Warren Court", "5-4 decision split"],
            "why_negative": "Procedural details that don't reveal doctrinal categorization"
          },
          "variation_parameters": {
            "legal_domain": {
              "values": ["constitutional_law", "contract_law", "tort_law", "criminal_law", "administrative_law"],
              "why_this_varies": "Domain determines relevant doctrinal hierarchies"
            },
            "precedent_strength": {
              "values": ["binding_precedent", "persuasive_authority", "distinguishable", "overruled"],
              "why_this_varies": "Strength affects entailment relationship to principle"
            },
            "principle_abstraction": {
              "values": ["narrow_holding", "intermediate_rule", "broad_doctrine", "fundamental_right"],
              "why_this_varies": "Abstraction level changes taxonomic position"
            },
            "jurisdiction_scope": {
              "values": ["federal_supreme", "circuit_level", "state_supreme", "trial_court"],
              "why_this_varies": "Jurisdiction affects which principles cases can establish"
            }
          },
          "combination_space": 192,
          "notes": "Show clear semantic entailment from case to principle"
        }
      ]
    },
    {
      "domain": "NARRATIVE_DISCOURSE",
      "domain_description": "Story and explanation structures with multiple asymmetry types in natural flow",
      "batch_allocation": 150,
      "information_types": [
        {
          "type_id": "story_chronology",
          "type_description": "Narrative events where temporal sequence creates coherent story",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Narrative iconicity - story order reflects chronological event sequence",
            "structure": "initial_event → consequent_event → outcome",
            "example": "She submitted her resume on Monday → The hiring manager called her on Wednesday → She started the new job two weeks later",
            "why_asymmetric": "Events follow causal time order; reversing breaks narrative coherence",
            "real_world_application": "News articles, case studies, historical accounts, storytelling"
          },
          "symmetric_pattern": {
            "structure": "parallel_event_A ↔ parallel_event_B (simultaneous developments)",
            "example": "She prepared for the interview by researching the company ↔ She practiced answering common interview questions",
            "why_symmetric": "Both preparations happened concurrently; each activity complements the other"
          },
          "hard_negative_strategy": {
            "description": "Background details that don't advance narrative timeline",
            "examples": ["The company was founded in 2010", "She had been job hunting for three months"],
            "why_negative": "Contextual information that doesn't create temporal progression"
          },
          "variation_parameters": {
            "narrative_genre": {
              "values": ["personal_journey", "business_event", "historical_account", "investigative_story", "process_narrative"],
              "why_this_varies": "Genre determines typical event sequences and causal structures"
            },
            "time_scale": {
              "values": ["hours", "days", "weeks", "months", "years"],
              "why_this_varies": "Scale affects granularity of temporal relationships"
            },
            "event_density": {
              "values": ["sparse_key_events", "moderate_detail", "dense_play_by_play"],
              "why_this_varies": "Density changes how tightly events are causally linked"
            },
            "narrative_perspective": {
              "values": ["first_person", "third_person_limited", "third_person_omniscient", "journalistic_objective"],
              "why_this_varies": "Perspective affects what temporal information is available"
            },
            "causal_complexity": {
              "values": ["linear_sequence", "branching_outcomes", "converging_threads", "cyclical_pattern"],
              "why_this_varies": "Complexity determines temporal-causal structure"
            }
          },
          "combination_space": 300,
          "notes": "Vary event causality from simple sequence to complex temporal structures"
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
    "asymmetric_patterns": "All 5 linguistic asymmetry types equally represented with 600 batches each. TEMPORAL (600): recipe_execution (150), assembly_instructions (150), emergency_response (150), story_chronology (150). CAUSAL (600): repair_procedures (150), software_debugging (150), network_diagnostics (150), hardware_failure_diagnosis (150). EPISTEMIC (600): technical_concept_teaching (150), scientific_principle_explanation (150), business_concept_education (150), historical_context_building (150). INTERACTIONAL (600): technical_qa_forums (150), customer_support_interactions (150), advice_seeking_responses (150), scheduling_coordination (150). SEMANTIC (600): error_categorization (150), product_taxonomy (150), medical_diagnosis_hierarchy (150), legal_case_precedent (150).",
    "symmetric_patterns": [
      "Complementary techniques (alternative methods for same goal)",
      "Mutual diagnostic methods (different ways to confirm same finding)",
      "Concept facets (complementary properties of same idea)",
      "Information exchanges (back-and-forth context building)",
      "Correlated indicators (co-occurring evidence)",
      "Parallel events (simultaneous developments)",
      "Complementary attributes (mutually reinforcing features)"
    ],
    "hard_negative_types": [
      "Domain facts without procedural value",
      "Specifications without assembly guidance",
      "Maintenance advice not solving specific problem",
      "Safety context not guiding emergency action",
      "Tech stack details not fixing specific bug",
      "Architecture facts not diagnosing problem",
      "Component specs not identifying failure",
      "Historical trivia not teaching concept",
      "Science facts not explaining principle",
      "Business jargon not building framework",
      "Historical facts not connecting narrative",
      "Background info not fulfilling answer obligation",
      "Generic statements not addressing request",
      "General wisdom not addressing situation",
      "Meeting context not addressing logistics",
      "Error context not enabling categorization",
      "Product details not revealing taxonomy",
      "Epidemiological info not showing hierarchy",
      "Procedural details not establishing principle",
      "Background details not advancing timeline"
    ],
    "why_complete": "This curriculum comprehensively teaches directional information gain by grounding training in the 5 fundamental linguistic asymmetry types that govern how information flows in natural language. Each asymmetry type receives exactly 600 batches (equal 20% distribution) across diverse domains. TEMPORAL asymmetry (iconicity) is taught through procedures, assembly, emergencies, and narratives. CAUSAL asymmetry (explanation) through troubleshooting and repair across software, network, and hardware. EPISTEMIC asymmetry (given→new) through teaching in technical, scientific, business, and historical contexts. INTERACTIONAL asymmetry (adjacency pairs) through Q&A, support, advice, and coordination dialogues. SEMANTIC asymmetry (entailment) through error, product, medical, and legal taxonomies. The curriculum balances concrete domains (cooking, repairs) with abstract ones (concepts, principles), professional contexts (technical, medical, legal) with everyday ones (conversation, advice, stories). Hard negatives systematically test keyword overlap without functional value across all patterns. 3000 batches ensure the model learns that information gain is directional, context-dependent, and rooted in how language actually structures meaning transfer."
  }
}
