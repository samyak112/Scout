TOPICS = {
  "curriculum": 
      [
    {
      "domain": "NARRATIVE_SEQUENCE",
      "domain_description": "Story, investigation, and event progression contexts where temporal ordering is the primary structure. Teaches TEMPORAL asymmetry through journalistic, investigative, and lifecycle narratives rather than task procedures. The key signal is that each sentence only makes sense given the prior one has been established as real.",
      "batch_allocation": 500,
      "information_types": [
        {
          "type_id": "crime_investigation_arc",
          "type_description": "Detective and forensic investigation sequences where each discovery narrows the possibility space established by the prior finding.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - investigative discoveries build sequentially. Each finding recontextualizes prior evidence and opens new questions answered in the next sentence.",
            "structure": "sentence_A (initial anomaly or crime scene observation) → sentence_B (investigative finding that explains or narrows A) → sentence_C (conclusion or arrest action enabled by B)",
            "example": "'The security footage showed the vault door closing at 2:47am, three hours before the morning shift discovered it empty.' → 'Forensic analysis of the door mechanism found tool marks consistent with a bypass device used on fewer than twelve known heists globally.' → 'Investigators cross-referenced all twelve prior cases and identified a suspect who had worked at two of the affected facilities.'",
            "why_asymmetric": "B is only meaningful given A established the specific anomaly being investigated. C is only actionable given B identified the rare tool type. Reversed: knowing the suspect was identified tells you nothing about what anomaly started the investigation.",
            "real_world_application": "True crime journalism, police procedural writing, forensic case documentation, investigative reporting"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (investigative technique) ↔ sentence_Y (the class of evidence that technique uniquely reveals)",
            "example": "'Luminol reacts with iron in hemoglobin to produce chemiluminescence even after thorough cleaning.' ↔ 'Blood traces that are invisible to the naked eye after surface cleaning can be mapped precisely using luminol under UV lighting.'",
            "why_symmetric": "X explains the chemistry; Y explains the forensic capability that chemistry creates. Each makes the other operationally meaningful for an investigator."
          },
          "hard_negative_strategy": {
            "description": "Two types: (1) CLOSE - same crime scene, same timeline, same location but provides administrative or statistical facts with zero investigative chain value; (2) DISTANT - unrelated forensic or legal domain fact.",
            "examples": [
              "CLOSE: 'The vault had been installed in 1998 and last serviced by the manufacturer eighteen months prior to the incident.' (same vault, zero investigation chain utility)",
              "CLOSE: 'Bank vault crimes account for approximately 0.3 percent of all reported financial crimes in the country annually.' (same crime type, zero chain value)",
              "DISTANT: 'Chain of custody documentation must accompany all physical evidence from collection through trial presentation.'"
            ],
            "why_negative": "Installation history and crime statistics share vocabulary with the investigation but participate in no investigative chain."
          },
          "variation_parameters": {
            "crime_category": {
              "values": ["financial fraud", "physical theft", "cybercrime", "homicide", "corporate espionage", "art forgery"],
              "why_this_varies": "Different crime categories have structurally different investigation arcs and discovery vocabularies"
            },
            "investigation_stage": {
              "values": ["initial discovery to first lead", "lead to suspect identification", "suspect to prosecution evidence"],
              "why_this_varies": "Different stages create different types of temporal dependency between sentences"
            },
            "evidence_type": {
              "values": ["physical", "digital", "testimonial", "financial records", "biological"],
              "why_this_varies": "Evidence type determines what the B sentence discovers and what vocabulary it uses"
            },
            "jurisdiction": {
              "values": ["local", "federal", "international", "corporate internal"],
              "why_this_varies": "Jurisdiction changes who is doing the investigating and what tools they have"
            }
          },
          "combination_space": 432,
          "notes": "Close hard negative must use the same location name, same victim name, or same crime time as the chain sentences."
        },
        {
          "type_id": "organizational_lifecycle",
          "type_description": "Business, institutional, or product lifecycle stages where each phase is only meaningful given the prior phase was completed.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - organizational phases build on prior established states. You cannot scale what has not been validated.",
            "structure": "sentence_A (early phase action or state) → sentence_B (transition event that closes A and opens the next phase) → sentence_C (activity that is only possible given B's transition)",
            "example": "'The team spent four months interviewing 200 potential users to identify a recurring pain point around expense report submission.' → 'A clickable prototype built in two weeks was tested with 30 users, achieving a task completion rate of 87 percent with no instructions.' → 'With validated demand and a working proof of concept, the founders raised a 1.8 million dollar seed round from three angel investors.'",
            "why_asymmetric": "The fundraise in C is only credible given B validated the prototype, which is only meaningful given A identified the real problem. Reversed: knowing the fundraise amount tells you nothing about what user research preceded it.",
            "real_world_application": "Startup narratives, product management documentation, business case writing, investor updates"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (resource requirement at a specific phase) ↔ sentence_Y (the outcome that resource requirement produces at that phase)",
            "example": "'Early-stage startups allocate disproportionate time to direct customer contact rather than product development.' ↔ 'Startups that skip early customer contact typically build products that solve problems users do not actually have.'",
            "why_symmetric": "X describes the investment; Y describes what happens when the investment is made versus skipped. Each makes the other prescriptive."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same company name, same funding figures, or same product vocabulary but provide market comparison or team biography instead of lifecycle chain.",
            "examples": [
              "CLOSE: 'The startup was founded by two former engineers from a major technology company and operates out of a coworking space.' (same company context, zero lifecycle chain value)",
              "CLOSE: 'Seed rounds in enterprise software averaged 1.6 million dollars in the most recent fiscal year.' (same domain, benchmark statistic, zero specific chain value)",
              "DISTANT: 'Venture capital funds typically reserve 40 percent of their capital for follow-on investments in their portfolio companies.'"
            ],
            "why_negative": "Team biography and market benchmarks share startup vocabulary but provide no lifecycle dependency chain."
          },
          "variation_parameters": {
            "organization_type": {
              "values": ["technology startup", "nonprofit", "corporate spinout", "government program", "academic research group"],
              "why_this_varies": "Different organization types have structurally different lifecycle phases and transition events"
            },
            "lifecycle_stage": {
              "values": ["discovery to validation", "validation to launch", "launch to scale", "scale to exit or maturity"],
              "why_this_varies": "Different stages create different temporal chain structures and different vocabulary"
            },
            "constraint": {
              "values": ["resource-constrained", "time-constrained", "regulatory-constrained", "market-constrained"],
              "why_this_varies": "Different constraints change what each phase must accomplish before the next can begin"
            }
          },
          "combination_space": 270,
          "notes": "Each chain must make the dependency between phases explicit - not just sequential but causally ordered."
        },
        {
          "type_id": "ecological_process_sequence",
          "type_description": "Natural ecological and geological processes where each stage creates the physical conditions that enable the next stage.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity mirroring natural process order. Geological and ecological sequences are irreversible - you cannot have the forest before the pioneer species.",
            "structure": "sentence_A (initial environmental condition or disturbance) → sentence_B (biological or physical response that transforms that condition) → sentence_C (new stable state that only exists because of B's transformation)",
            "example": "'A volcanic eruption deposited a layer of sterile basalt across 300 square kilometers of previously forested land.' → 'Within two years, nitrogen-fixing pioneer species including mosses and lupines colonized the bare rock, beginning to create thin organic soil layers.' → 'By the fourth decade, the accumulated organic matter supported shrub species that shaded out the pioneer plants, initiating the transition to secondary forest.'",
            "why_asymmetric": "B only occurs given the sterile substrate created by A. C is impossible without the soil created by B. Reversed: knowing secondary forest developed tells you almost nothing about what disturbance started the sequence.",
            "real_world_application": "Ecology textbooks, environmental impact reports, conservation planning, natural history writing"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (ecological relationship) ↔ sentence_Y (the feedback mechanism that maintains that relationship)",
            "example": "'Mycorrhizal fungi extend the effective root area of host trees by several orders of magnitude in exchange for photosynthetically produced sugars.' ↔ 'Trees deprived of mycorrhizal networks show reduced growth and drought tolerance even in nutrient-rich soil, demonstrating the functional dependency runs in both directions.'",
            "why_symmetric": "X describes the exchange relationship; Y demonstrates that the dependency is genuinely mutual by showing what happens when it is broken. Each makes the other scientifically complete."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same species names, same location, or same ecosystem type but provide distribution statistics or taxonomic classification instead of process chains.",
            "examples": [
              "CLOSE: 'Lupines are members of the legume family and produce seeds in distinctive elongated pods.' (same species, taxonomic fact, zero succession chain value)",
              "CLOSE: 'Volcanic eruptions of this magnitude occur approximately once every 50 to 100 years in tectonically active regions.' (same event type, frequency statistic, zero succession value)",
              "DISTANT: 'Coral bleaching events caused by thermal stress have increased in frequency and severity since the 1980s.'"
            ],
            "why_negative": "Taxonomic classification and eruption frequency statistics share ecosystem vocabulary but participate in no succession chain."
          },
          "variation_parameters": {
            "ecosystem_type": {
              "values": ["boreal forest", "coral reef", "grassland", "wetland", "alpine", "deep ocean"],
              "why_this_varies": "Different ecosystems have radically different succession structures and species vocabularies"
            },
            "disturbance_type": {
              "values": ["volcanic", "wildfire", "flood", "glacial retreat", "deforestation", "invasive species introduction"],
              "why_this_varies": "Disturbance type determines the starting conditions in A and therefore the entire chain structure"
            },
            "timescale": {
              "values": ["years", "decades", "centuries", "millennia"],
              "why_this_varies": "Timescale changes what counts as a meaningful intermediate stage in B"
            }
          },
          "combination_space": 270,
          "notes": "Ensure the physical or chemical transformation in B is described mechanistically, not just labeled. The model must see what changed, not just that something changed."
        },
        {
          "type_id": "geopolitical_escalation_arc",
          "type_description": "Political and diplomatic sequences where each decision or event creates the specific conditions that made the next decision rational or inevitable.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "TEMPORAL",
            "linguistic_principle": "Iconicity - diplomatic and political sequences are path-dependent. Each decision is shaped by the landscape left by the prior decision.",
            "structure": "sentence_A (initial political action or decision by an actor) → sentence_B (response by another actor that was rational given A) → sentence_C (outcome that only follows given both A and B as prior context)",
            "example": "'The central bank raised interest rates by 75 basis points for the third consecutive meeting, signaling that inflation control took priority over economic growth.' → 'Three major corporations announced layoff rounds totaling 40,000 positions within six weeks of the rate decision, citing the increased cost of capital.' → 'Consumer confidence fell to its lowest reading in eleven years as unemployment data confirmed the labor market contraction the bank's policy had predicted would occur.'",
            "why_asymmetric": "The layoffs in B are a rational corporate response to the specific rate signal in A. The confidence collapse in C is only explicable given both A created the expectation and B confirmed it. Reversed: knowing consumer confidence fell tells you nothing about what policy decision triggered the sequence.",
            "real_world_application": "Economic journalism, policy analysis, political science research, government communications"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (structural condition in a political system) ↔ sentence_Y (type of event that condition makes more likely or more severe)",
            "example": "'Coalition governments require continuous negotiation among parties with divergent constituencies to maintain legislative majorities.' ↔ 'Budget crises in coalition governments tend to be more prolonged than in single-party governments because each line item must satisfy multiple veto players.'",
            "why_symmetric": "X explains the structural feature; Y explains the functional consequence that feature produces in a specific recurring scenario. Each contextualizes the other."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same economic indicators, same institution names, or same percentage figures but provide definitional or historical facts instead of decision chains.",
            "examples": [
              "CLOSE: 'The central bank was established in 1913 and operates independently of the executive branch under its founding legislation.' (same institution, historical fact, zero decision chain value)",
              "CLOSE: 'A basis point is one hundredth of one percentage point and is the standard unit for expressing interest rate changes.' (same vocabulary, definition, zero sequence value)",
              "DISTANT: 'Sovereign wealth funds invest national surplus revenue in global markets to provide long-term financial stability.'"
            ],
            "why_negative": "Institutional history and definitional facts share the vocabulary of the sequence but participate in no decision chain."
          },
          "variation_parameters": {
            "domain": {
              "values": ["monetary policy", "trade negotiation", "military alliance", "electoral politics", "international sanctions"],
              "why_this_varies": "Different political domains have different actor types and different escalation mechanisms"
            },
            "actor_count": {
              "values": ["two actors", "three or more actors", "multilateral institution"],
              "why_this_varies": "More actors create more complex path dependencies and different chain structures"
            },
            "outcome_type": {
              "values": ["cooperative resolution", "escalation", "stalemate", "unilateral withdrawal"],
              "why_this_varies": "Different outcomes require different C sentence structures and different prior conditions"
            }
          },
          "combination_space": 270,
          "notes": "The rationality of each actor's decision given the prior context is the key asymmetry signal. B must be interpretable as a rational response to A specifically."
        }
      ]
    },
    {
      "domain": "FAILURE_MODE_ANALYSIS",
      "domain_description": "Root cause reasoning about system, organizational, and human failures where the correct diagnosis is prerequisite to the correct intervention. Teaches CAUSAL asymmetry through failure attribution rather than simple troubleshooting. The diagnostic chain is the core structure: observed failure → attributed cause → targeted intervention.",
      "batch_allocation": 500,
      "information_types": [
        {
          "type_id": "cognitive_bias_in_decision",
          "type_description": "Human decision failures caused by identifiable cognitive biases, where knowing the bias type determines the correct debiasing intervention.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Causal explanation - the specific error pattern in the decision identifies the cognitive mechanism, which determines what intervention will correct future decisions.",
            "structure": "sentence_A (observed decision error with specific pattern) → sentence_B (cognitive mechanism that produces that specific error pattern) → sentence_C (debiasing technique that targets that mechanism)",
            "example": "'The investment committee approved the project despite analysts flagging three significant risk factors, because the CEO expressed strong enthusiasm at the start of the meeting.' → 'Authority bias caused the committee to anchor on the CEO's framing and discount independent analysis that contradicted the authority figure's position.' → 'Structured pre-mortem exercises where participants independently document failure scenarios before group discussion prevent authority bias from suppressing dissenting analysis.'",
            "why_asymmetric": "The intervention in C is specifically designed for authority bias identified in B. Without B, you might apply the wrong debiasing technique. Reversed: knowing pre-mortems are useful tells you nothing about what specific decision failure caused it to be recommended.",
            "real_world_application": "Behavioral economics training, management consulting, organizational psychology, decision quality auditing"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (cognitive bias mechanism) ↔ sentence_Y (the environmental condition that amplifies that bias)",
            "example": "'Sunk cost fallacy causes decision makers to continue failing projects because they weight prior investment rather than future returns.' ↔ 'Time pressure and public commitment to a project dramatically amplify sunk cost reasoning by reducing cognitive bandwidth for counterfactual thinking.'",
            "why_symmetric": "X describes the bias; Y describes the context that makes it worse. Together they define both the mechanism and the conditions under which it most needs to be countered."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same bias name, same organization type, or same decision vocabulary but provide academic citation history or general definitions instead of causal chains.",
            "examples": [
              "CLOSE: 'Authority bias was first systematically studied by Stanley Milgram in his obedience experiments at Yale in the 1960s.' (same bias, historical attribution, zero decision chain value)",
              "CLOSE: 'Investment committees in large organizations typically meet quarterly and require a quorum of senior members.' (same organizational context, procedural fact, zero causal chain value)",
              "DISTANT: 'Prospect theory describes how people evaluate gains and losses asymmetrically relative to a reference point.'"
            ],
            "why_negative": "Research history and procedural facts share cognitive bias vocabulary but participate in no causal chain between error and intervention."
          },
          "variation_parameters": {
            "bias_type": {
              "values": ["authority bias", "confirmation bias", "availability heuristic", "anchoring", "groupthink", "overconfidence", "status quo bias"],
              "why_this_varies": "Different biases have structurally different error patterns and require completely different debiasing interventions"
            },
            "decision_domain": {
              "values": ["corporate strategy", "medical diagnosis", "hiring", "public policy", "financial investment", "legal judgment"],
              "why_this_varies": "The same bias manifests differently in different decision contexts, changing the vocabulary of all three sentences"
            },
            "severity": {
              "values": ["minor suboptimal outcome", "significant financial loss", "safety-critical error"],
              "why_this_varies": "Severity affects the stakes and the urgency of the intervention described in C"
            }
          },
          "combination_space": 294,
          "notes": "The error pattern in A must be specific enough that only one bias type (in B) is the correct attribution. Vague errors create multiple valid B sentences and weaken the chain."
        },
        {
          "type_id": "supply_chain_disruption",
          "type_description": "Supply chain failures where the point of failure propagates through the network in a specific causal direction, and the correct intervention targets the propagation mechanism.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Propagation causality - supply chain failures have a specific origin point and direction of propagation. Intervening at the effect rather than the cause leaves the propagation mechanism intact.",
            "structure": "sentence_A (downstream disruption visible to the end of chain) → sentence_B (upstream cause that produced the propagation) → sentence_C (intervention at the causal origin that stops further propagation)",
            "example": "'Semiconductor assembly plants in Malaysia began receiving incorrect voltage regulators from their supplier, causing a 40 percent defect rate in completed circuit boards.' → 'A specification change by the circuit board manufacturer was communicated verbally to procurement but never updated in the formal supplier purchase order system, so the wrong part continued to be ordered.' → 'The manufacturer implemented a change control procedure requiring engineering change orders to be formally closed in the procurement system before any physical implementation can proceed.'",
            "why_asymmetric": "The intervention in C targets the process gap identified in B, not the defect rate in A. Without B, C would be something like 'improve incoming inspection' which treats the effect. Reversed: knowing a change control procedure exists tells you nothing about what defect rate initiated the investigation.",
            "real_world_application": "Supply chain management, quality engineering, operations consulting, manufacturing postmortem analysis"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (supply chain vulnerability) ↔ sentence_Y (risk mitigation strategy designed specifically for that vulnerability)",
            "example": "'Single-source supplier dependency means that any disruption at one facility immediately propagates to all downstream production lines.' ↔ 'Dual-sourcing strategies for critical components maintain two qualified suppliers even at higher unit cost, providing a failover when one source is disrupted.'",
            "why_symmetric": "X identifies the structural vulnerability; Y describes the mitigation designed to address exactly that vulnerability. Each makes the other operationally meaningful."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same component names, same country of origin, or same defect rate vocabulary but provide market share data or supplier history instead of causal chains.",
            "examples": [
              "CLOSE: 'Malaysia is one of the top five semiconductor manufacturing countries globally, hosting facilities for more than 50 major producers.' (same location, economic fact, zero causal chain value)",
              "CLOSE: 'Voltage regulators are passive electronic components that maintain a constant output voltage regardless of input variation.' (same component, definition, zero propagation chain value)",
              "DISTANT: 'Just-in-time inventory management reduces warehousing costs but increases vulnerability to supply disruption.'"
            ],
            "why_negative": "Country rankings and component definitions share supply chain vocabulary but do not trace any causal propagation."
          },
          "variation_parameters": {
            "industry": {
              "values": ["electronics", "pharmaceutical", "automotive", "food and beverage", "aerospace", "medical devices"],
              "why_this_varies": "Different industries have different supply chain structures and different intervention options"
            },
            "failure_origin": {
              "values": ["tier-1 supplier", "tier-2 supplier", "logistics partner", "internal process", "regulatory change"],
              "why_this_varies": "Different failure origins create different propagation paths and different chain structures"
            },
            "disruption_type": {
              "values": ["quality failure", "delivery failure", "capacity shortage", "specification mismatch", "regulatory non-compliance"],
              "why_this_varies": "Disruption type determines what the visible symptom in A looks like and what the intervention in C addresses"
            }
          },
          "combination_space": 270,
          "notes": "The propagation direction from cause to effect must be explicit in B. 'This caused that' is not enough - the mechanism of propagation is the key teaching signal."
        },
        {
          "type_id": "architectural_failure_pattern",
          "type_description": "Software and systems architecture failures where a specific architectural anti-pattern is the root cause of observed reliability or performance problems.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Structural causality - architectural decisions create systematic failure modes that persist until the structure is changed. Fixing symptoms without changing structure causes recurrence.",
            "structure": "sentence_A (recurring operational failure pattern with specific characteristics) → sentence_B (architectural anti-pattern that structurally produces A) → sentence_C (architectural refactoring that eliminates the structural cause)",
            "example": "'Every time traffic exceeds 8,000 concurrent users the checkout service becomes unavailable for 15 to 20 minutes before recovering, and this has happened identically on each of the past four high-traffic events.' → 'The checkout service maintains a synchronous connection to the inventory database for every item in the cart, creating a linear scaling bottleneck where connection pool exhaustion under load causes cascading timeouts.' → 'Decoupling inventory validation from checkout using an asynchronous event queue with eventual consistency allows checkout to proceed without holding a database connection, eliminating the linear scaling constraint.'",
            "why_asymmetric": "The refactoring in C is designed specifically for the synchronous bottleneck identified in B. Applying C without B's diagnosis would mean adding infrastructure without addressing the synchronous coupling. Reversed: knowing eventual consistency is used tells you nothing about what failure pattern motivated it.",
            "real_world_application": "Software architecture review, system design interviews, incident postmortems, technical debt documentation"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (architectural property) ↔ sentence_Y (operational consequence of that property under specific load conditions)",
            "example": "'Synchronous request chains couple the latency of each dependent service, making end-to-end response time the sum of all individual service latencies.' ↔ 'In a chain of five synchronous services each averaging 50ms, tail latency at the 99th percentile compounds to over 1 second even with no individual service degradation.'",
            "why_symmetric": "X explains the property; Y quantifies what that property means in practice under real operational conditions. Each makes the other measurably concrete."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same service name, same metric thresholds, or same architectural terms but provide vendor comparison or industry benchmark data instead of causal structure.",
            "examples": [
              "CLOSE: 'The checkout service was built using a microservices architecture deployed on Kubernetes and processes approximately 2 million transactions per day in normal operation.' (same service, operational statistics, zero architectural failure chain value)",
              "CLOSE: 'Database connection pooling was standardized in most enterprise frameworks in the early 2000s to reduce connection overhead.' (same concept, historical fact, zero structural chain value)",
              "DISTANT: 'CQRS separates read and write operations into distinct models to optimize each independently.'"
            ],
            "why_negative": "Operational statistics and technology history share architecture vocabulary but do not trace any structural causal chain."
          },
          "variation_parameters": {
            "anti_pattern_type": {
              "values": ["synchronous coupling", "shared mutable state", "monolithic deployment", "tight database dependency", "missing circuit breaker", "synchronous saga"],
              "why_this_varies": "Different anti-patterns produce different failure signatures and require different architectural interventions"
            },
            "failure_signature": {
              "values": ["linear degradation with load", "sudden cliff at threshold", "cascading failure", "memory leak pattern", "thundering herd"],
              "why_this_varies": "Different failure signatures are the observable symptoms in A that point to different anti-patterns in B"
            },
            "scale": {
              "values": ["single service", "service-to-service interaction", "data layer", "infrastructure level"],
              "why_this_varies": "Scale determines the scope of the architectural change needed in C"
            }
          },
          "combination_space": 270,
          "notes": "The recurrence pattern in A is the signal that distinguishes architectural failure from random incident. Ensure A mentions that the failure has happened repeatedly with the same characteristics."
        },
        {
          "type_id": "relationship_conflict_diagnosis",
          "type_description": "Interpersonal and organizational conflict where a recurring pattern in interactions reveals an underlying relational or structural dynamic that must be addressed.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CAUSAL",
            "linguistic_principle": "Systemic causality in relationships - recurring conflict patterns are symptoms of underlying relational dynamics. Addressing the surface conflict without the dynamic causes recurrence.",
            "structure": "sentence_A (recurring conflict or communication failure with specific pattern) → sentence_B (underlying relational or structural dynamic producing the pattern) → sentence_C (structural or relational intervention that addresses the dynamic)",
            "example": "'Every time the engineering team misses a deadline, the product manager escalates to the VP rather than speaking directly with the engineering lead, and the engineering lead finds out from their VP rather than the product manager.' → 'The product manager does not feel safe raising concerns directly because in a previous incident the engineering lead responded defensively and later excluded them from technical planning meetings as a consequence.' → 'A structured weekly touchpoint with a neutral facilitator for the first three months creates a safe channel for both parties to surface risks directly before they become escalations.'",
            "why_asymmetric": "The facilitated touchpoint in C addresses the specific psychological safety deficit identified in B. Without B, C would be irrelevant or counterproductive. Reversed: knowing a structured meeting was introduced tells you nothing about the specific escalation pattern that necessitated it.",
            "real_world_application": "Executive coaching, organizational development, team effectiveness consulting, HR mediation"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (relational dynamic) ↔ sentence_Y (the behavioral pattern that dynamic produces and that also reinforces the dynamic)",
            "example": "'When one party in a working relationship consistently withholds information to maintain control, the other party develops informal information networks to work around them.' ↔ 'The existence of informal workaround networks confirms to the information-withholding party that they are correct to be guarded, reinforcing the original withholding behavior.'",
            "why_symmetric": "X describes the dynamic; Y describes the behavioral consequence that loops back to strengthen the dynamic. Each explains why the other persists without intervention."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same role titles, same organizational terms, or same conflict vocabulary but provide management theory citations or HR policy descriptions instead of causal chains.",
            "examples": [
              "CLOSE: 'Product managers are responsible for defining the product roadmap and communicating requirements to engineering teams.' (same roles, job description fact, zero conflict chain value)",
              "CLOSE: 'Workplace conflict is estimated to cost US businesses approximately 359 billion dollars annually in lost productivity.' (same domain, economic statistic, zero causal chain value)",
              "DISTANT: 'Nonviolent communication frameworks distinguish between observations, feelings, needs, and requests as four components of effective expression.'"
            ],
            "why_negative": "Job descriptions and conflict cost statistics share organizational vocabulary but participate in no specific relational causal chain."
          },
          "variation_parameters": {
            "relationship_type": {
              "values": ["peer colleagues", "manager and direct report", "cross-functional partners", "client and vendor", "co-founders"],
              "why_this_varies": "Different relationship types have different power dynamics and different available interventions"
            },
            "conflict_pattern": {
              "values": ["avoidance", "escalation bypass", "information hoarding", "credit attribution conflict", "scope encroachment"],
              "why_this_varies": "Different conflict patterns point to different underlying dynamics and require different interventions"
            },
            "organizational_context": {
              "values": ["startup", "corporate", "nonprofit", "academic institution", "government agency"],
              "why_this_varies": "Context determines what structural interventions are available and appropriate"
            }
          },
          "combination_space": 270,
          "notes": "The recurring nature of the conflict pattern in A is essential. One-time conflicts do not reveal underlying dynamics. Ensure A explicitly mentions that the pattern repeats."
        }
      ]
    },
    {
      "domain": "CONCEPTUAL_SCAFFOLDING",
      "domain_description": "Explanatory contexts where a foundational concept must be established before a dependent concept can be correctly understood. Teaches EPISTEMIC asymmetry through paradigm building, model elaboration, and cross-domain analogy rather than simple given-new information. Includes misconception correction as a subtype.",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "paradigm_shift_explanation",
          "type_description": "Scientific or intellectual paradigm changes where the old model must be understood before the anomaly that broke it and the new model that replaced it are comprehensible.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given-New contract - the old paradigm is shared knowledge that makes the anomaly legible. Without knowing what everyone believed, the anomaly appears as just another fact rather than a crisis.",
            "structure": "sentence_A (dominant prior paradigm, stated as shared knowledge) → sentence_B (anomalous finding that the prior paradigm cannot explain) → sentence_C (new conceptual framework that explains both old observations and the anomaly)",
            "example": "'For most of the 20th century, stomach ulcers were believed to be caused by stress and excess stomach acid, leading to treatments focused on antacids and stress reduction.' → 'In 1982, Barry Marshall and Robin Warren cultured a bacterium, Helicobacter pylori, from the stomach lining of nearly all ulcer patients, a location previously considered too acidic to support life.' → 'Recognizing ulcers as a bacterial infection rather than a lifestyle disease led to antibiotic-based cures with a greater than 90 percent success rate, replacing lifelong antacid dependency.'",
            "why_asymmetric": "B is astonishing and meaningful only given A established what everyone believed. Without A, finding bacteria in the stomach is merely a microbiological observation. C transforms medicine only given B broke the prior model. Reversed: knowing antibiotics cure ulcers tells you nothing about what prior belief made that discovery revolutionary.",
            "real_world_application": "Science communication, history of science, intellectual biography, paradigm change teaching"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (property of the new paradigm) ↔ sentence_Y (the specific type of anomaly that property was designed to explain)",
            "example": "'Plate tectonics models the Earth's lithosphere as a set of rigid plates moving relative to each other on a viscous mantle.' ↔ 'The geographic fit between South American and African coastlines, similar fossil records on both continents, and matching rock formations at their margins were anomalies that earlier fixed-continent models could not account for.'",
            "why_symmetric": "X describes the new model; Y describes the set of anomalies the model was specifically constructed to explain. Each contextualizes the other's scientific significance."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same scientist names, same disease or phenomenon vocabulary, or same historical period but provide biographical or institutional context instead of paradigm chain.",
            "examples": [
              "CLOSE: 'Barry Marshall received the Nobel Prize in Physiology or Medicine in 2005 together with Robin Warren for their discovery of H. pylori.' (same discovery, award context, zero paradigm chain value)",
              "CLOSE: 'H. pylori infection affects approximately 44 percent of the global population and is more prevalent in developing countries.' (same bacterium, epidemiology, zero paradigm shift chain value)",
              "DISTANT: 'Prion diseases challenged the central dogma of molecular biology by demonstrating that proteins can transmit heritable information without nucleic acids.'"
            ],
            "why_negative": "Nobel Prize context and infection prevalence statistics share the H. pylori vocabulary but participate in no paradigm chain."
          },
          "variation_parameters": {
            "knowledge_domain": {
              "values": ["medicine", "physics", "economics", "geology", "psychology", "cosmology", "linguistics"],
              "why_this_varies": "Different disciplines have different paradigm structures and different types of anomalies that break old models"
            },
            "paradigm_age": {
              "values": ["centuries-old", "decades-old", "recently established"],
              "why_this_varies": "Older paradigms have deeper entrenchment and more dramatic reversals, affecting how sentence A is framed"
            },
            "resistance_level": {
              "values": ["rapid adoption", "strong institutional resistance", "gradual acceptance over decades"],
              "why_this_varies": "Resistance level adds contextual information about why the old paradigm persisted despite the anomaly"
            }
          },
          "combination_space": 378,
          "notes": "The prior paradigm in A must be stated as something the audience was genuinely expected to believe. Obscure prior beliefs do not create the epistemic contrast needed."
        },
        {
          "type_id": "model_boundary_elaboration",
          "type_description": "Explanations that establish a model or framework, then reveal where that model breaks down, then introduce the refined model that handles both cases.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given-New scaffolding - knowing the model is prerequisite to understanding where and why it fails. You cannot appreciate a limitation without first understanding what the model does correctly.",
            "structure": "sentence_A (model or simplification stated as useful but incomplete) → sentence_B (specific case where the model's predictions diverge from reality) → sentence_C (refinement or successor model that handles both the original domain and the edge case)",
            "example": "'Newtonian mechanics accurately describes the motion of macroscopic objects at everyday speeds and is taught as the foundational model of physics.' → 'At velocities approaching a significant fraction of the speed of light, Newtonian predictions for momentum and energy become measurably wrong, with discrepancies that compound at higher velocities.' → 'Special relativity replaces Newtonian mechanics for high-velocity regimes while reducing to Newton's equations at low velocities, making it the more complete theory that subsumes rather than replaces classical mechanics.'",
            "why_asymmetric": "B is meaningful only given A established what Newtonian mechanics predicts. Without A, relativistic corrections are incomprehensible - corrections to what? C is a refinement that requires B to motivate it. Reversed: knowing relativity reduces to Newtonian mechanics at low speeds tells you nothing about what limitation made that a requirement.",
            "real_world_application": "Physics and mathematics education, model documentation, scientific writing, engineering approximation guidelines"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (domain where simplified model applies) ↔ sentence_Y (domain where simplified model fails and refined model is required)",
            "example": "'For most engineering applications involving structural loads and everyday materials, linear elastic models provide accurate predictions with far less computational cost than nonlinear models.' ↔ 'Under extreme deformation, material failure conditions, or cyclic loading, nonlinear plastic deformation must be modeled explicitly because linear assumptions produce dangerous underestimates of stress.'",
            "why_symmetric": "X defines when to use the simple model; Y defines when you must use the complex model. Each sentence makes the other prescriptively complete for an engineer choosing between models."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same model name, same physicist or mathematician, or same domain but provide historical development or mathematical notation instead of model limitation chains.",
            "examples": [
              "CLOSE: 'Newton published his three laws of motion in Principia Mathematica in 1687, a work considered foundational to classical mechanics.' (same theory, historical fact, zero model limitation chain value)",
              "CLOSE: 'Newtonian mechanics uses calculus, which Newton developed concurrently with Leibniz during the same period.' (same theory, disciplinary history, zero refinement chain value)",
              "DISTANT: 'Quantum field theory unifies quantum mechanics and special relativity by treating particles as excitations of underlying fields.'"
            ],
            "why_negative": "Publication history and mathematical development context share theory names but provide no model-limitation-refinement chain."
          },
          "variation_parameters": {
            "model_type": {
              "values": ["physical model", "economic model", "biological model", "computational model", "psychological model"],
              "why_this_varies": "Different model types have different failure modes and different successor frameworks"
            },
            "limitation_type": {
              "values": ["scale limitation", "speed limitation", "complexity limitation", "assumption violation", "emergent phenomenon"],
              "why_this_varies": "Different limitation types produce different B sentences and different successor models in C"
            },
            "successor_relationship": {
              "values": ["replaces entirely", "extends", "subsumes as special case", "runs in parallel for different domains"],
              "why_this_varies": "The relationship between old and new model determines how C is framed"
            }
          },
          "combination_space": 360,
          "notes": "C must subsume A's domain, not just describe a different theory. The refinement relationship is the key epistemic teaching signal."
        },
        {
          "type_id": "cross_domain_structural_analogy",
          "type_description": "Explanations that use a known principle from one domain as scaffolding to make a structurally identical principle in another domain comprehensible.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Given-New through analogy - the known domain (A) provides the structural scaffold that makes the target domain (B) immediately comprehensible. Without A, B requires independent derivation.",
            "structure": "sentence_A (principle in familiar domain, assumed known) → sentence_B (structurally identical principle in unfamiliar domain, made comprehensible by A) → sentence_C (the structural property that makes the analogy hold and its limits)",
            "example": "'In electrical circuits, resistance limits current flow in proportion to voltage, and higher resistance means less current for the same driving voltage.' → 'In fluid dynamics, viscosity plays an analogous role to resistance, limiting flow rate in proportion to pressure difference, with more viscous fluids requiring higher pressure to achieve the same flow rate.' → 'Both relationships are instances of a linear response law where a driving force produces a proportional flow opposed by a material property, a structure that appears in thermal conductivity, diffusion, and several other physical systems.'",
            "why_asymmetric": "B is immediately intuitive given A because the structure is identical. Without A, viscosity and pressure require independent explanation. C reveals why the analogy holds, which is only meaningful once both A and B are established. Reversed: knowing the linear response law is general tells you nothing about which familiar domain makes viscosity intuitive.",
            "real_world_application": "Science pedagogy, cross-disciplinary research papers, popular science writing, technical onboarding"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (mechanism in domain 1) ↔ sentence_Y (mechanism in domain 2 that the same structural principle describes)",
            "example": "'Compound interest causes small differences in interest rates to produce exponentially diverging wealth over decades.' ↔ 'Exponential growth in epidemics causes small differences in transmission rates to produce dramatically different infection curves over weeks, which is why early interventions have disproportionate impact.'",
            "why_symmetric": "X and Y are both instances of exponential dynamics in different domains. Each makes the other more intuitive by providing a concrete instantiation of the same abstract structure."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same domain terms but describe a superficially similar phenomenon with a different underlying structure, making the analogy false.",
            "examples": [
              "CLOSE: 'In electrical circuits, capacitance stores energy in an electric field and releases it when the circuit demands current.' (same circuit domain, different phenomenon - not analogous to resistance, the analogy breaks)",
              "CLOSE: 'Fluid dynamics is the branch of physics that studies the behavior of liquids and gases in motion, with applications in aerodynamics and hydraulics.' (same domain, definitional, zero structural analogy value)",
              "DISTANT: 'Category theory in mathematics abstracts structural patterns that appear across different mathematical domains under a unified framework.'"
            ],
            "why_negative": "False analogies (capacitance is not like resistance in the relevant way) and domain definitions share vocabulary but break or avoid the structural analogy that is the point of the chain."
          },
          "variation_parameters": {
            "source_domain": {
              "values": ["electrical circuits", "fluid dynamics", "mechanical systems", "financial markets", "evolutionary biology"],
              "why_this_varies": "Different source domains are familiar to different audiences, creating different scaffolding effectiveness"
            },
            "target_domain": {
              "values": ["neuroscience", "information theory", "thermodynamics", "population dynamics", "social network theory"],
              "why_this_varies": "Different target domains have different degrees of unfamiliarity and different abstraction levels"
            },
            "analogy_fidelity": {
              "values": ["near-perfect structural identity", "structural similarity with important limits", "partial analogy with noted divergences"],
              "why_this_varies": "Analogy fidelity affects what the C sentence must say about where the analogy breaks"
            }
          },
          "combination_space": 324,
          "notes": "The structural property in C is the key - it must name the abstract principle that both A and B instantiate. Without naming the structure, the analogy is anecdotal."
        },
        {
          "type_id": "embedded_presupposition_correction",
          "type_description": "Explanations that reveal and correct a false presupposition embedded in a question or belief, then provide the accurate framing. Teaches that high-value correction of a presupposition is different from simple factual contradiction.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "EPISTEMIC",
            "linguistic_principle": "Presupposition accommodation - a statement or question can embed a false assumption that must be surfaced and rejected before a correct answer is possible. The correction is only meaningful given the false presupposition was first named.",
            "structure": "sentence_A (question or belief that embeds a specific false presupposition) → sentence_B (identification and correction of the presupposition itself, not just the surface claim) → sentence_C (accurate answer or belief that follows given the corrected presupposition)",
            "example": "'Why did Einstein fail mathematics in school, given that he became the most famous physicist in history?' → 'Einstein did not fail mathematics in school - he excelled and had mastered calculus by age 15, making the question unanswerable because its premise is false.' → 'The misconception arose from a misreading of Swiss grading conventions, where 6 is the top grade, not 1, leading to reports of his high scores being misinterpreted as failures.'",
            "why_asymmetric": "B is only meaningful given A stated the false presupposition explicitly. Without A, B appears to be an unprompted defense of Einstein's math ability. C provides the accurate account, which only makes sense given B corrected the framework. SCORING NOTE: B contradicts A's embedded assumption but should score HIGH for A→B because the correction is maximally useful.",
            "real_world_application": "Science journalism, fact-checking, educational Q&A, debate preparation, critical thinking training"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (the true fact) ↔ sentence_Y (why the false version of this fact is so persistently believed)",
            "example": "'Humans use all regions of their brain regularly throughout the day, with different regions more active during different tasks.' ↔ 'The 10 percent of the brain myth persists because it is emotionally appealing - it implies unused potential waiting to be unlocked - and because it is repeated by self-help authors for whom the false claim is commercially useful.'",
            "why_symmetric": "X states the true fact; Y explains the sociological mechanism that keeps the false version alive. Each makes the other complete as a full debunking."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives are true statements about the same person, institution, or phenomenon that do not address the presupposition or the correction.",
            "examples": [
              "CLOSE: 'Einstein was born in Ulm, Germany in 1879 and moved to Switzerland as a teenager, eventually becoming a Swiss citizen.' (same person, biographical fact, does not address the math performance presupposition)",
              "CLOSE: 'The special theory of relativity was published by Einstein in 1905, a year often called his annus mirabilis in which he also published four other landmark papers.' (same person, historical context, zero presupposition correction value)",
              "DISTANT: 'Cognitive biases cause people to selectively remember information that confirms their existing beliefs about famous figures.'"
            ],
            "why_negative": "Biographical facts and publication history share the Einstein vocabulary but neither embed the false presupposition nor provide any correction."
          },
          "variation_parameters": {
            "presupposition_type": {
              "values": ["false biographical fact", "false causal attribution", "false categorical membership", "false quantitative claim", "false temporal sequence"],
              "why_this_varies": "Different presupposition types require different correction structures in B"
            },
            "subject_domain": {
              "values": ["famous scientists", "historical events", "medical claims", "economic beliefs", "legal rights", "nutritional facts"],
              "why_this_varies": "Different domains have different types of culturally embedded false presuppositions"
            },
            "correction_mechanism": {
              "values": ["definitional clarification", "grading convention", "translation error", "misattribution", "selective quotation"],
              "why_this_varies": "How the false presupposition arose determines the structure of the correction and the explanation in C"
            }
          },
          "combination_space": 378,
          "notes": "CRITICAL SCORING NOTE: B scores HIGH for A→B despite contradicting A's embedded assumption. Mark these with presupposition_correction flag. This teaches the model that context determines whether contradiction is high or low utility."
        }
      ]
    },
    {
      "domain": "PRAGMATIC_EXCHANGE",
      "domain_description": "Communicative acts governed by social and institutional obligations. Teaches INTERACTIONAL asymmetry through commitment structures, institutional protocols, and negotiated meaning. Emphasizes that what a response means is determined by what act it is responding to.",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "commitment_and_accountability",
          "type_description": "Exchanges where one party makes a specific commitment that creates obligations, and subsequent utterances are interpretable only given that commitment was made.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Commissive speech acts - a commitment creates a normative expectation that the committed action will occur, making subsequent references to that action interpretable only given the prior commitment.",
            "structure": "sentence_A (explicit commitment made by a party with specific terms) → sentence_B (follow-up that references or updates the commitment) → sentence_C (accountability or outcome statement that is only meaningful given B's update and A's original commitment)",
            "example": "'During the board meeting, the CFO committed to delivering a revised cost reduction plan within ten business days, with savings targets above 8 percent of operating expenses.' → 'On day seven, the CFO notified the board chair that the analysis was complete but that the achievable savings were 6.2 percent, below the committed target, and requested a brief discussion before formal submission.' → 'The board accepted the revised plan with a 6-month performance review clause, reflecting that the CFO's proactive disclosure of the shortfall before the deadline preserved the trust that a silent miss would have damaged.'",
            "why_asymmetric": "B is only interpretable as a pre-deadline update given A established the specific 8 percent commitment and 10-day timeline. C is only meaningful given B established proactive disclosure as the specific form of non-compliance. Reversed: knowing the board accepted a performance review clause tells you nothing about what original commitment framed the acceptance.",
            "real_world_application": "Corporate governance, project management, professional accountability, leadership communication training"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (what a commitment requires from the committing party) ↔ sentence_Y (what proactive update behavior signals about the committing party's reliability)",
            "example": "'A specific, time-bound commitment creates a clear standard against which performance can be objectively measured by both parties.' ↔ 'Proactively disclosing a predicted shortfall before a deadline signals that the committing party prioritizes the relationship over avoiding discomfort, which typically increases rather than decreases the other party's confidence.'",
            "why_symmetric": "X explains the accountability structure; Y explains the counterintuitive dynamic where honest disclosure of failure strengthens trust. Each makes the other actionable for someone managing a commitment."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same role titles, same percentage figures, or same organizational vocabulary but provide general governance principles or industry benchmarks instead of commitment chains.",
            "examples": [
              "CLOSE: 'Chief financial officers typically report directly to the CEO and chair the finance committee in most corporate governance structures.' (same role, structural fact, zero commitment chain value)",
              "CLOSE: 'Cost reduction programs in large enterprises typically target between 5 and 15 percent of operating expenses depending on industry and competitive position.' (same domain, benchmark, zero specific commitment value)",
              "DISTANT: 'Scenario planning allows organizations to prepare multiple strategic responses before uncertainty resolves into a specific outcome.'"
            ],
            "why_negative": "Role descriptions and industry benchmarks share organizational vocabulary but participate in no specific commitment chain."
          },
          "variation_parameters": {
            "commitment_type": {
              "values": ["financial target", "delivery timeline", "quality standard", "relationship boundary", "regulatory compliance"],
              "why_this_varies": "Different commitment types create different accountability structures and different follow-up vocabulary"
            },
            "compliance_outcome": {
              "values": ["full delivery", "partial delivery with disclosure", "silent miss", "renegotiated with notice", "force majeure failure"],
              "why_this_varies": "Different outcomes create structurally different B and C sentences"
            },
            "stakeholder_relationship": {
              "values": ["subordinate to superior", "peer to peer", "vendor to client", "contractor to regulator"],
              "why_this_varies": "Power relationship determines tone, vocabulary, and what accountability looks like in C"
            }
          },
          "combination_space": 270,
          "notes": "The specific terms of the commitment in A (number, date, metric) must be referenced explicitly in B to make the interactional dependency concrete."
        },
        {
          "type_id": "institutional_request_processing",
          "type_description": "Formal institutional exchanges where a request triggers a processing obligation and subsequent communications are only interpretable given that obligation.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Institutional adjacency pairs - formal requests in institutional contexts create mandatory processing obligations. Responses are institutionally defined and interpretable only given the specific request type.",
            "structure": "sentence_A (formal request with specific type and parameters) → sentence_B (institutional response that processes the request according to defined procedure) → sentence_C (outcome communication that closes the request cycle)",
            "example": "'The researcher submitted a formal Freedom of Information Act request to the agency for all internal communications regarding the pesticide approval review conducted between 2018 and 2021.' → 'Within the statutory 20-business-day window, the agency acknowledged receipt and classified the request as complex, extending the response deadline by 30 days under exemption provisions for requests requiring inter-agency coordination.' → 'At day 50, the agency released 847 pages of documents with 23 percent of content redacted under the deliberative process exemption, providing the researcher with grounds to appeal specific redactions.'",
            "why_asymmetric": "B is only interpretable as a procedurally correct response given A was a formal FOIA request. The specific exemption used in B applies only given the request category established in A. C is only a legally meaningful outcome given B's specific procedural steps. Reversed: knowing 847 pages were released with redactions tells you nothing about what formal request generated that response.",
            "real_world_application": "Government accountability journalism, legal practice, regulatory compliance, administrative law training"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (procedural right) ↔ sentence_Y (the institutional mechanism that makes that right exercisable)",
            "example": "'Citizens have a legal right to access most government records under freedom of information legislation.' ↔ 'Agencies must maintain request tracking systems, designate FOIA officers, and publish response logs to operationalize the access right rather than making it theoretical.'",
            "why_symmetric": "X states the right; Y describes the institutional infrastructure that transforms the right from theoretical to practical. Each makes the other concrete."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same legislation name, same agency type, or same document vocabulary but provide policy history or statistical summaries instead of request processing chains.",
            "examples": [
              "CLOSE: 'The Freedom of Information Act was signed into law in 1966 and has been amended multiple times, most significantly in 1974 and 1996.' (same legislation, historical fact, zero processing chain value)",
              "CLOSE: 'Federal agencies receive approximately 900,000 FOIA requests annually, with median response times varying significantly by agency.' (same process, aggregate statistic, zero specific chain value)",
              "DISTANT: 'Whistleblower protection statutes create legal shields for employees who report regulatory violations to designated authorities.'"
            ],
            "why_negative": "Legislative history and aggregate statistics share FOIA vocabulary but participate in no specific request processing chain."
          },
          "variation_parameters": {
            "institution_type": {
              "values": ["government agency", "university", "hospital", "financial regulator", "professional licensing board"],
              "why_this_varies": "Different institutions have different processing procedures, timelines, and exemption categories"
            },
            "request_type": {
              "values": ["information access", "permit application", "formal complaint", "appeal", "benefit claim"],
              "why_this_varies": "Different request types have different processing obligations and different response structures"
            },
            "processing_outcome": {
              "values": ["full grant", "partial grant with redactions", "denial with appeal rights", "extension with explanation", "referral to another body"],
              "why_this_varies": "Different outcomes produce structurally different C sentences and different grounds for subsequent action"
            }
          },
          "combination_space": 270,
          "notes": "The specific procedural category in B (which exemption, which timeline, which officer) must match the specific request type in A. Generic processing responses reduce the interactional asymmetry."
        },
        {
          "type_id": "presupposition_denial_exchange",
          "type_description": "Dialogic exchanges where the second utterance explicitly denies a presupposition of the first rather than answering at face value. Tests negation sensitivity in an interactional context.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Presupposition cancellation - a denial response challenges not the question itself but the embedded assumption that makes the question well-formed. The denial is maximally relevant to the question despite contradicting it.",
            "structure": "sentence_A (question or statement that embeds a specific factual or relational presupposition) → sentence_B (denial that explicitly cancels the presupposition, with the reason) → sentence_C (corrected reframing that provides the accurate picture given B's denial)",
            "example": "'When did you stop including the safety check in your deployment pipeline?' → 'We have not stopped including it - the safety check runs in a separate stage that does not appear in the main pipeline view you are looking at, which is why it looked absent.' → 'If you filter the deployment history by all stages rather than just the main branch jobs, you will see the safety check completing successfully on every deployment for the past six months.'",
            "why_asymmetric": "B is maximally relevant to A as a presupposition denial - it directly addresses the assumption that the safety check was removed. Without A, B is an unprompted explanation of why something appears absent. C provides the corrective evidence, only meaningful given B established the false presupposition. SCORING: A→B HIGH because the denial is the most useful possible response to A. Negation does not reduce relevance here.",
            "real_world_application": "Technical debugging conversations, status review meetings, audit responses, investigative interviewing, diagnostic clinical conversations"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (presupposition embedded in a common question type) ↔ sentence_Y (the accurate framing that replaces the presupposition)",
            "example": "'Questions that ask when someone stopped doing something presuppose they did stop, framing innocent parties as guilty before any evidence is examined.' ↔ 'Neutral investigative questions ask what happened without assuming a specific answer, allowing the respondent to correct false presuppositions without appearing defensive.'",
            "why_symmetric": "X identifies the structure of the leading question; Y describes the alternative that avoids it. Each makes the other practically applicable to someone conducting or responding to an inquiry."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same technical terms, same process names, or same organizational context but provide general descriptions of the process rather than participating in the denial chain.",
            "examples": [
              "CLOSE: 'Deployment pipelines typically include stages for testing, building, security scanning, and deployment to production environments.' (same domain, general description, zero presupposition denial value)",
              "CLOSE: 'Automated safety checks in CI/CD pipelines reduce the incidence of security vulnerabilities reaching production by approximately 60 percent according to DevSecOps surveys.' (same topic, statistic, zero denial chain value)",
              "DISTANT: 'Post-deployment monitoring tools detect anomalies in production traffic that pre-deployment checks may not anticipate.'"
            ],
            "why_negative": "General pipeline descriptions and security statistics share the technical vocabulary but participate in no presupposition-denial-correction chain."
          },
          "variation_parameters": {
            "presupposition_category": {
              "values": ["completion assumed", "cessation assumed", "responsibility assumed", "knowledge assumed", "agreement assumed"],
              "why_this_varies": "Different presupposition categories create structurally different denial responses"
            },
            "denial_evidence": {
              "values": ["direct counter-evidence", "definitional clarification", "contextual reframing", "alternative explanation of appearance"],
              "why_this_varies": "Different evidence types for the denial create different B sentence structures"
            },
            "communication_context": {
              "values": ["technical review", "performance review", "audit", "client report", "medical consultation", "legal deposition"],
              "why_this_varies": "Context determines the stakes of the presupposition and the formality of the denial"
            }
          },
          "combination_space": 270,
          "notes": "CRITICAL: This information type trains negation sensitivity. B must contain an explicit negation ('have not', 'did not', 'never') and still score HIGH for A→B. Include negation_high_relevance flag in batch metadata."
        },
        {
          "type_id": "repair_and_clarification_sequence",
          "type_description": "Conversational repair sequences where a misunderstanding is identified and corrected, with the repair being only interpretable given the specific misunderstanding that prompted it.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "INTERACTIONAL",
            "linguistic_principle": "Conversational repair - when communication breaks down, repair sequences restore shared understanding. The specific repair utterance is interpretable only given the specific breakdown it addresses.",
            "structure": "sentence_A (utterance that reveals or creates a specific misunderstanding) → sentence_B (repair initiation that identifies the source and nature of the misunderstanding) → sentence_C (corrected and clarified restatement that resolves the specific breakdown)",
            "example": "'So you are saying that we should pause all marketing spend until the product redesign is complete next quarter.' → 'That is not quite what I meant - I was recommending pausing the performance marketing channels specifically, not brand awareness spending, because performance channels require a working purchase funnel to be effective.' → 'To be precise, I recommend continuing the brand campaigns at current spend but reducing paid search and retargeting to maintenance levels until the checkout redesign ships in six weeks.'",
            "why_asymmetric": "B is only a coherent repair given A revealed a specific over-generalization of the recommendation. Without A, B appears as an unprompted specification of marketing channel distinctions. C's specificity is only necessary given B identified where the generalization went wrong. Reversed: knowing the specific budget recommendation tells you nothing about what misunderstanding prompted the clarification.",
            "real_world_application": "Business communication, instructional design, clinical communication, technical documentation, meeting facilitation"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (source of systematic communication breakdown) ↔ sentence_Y (structural repair that prevents recurrence of that type of breakdown)",
            "example": "'Recommendations framed at a general level are regularly misinterpreted as applying more broadly than intended when the audience has high stakes in the decision.' ↔ 'Explicitly scoping recommendations with the specific conditions under which they apply, before the audience can anchor on a more general reading, prevents high-stakes misinterpretation at the cost of slightly more complex communication.'",
            "why_symmetric": "X explains the breakdown source; Y describes the preventive communication pattern designed for that specific source. Each makes the other prescriptively actionable."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same marketing, product, or communication vocabulary but provide general communication advice or industry data instead of the specific repair chain.",
            "examples": [
              "CLOSE: 'Marketing spend allocation typically divides between brand awareness, which builds long-term equity, and performance channels, which drive immediate conversion.' (same domain, definitional distinction, zero repair chain value)",
              "CLOSE: 'Misunderstandings in business communication cost organizations an estimated 37 billion dollars annually through project failures and rework.' (same domain, aggregate statistic, zero specific repair chain value)",
              "DISTANT: 'Asynchronous communication tools like email increase the frequency of misunderstandings relative to synchronous conversation because they lack paralinguistic cues.'"
            ],
            "why_negative": "Channel definitions and communication cost statistics share the vocabulary but participate in no specific misunderstanding-repair-clarification chain."
          },
          "variation_parameters": {
            "breakdown_type": {
              "values": ["scope over-generalization", "false equivalence", "misattributed causation", "missed conditionality", "register mismatch"],
              "why_this_varies": "Different breakdown types produce structurally different repair utterances and different clarification forms"
            },
            "professional_context": {
              "values": ["executive meeting", "medical consultation", "legal briefing", "technical review", "client presentation"],
              "why_this_varies": "Context changes the stakes and the vocabulary of both the breakdown and the repair"
            },
            "repair_initiator": {
              "values": ["speaker self-corrects", "listener identifies breakdown", "third party mediates"],
              "why_this_varies": "Who initiates the repair changes the linguistic structure of B significantly"
            }
          },
          "combination_space": 270,
          "notes": "The specific source of misunderstanding in B must directly map to something in A. Generic 'let me clarify' repairs without identifying the specific breakdown reduce the interactional asymmetry signal."
        }
      ]
    },
    {
      "domain": "CATEGORICAL_BOUNDARY",
      "domain_description": "Classification and categorization contexts where specific instances imply their category membership, but category membership does not imply a specific instance. Teaches SEMANTIC asymmetry through edge cases, definitional inheritance, and boundary cases where near-identical items fall on different sides of a category threshold.",
      "batch_allocation": 600,
      "information_types": [
        {
          "type_id": "regulatory_classification",
          "type_description": "Classification decisions where a specific factual attribute determines which regulatory category an entity falls into, which then determines the complete set of applicable rules.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Regulatory subsumption - specific facts instantiate legal categories, and category membership determines the full set of applicable obligations. The category determines the rules, not the other way around.",
            "structure": "sentence_A (specific entity with concrete classifying attribute) → sentence_B (regulatory category that the specific attribute places the entity in) → sentence_C (set of obligations that applies specifically to entities in that category)",
            "example": "'This drone weighs 249 grams and is operated commercially within visual line of sight at altitudes below 400 feet.' → 'At 249 grams and commercial use, this drone falls into the FAA Part 107 regulated category rather than the recreational exemption, which requires aircraft to remain under 250 grams for non-registration.' → 'Part 107 operators must pass an aeronautical knowledge test, register the aircraft, display the registration number, and apply for waivers before flying in controlled airspace or at night.'",
            "why_asymmetric": "B is the classification determination that follows from A's specific attributes. Without B, C's obligations cannot be known. Note: if the drone were 250 grams instead of 249, it crosses the registration threshold - showing how classification is threshold-dependent. Reversed: knowing Part 107 requirements exist tells you nothing about what specific drone attributes trigger them.",
            "real_world_application": "Regulatory compliance, product launch legal review, import/export classification, business licensing"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (attribute that places entity just inside category boundary) ↔ sentence_Y (attribute that places similar entity just outside the same boundary, with different obligations)",
            "example": "'A drone weighing 249 grams used commercially requires FAA Part 107 certification but does not require registration, falling in the lightest regulated commercial category.' ↔ 'A drone weighing 251 grams used commercially requires both Part 107 certification and registration, with the registration number visibly displayed, because it crosses the 250-gram threshold.'",
            "why_symmetric": "X and Y describe entities on opposite sides of the same regulatory boundary. Each makes the other meaningful by showing what the two-gram difference in weight costs in compliance obligations."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same regulatory name, same weight threshold, or same product category but provide market data or agency history instead of classification chains. The critical close negative is a near-identical entity on the wrong side of the threshold.",
            "examples": [
              "CLOSE BOUNDARY: 'This drone weighs 252 grams and is operated recreationally in an uncontrolled rural area.' (near-identical surface, different classification trajectory, zero utility for understanding the 249-gram commercial case)",
              "CLOSE: 'The FAA received over 860,000 drone registrations in the first three years of its UAS registration program.' (same agency, aggregate statistic, zero classification chain value)",
              "DISTANT: 'Autonomous vehicle regulation is handled at the state level in the United States with no current federal classification framework for consumer vehicles.'"
            ],
            "why_negative": "The boundary near-miss is the most important hard negative: near-identical but crosses the threshold in the other direction. The model must score it very low despite identical vocabulary."
          },
          "variation_parameters": {
            "regulatory_domain": {
              "values": ["aviation", "food and drug", "financial products", "data privacy", "employment law", "environmental compliance"],
              "why_this_varies": "Different regulatory domains have different classification triggers, threshold structures, and consequence vocabularies"
            },
            "attribute_type": {
              "values": ["weight or size threshold", "financial value threshold", "use-type determination", "entity size threshold", "compositional attribute"],
              "why_this_varies": "Different attribute types create different classification logic and different hard negative structures"
            },
            "consequence_severity": {
              "values": ["administrative registration", "professional certification required", "operational restriction", "criminal liability threshold"],
              "why_this_varies": "Consequence severity affects C sentence structure and makes the classification threshold more or less significant"
            }
          },
          "combination_space": 270,
          "notes": "The close-boundary hard negative is the key test. Always include one near-identical entity that differs only in the threshold-determining attribute."
        },
        {
          "type_id": "functional_equivalence_grouping",
          "type_description": "Cases where structurally different entities belong to the same functional category because they perform the same role, which determines what rules and analysis apply to them.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Functional category membership - entities that look different may belong to the same category if they perform the same function. The function determines the applicable rules regardless of surface form.",
            "structure": "sentence_A (specific entity with described function) → sentence_B (functional category that includes entities performing that function regardless of surface form) → sentence_C (rule or analysis framework applicable to all members of the functional category)",
            "example": "'The company pays its delivery workers per parcel delivered, sets their routes and delivery windows, prohibits them from working for competitors, and provides the uniforms they wear.' → 'Despite being contracted as independent contractors, these workers function as employees under the economic realities test, which classifies based on actual working conditions rather than the contractual label.' → 'Workers meeting the employee definition under the economic realities test are entitled to minimum wage, overtime protections, and employer payroll tax contributions regardless of what their contracts call them.'",
            "why_asymmetric": "B is the classification determination that follows from A's described working conditions. Without B, C's employment protections cannot be known. The surface label says contractor but the function says employee. Reversed: knowing employment protections exist tells you nothing about what working conditions triggered the reclassification.",
            "real_world_application": "Employment law, antitrust analysis, tax classification, insurance categorization, regulatory arbitrage detection"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (surface form of entity) ↔ sentence_Y (the functional characteristic that determines its category membership regardless of surface form)",
            "example": "'A financial instrument is called a bond when issued by corporations or governments, a note when issued by the US Treasury at specific maturities, and a debenture when unsecured by specific assets.' ↔ 'All three instruments function as debt obligations where the issuer promises to make specified payments to holders, placing them in the same debt security category for regulatory and accounting purposes despite different names.'",
            "why_symmetric": "X enumerates the surface variants; Y explains the functional identity that groups them. Each makes the other complete as an explanation of why different names do not mean different categories."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives describe entities from the same surface domain that genuinely belong to a different functional category despite sharing vocabulary.",
            "examples": [
              "CLOSE: 'The company pays its delivery workers an annual salary, provides them with benefits, and they work fixed hours at the company warehouse sorting packages.' (same delivery domain, but these workers are employees by surface form too - no reclassification issue, zero functional equivalence chain value)",
              "CLOSE: 'Independent contractor arrangements are common in the gig economy and cover approximately 15 percent of the US workforce.' (same domain, aggregate statistic, zero functional classification chain value)",
              "DISTANT: 'Partnership agreements define the governance structure and profit sharing arrangements between business co-owners.'"
            ],
            "why_negative": "Entities that are employees by surface form don't illustrate functional reclassification. The point is entities that appear to be one category but function as another."
          },
          "variation_parameters": {
            "classification_system": {
              "values": ["employment status", "securities type", "tax entity type", "insurance category", "antitrust market definition"],
              "why_this_varies": "Different classification systems have different functional tests and different surface-form versus function tensions"
            },
            "surface_label": {
              "values": ["contractor vs employee", "loan vs equity", "product vs service", "employee vs partner", "domestic vs export"],
              "why_this_varies": "Different surface labels create different tensions between the label and the functional determination"
            },
            "jurisdiction": {
              "values": ["US federal", "EU", "UK", "California specifically", "international"],
              "why_this_varies": "Different jurisdictions use different functional tests for the same classification question"
            }
          },
          "combination_space": 270,
          "notes": "The tension between surface form and functional category is the core teaching signal. If there is no tension, the chain does not teach functional classification."
        },
        {
          "type_id": "prototype_versus_edge_case",
          "type_description": "Category membership tests where a prototype clearly belongs to the category, and an edge case shares all surface features but differs in one critical attribute that may exclude it.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Prototype theory with graded membership - categories have central members and peripheral edge cases. Specific instances imply the category, but the category does not imply the same rules apply to all members.",
            "structure": "sentence_A (prototype instance that clearly belongs to category) → sentence_B (the defining feature that places A in the category) → sentence_C (edge case that shares A's surface features but lacks the defining feature, showing the category boundary)",
            "example": "'A robin is a small bird with a red breast that builds nests, lays eggs, and raises young, and is the prototypical example of a bird.' → 'The defining features that place the robin in the bird category are its feathers, warm blood, and vertebrate structure - not its ability to fly, which is common but not definitional.' → 'The penguin shares every defining bird feature - feathers, warm blood, vertebrate - but cannot fly, demonstrating that flight is a typical bird attribute but not a defining one, which is why penguins are birds despite the intuitive conflict.'",
            "why_asymmetric": "B reveals which features are definitional (not flight), making C coherent when it presents a non-flying bird. Without B's definitional clarification, C's claim that penguins are birds seems to violate the prototype. Reversed: knowing penguins are birds tells you nothing about which features B must clarify to make that classification hold.",
            "real_world_application": "Linguistics, cognitive science, legal classification, AI ontology design, taxonomy building"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (necessary and sufficient defining features of a category) ↔ sentence_Y (common but non-defining features that create prototype intuitions about the category)",
            "example": "'The legally necessary and sufficient criteria for a document to constitute a contract are offer, acceptance, consideration, and mutual assent by parties with legal capacity.' ↔ 'Most contracts people encounter in daily life are written, signed, dated, and witnessed - features that are common but legally irrelevant, because an oral agreement satisfying the four criteria is equally binding.'",
            "why_symmetric": "X specifies what legally matters; Y specifies what people commonly but erroneously believe matters. Each makes the other necessary for understanding why prototype intuitions mislead in legal classification."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives are examples from the same category that are also prototypical members, sharing all features with A including the non-definitional ones, providing no category boundary information.",
            "examples": [
              "CLOSE: 'A sparrow is a small brown bird that builds cup-shaped nests, lays clutches of four to six eggs, and is one of the most common birds in suburban environments.' (same category, another prototype, zero category boundary teaching value)",
              "CLOSE: 'Birds evolved from a lineage of theropod dinosaurs approximately 150 million years ago, with Archaeopteryx often cited as a transitional form.' (same category, evolutionary history, zero prototype-edge-case chain value)",
              "DISTANT: 'Bats are the only mammals capable of sustained flight but are classified as mammals, not birds, because they lack feathers and are warm-blooded with fur.'"
            ],
            "why_negative": "Another prototype member adds nothing to understanding the category boundary. The edge case is the teaching signal, not more prototype examples."
          },
          "variation_parameters": {
            "category_domain": {
              "values": ["biological taxonomy", "legal categories", "linguistic categories", "software design patterns", "economic categories"],
              "why_this_varies": "Different domains have different defining versus typical feature structures and different edge cases"
            },
            "definitional_feature_type": {
              "values": ["structural", "functional", "historical", "relational", "intentional"],
              "why_this_varies": "Different feature types create different edge case structures"
            },
            "prototype_distance": {
              "values": ["clear prototype", "intermediate member", "extreme edge case that still qualifies", "looks like member but is excluded"],
              "why_this_varies": "Greater distance from prototype creates stronger teaching signal about where the boundary is"
            }
          },
          "combination_space": 360,
          "notes": "The edge case in C must be surprising - if it is obvious that the edge case belongs, the prototype-edge-case tension is lost."
        },
        {
          "type_id": "negative_definition_by_exclusion",
          "type_description": "Category definitions that are most clearly understood by what they exclude rather than what they include. The exclusion cases are specific instances that share all apparent features but lack the category-defining attribute.",
          "batch_count": 150,
          "asymmetric_pattern": {
            "asymmetry_type": "SEMANTIC",
            "linguistic_principle": "Contrastive definition - some categories are best defined by their exclusion conditions. The boundary is sharper when characterized by specific excluded instances than by positive membership criteria alone.",
            "structure": "sentence_A (positive definition of category with stated membership criteria) → sentence_B (specific instance that appears to qualify but is explicitly excluded, with reason) → sentence_C (implication of the exclusion for how the category is applied in practice)",
            "example": "'A trade secret is any information that has economic value from not being generally known and is subject to reasonable steps to maintain its secrecy, qualifying for legal protection under trade secret law.' → 'A company's customer list maintained on an unlocked shared drive that all employees and some contractors can access does not qualify as a trade secret, because the failure to take reasonable security steps negates the secrecy requirement regardless of the list's economic value.' → 'Courts require companies to demonstrate specific, documented security measures - access controls, non-disclosure agreements, and need-to-know restrictions - before extending trade secret protection, meaning the protection must be actively maintained rather than passively assumed.'",
            "why_asymmetric": "B reveals the specific exclusion condition that A's positive definition implied but did not make concrete. Without B, C's court requirements are unmotivated. Reversed: knowing courts require documented security measures tells you nothing about what the positive definition included that B's example violated.",
            "real_world_application": "Legal education, compliance training, IP portfolio management, risk assessment"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (what the category includes) ↔ sentence_Y (what the category excludes that might be expected to qualify)",
            "example": "'Trade secret protection covers formulas, patterns, compilations, programs, devices, methods, techniques, or processes that derive independent economic value from secrecy.' ↔ 'Trade secret law does not protect information that is independently developed by a competitor, reverse-engineered from a lawfully obtained product, or obtained from a public disclosure - only misappropriation is prohibited.'",
            "why_symmetric": "X describes the positive scope; Y describes the negative scope. Together they define the complete boundary of the category, each making the other more precise."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same legal term, same business context, or same information type vocabulary but provide case citation history or industry practice data instead of definitional exclusion chains.",
            "examples": [
              "CLOSE: 'Trade secret litigation increased by 30 percent in the five years following the passage of the Defend Trade Secrets Act in 2016.' (same legal domain, litigation statistic, zero definitional chain value)",
              "CLOSE: 'The Coca-Cola formula is often cited as the most famous trade secret in the world and has been maintained for over 130 years.' (same category, famous example, zero exclusion chain value)",
              "DISTANT: 'Patents provide time-limited exclusive rights in exchange for public disclosure, offering a different protection mechanism than trade secrets.'"
            ],
            "why_negative": "Litigation statistics and famous examples share trade secret vocabulary but provide no definitional exclusion teaching."
          },
          "variation_parameters": {
            "category_domain": {
              "values": ["intellectual property", "constitutional rights", "insurance coverage", "nonprofit tax exemption", "academic integrity"],
              "why_this_varies": "Different domains have different exclusion logics and different consequences for failing to meet the definitional criteria"
            },
            "exclusion_reason": {
              "values": ["missing necessary condition", "presence of disqualifying feature", "threshold not met", "wrong actor type", "timing constraint violated"],
              "why_this_varies": "Different exclusion reasons create structurally different B sentences"
            },
            "practical_implication": {
              "values": ["affirmative steps required", "periodic re-qualification needed", "third-party certification required", "documentation burden"],
              "why_this_varies": "Different implications for the C sentence create different levels of specificity in what the category requires in practice"
            }
          },
          "combination_space": 270,
          "notes": "The excluded instance in B must look like it qualifies - if the exclusion is obvious, the definitional boundary is not interesting. The surprise of the exclusion is the teaching signal."
        }
      ]
    },
    {
      "domain": "DIRECTIONAL_KNOWLEDGE_TRANSFER",
      "domain_description": "Asymmetric information transfer from question or need to answer or provision. Teaches QUERY-RESPONSE asymmetry through diverse question types: comparative, counterfactual, diagnostic, and explanatory. The answer derives its utility entirely from the question that preceded it.",
      "batch_allocation": 500,
      "information_types": [
        {
          "type_id": "comparative_evaluation_query",
          "type_description": "Questions asking which of two or more options is better under specific conditions, where the answer is directional: B tells you which option to choose given the conditions in A, but the recommendation does not make sense without those conditions.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Conditional recommendation - the answer to a comparative question is only valid under the conditions specified in the question. Removing the conditions makes the recommendation incoherent.",
            "structure": "sentence_A (comparative question with specific conditions that determine the answer) → sentence_B (recommendation calibrated to those specific conditions) → sentence_C (explanation of why those conditions make the recommendation correct rather than the alternative)",
            "example": "'Should I use a relational database or a document store for an application where each user has a profile with highly variable nested data and the access pattern is almost exclusively profile lookups by user ID?' → 'Given that the data structure is variable and nested and the access pattern is a single-key lookup, a document store like MongoDB is the better choice for this specific application.' → 'Relational databases excel when data has a fixed schema and queries join multiple tables, but variable nested structures with single-key lookups eliminate the joins that justify relational overhead, making the document model both simpler and faster for this pattern.'",
            "why_asymmetric": "B is the recommendation only given A's specific conditions. Without A's variable schema and single-key lookup specification, the answer would be different. C explains why A's conditions make B correct rather than the alternative. Reversed: knowing document stores are recommended for some use case tells you nothing about what access pattern and data structure prompted the recommendation.",
            "real_world_application": "Technical consultation, procurement decision support, comparative buying guides, clinical treatment selection"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (conditions that favor option A) ↔ sentence_Y (conditions that favor option B)",
            "example": "'Relational databases are preferable when data has a fixed schema, relationships between entities must be queried across tables, and transactional consistency is required.' ↔ 'Document databases are preferable when data structure varies across instances, access patterns are primarily by document key, and horizontal scaling is needed before transactional complexity.'",
            "why_symmetric": "X and Y together define when each option wins. Each makes the other complete as a decision guide, and neither is derivable from the other alone."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives describe the same technology options with the same vocabulary but provide general feature descriptions rather than condition-specific recommendations.",
            "examples": [
              "CLOSE: 'MongoDB is a document-oriented database that stores data in flexible JSON-like documents and supports horizontal sharding for scale.' (same technology, general description, does not answer the specific question with its specific conditions)",
              "CLOSE: 'The relational database market is dominated by PostgreSQL, MySQL, and Oracle, which together hold approximately 70 percent of enterprise database deployments.' (same domain, market fact, zero comparative evaluation value)",
              "DISTANT: 'Event sourcing stores state changes as an immutable log of events rather than the current state, making it suitable for audit-heavy domains.'"
            ],
            "why_negative": "Technology feature descriptions and market share data share database vocabulary but do not answer any specific comparative question."
          },
          "variation_parameters": {
            "comparison_domain": {
              "values": ["technology stack", "treatment options", "financial instruments", "communication channels", "supply chain strategies"],
              "why_this_varies": "Different comparison domains have different condition types and different recommendation vocabularies"
            },
            "condition_type": {
              "values": ["scale requirement", "structure constraint", "regulatory requirement", "skill constraint", "cost constraint", "time constraint"],
              "why_this_varies": "Different condition types change which option wins, creating genuine variation in B"
            },
            "option_count": {
              "values": ["binary choice", "three options", "ranked list of four"],
              "why_this_varies": "More options create more complex recommendation structures and harder negative cases"
            }
          },
          "combination_space": 270,
          "notes": "The conditions in A must be specific enough that changing them would change the recommendation. Vague conditions weaken the directional dependency."
        },
        {
          "type_id": "counterfactual_consequence_query",
          "type_description": "Questions about what would have happened if a specific condition were different, where the answer traces the causal chain from the changed condition to the different outcome.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Counterfactual analysis - the answer to a counterfactual traces a causal chain from a hypothetical change to its consequences. The chain is specific to the changed condition and meaningless without it.",
            "structure": "sentence_A (counterfactual question specifying what was different and asking what would have changed) → sentence_B (first consequence of the changed condition, traced causally) → sentence_C (downstream consequence that follows from B, completing the counterfactual chain)",
            "example": "'What would have happened to the Apollo 13 mission if the oxygen tank had not exploded on April 13, 1970?' → 'Without the tank explosion, the mission would have continued its planned trajectory toward a Fra Mauro highlands landing, which was completed instead by Apollo 14 nine months later.' → 'The Fra Mauro landing would have provided the mission's primary scientific contribution, validating or refuting the hypothesis that the samples would show volcanic activity from deep within the lunar mantle, and NASA's confidence in the CM life support systems would have remained unquestioned until later revealed vulnerabilities were discovered.'",
            "why_asymmetric": "B only traces a chain from A's specific changed condition (no explosion). C follows from B's specific continuation (Fra Mauro landing). Without A's specific counterfactual condition, B is a description of Apollo 14 rather than a counterfactual. Reversed: knowing the Fra Mauro scientific objectives tells you nothing about what counterfactual question prompted the analysis.",
            "real_world_application": "Historical analysis, policy counterfactual evaluation, risk assessment, academic historical writing, policy impact modeling"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (the actual historical decision and its outcome) ↔ sentence_Y (the alternative decision that was available and what it would have produced)",
            "example": "'The decision to introduce austerity policies in response to the 2008 financial crisis reduced public deficits in the short term but slowed economic recovery in countries that implemented them most severely.' ↔ 'Countries that maintained higher public spending levels during the crisis recovered to pre-crisis employment levels two to three years faster than those that implemented steep austerity, suggesting the fiscal multiplier favored stimulus in a liquidity trap environment.'",
            "why_symmetric": "X and Y present two actual policy paths with documented outcomes. Each makes the other a genuine comparison by providing the counterfactual baseline."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same event, same historical figures, or same dates but provide factual descriptions of what actually happened rather than counterfactual chains.",
            "examples": [
              "CLOSE: 'Apollo 13 launched on April 11, 1970, and the oxygen tank explosion occurred approximately 56 hours into the flight, forcing mission abort and astronaut rescue.' (same mission, what actually happened, zero counterfactual chain value)",
              "CLOSE: 'The Apollo program included six successful lunar landings between 1969 and 1972, with Apollo 13 being the only mission that did not reach the lunar surface.' (same program, historical summary, zero counterfactual analysis value)",
              "DISTANT: 'Simulation-based risk assessment models the consequences of component failures before flight to inform contingency planning.'"
            ],
            "why_negative": "Historical facts about what actually happened share Apollo vocabulary but do not trace any counterfactual chain."
          },
          "variation_parameters": {
            "counterfactual_domain": {
              "values": ["historical events", "policy decisions", "business decisions", "scientific discoveries", "technological development"],
              "why_this_varies": "Different domains have different counterfactual chain structures and different consequences"
            },
            "change_type": {
              "values": ["one decision changes", "one actor absent", "one event does not occur", "timing changes", "technology not available"],
              "why_this_varies": "Different change types produce structurally different counterfactual chains"
            },
            "chain_length": {
              "values": ["immediate consequence only", "one indirect consequence", "long-term systemic consequence"],
              "why_this_varies": "Longer chains test whether the model tracks causal dependency across multiple inferential steps"
            }
          },
          "combination_space": 270,
          "notes": "The counterfactual condition in A must be specific and single - changing multiple things simultaneously dilutes the directional dependency."
        },
        {
          "type_id": "diagnostic_symptom_query",
          "type_description": "Questions about what a specific symptom pattern indicates, where the answer identifies the condition and the explanation describes the mechanism connecting symptom to condition.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Abductive inference from symptom to cause - the question specifies a symptom pattern and the answer identifies the condition that best explains the full pattern. The answer is only the correct answer given all symptoms in A.",
            "structure": "sentence_A (symptom pattern with multiple specific observations) → sentence_B (condition that the symptom pattern most specifically indicates) → sentence_C (mechanism connecting each symptom in A to the condition identified in B)",
            "example": "'A houseplant has yellowing leaves that start at the bottom and progress upward, thin spindly new growth leaning toward the window, and pale green rather than deep green color in healthy-looking leaves.' → 'This combination of upward-progressing chlorosis, etiolation, and overall paleness indicates nitrogen deficiency combined with insufficient light, which interact to produce this specific set of symptoms together.' → 'Nitrogen deficiency causes old leaves to yellow first as the plant mobilizes nitrogen to new growth, while insufficient light causes etiolation and reduces chlorophyll density, explaining why symptoms appear throughout the plant rather than just in old or new tissue.'",
            "why_asymmetric": "B identifies the condition that explains the complete symptom pattern in A. Without A's specific symptom combination (upward progression plus etiolation plus paleness together), B would be wrong - nitrogen deficiency alone causes downward progression, and light deficiency alone causes etiolation without yellowing. Reversed: knowing nitrogen deficiency causes upward chlorosis tells you nothing about what symptom pattern prompted the query.",
            "real_world_application": "Plant care guides, medical differential diagnosis training, mechanical troubleshooting, IT network diagnostics"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (symptom that appears in multiple conditions) ↔ sentence_Y (the differentiating symptom that distinguishes between conditions producing X)",
            "example": "'Both nitrogen deficiency and iron deficiency cause leaf yellowing, making chlorosis alone insufficient to determine which nutrient is deficient.' ↔ 'Nitrogen deficiency yellows old leaves first while new leaves remain green, whereas iron deficiency yellows new leaves first while old leaves remain green, making the pattern of progression the diagnostic differentiator.'",
            "why_symmetric": "X explains why a single symptom is diagnostically ambiguous; Y explains exactly what additional observation resolves the ambiguity. Each makes the other actionable for someone trying to diagnose a yellowing plant."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same symptom vocabulary or same plant/system type but provide general care information or species facts instead of diagnostic chains.",
            "examples": [
              "CLOSE: 'Most houseplants require watering when the top inch of soil is dry and benefit from monthly fertilization during the growing season.' (same domain, general care advice, does not address the specific symptom pattern)",
              "CLOSE: 'Pothos plants are among the most common houseplants due to their tolerance for low light and irregular watering.' (same context, species fact, zero diagnostic chain value)",
              "DISTANT: 'Hydroponic growing systems deliver nutrients directly to roots through water, allowing precise control of nutrient concentrations.'"
            ],
            "why_negative": "General care advice and species facts share houseplant vocabulary but do not diagnose any specific symptom pattern."
          },
          "variation_parameters": {
            "symptom_domain": {
              "values": ["plant care", "mechanical systems", "software performance", "organizational health", "network infrastructure"],
              "why_this_varies": "Different symptom domains have different symptom vocabularies and different differential diagnosis structures"
            },
            "symptom_count": {
              "values": ["single symptom", "two correlated symptoms", "three or more symptoms forming a pattern"],
              "why_this_varies": "More symptoms create a more specific diagnosis and a harder hard negative (wrong combination)"
            },
            "condition_uniqueness": {
              "values": ["unique to one condition", "shared by two conditions with differentiator", "common symptom requiring additional testing"],
              "why_this_varies": "Condition uniqueness affects how confident and specific the answer in B can be"
            }
          },
          "combination_space": 270,
          "notes": "The symptom pattern in A must be specific enough that the combination points to a unique or near-unique diagnosis. Generic symptoms reduce the directional dependency."
        },
        {
          "type_id": "mechanism_explanation_query",
          "type_description": "Questions asking how something works at a mechanistic level, where the answer describes the mechanism step by step and the elaboration explains why each step is necessary.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "QUERY-RESPONSE",
            "linguistic_principle": "Mechanistic explanation - a how question creates a deficit for understanding process. The mechanism is only the correct answer given the specific process asked about.",
            "structure": "sentence_A (how question about a specific process with a specific asking perspective) → sentence_B (the mechanism described at the level of abstraction the question implies) → sentence_C (explanation of the rate-limiting or critical step in the mechanism that determines overall behavior)",
            "example": "'How does the immune system distinguish its own cells from foreign cells to know which to attack and which to leave alone?' → 'Every cell in the body displays protein fragments from its internal activity on its surface using MHC molecules, and T-cells patrol the body checking these displays against a learned pattern of what self-proteins look like.' → 'T-cells that react to self-proteins are eliminated during development in the thymus - a process called negative selection - meaning the surviving T-cell population has been specifically filtered to ignore normal self-displays, so only abnormal or foreign protein displays trigger an attack.'",
            "why_asymmetric": "B answers A's specific question at the right level of abstraction (MHC display and T-cell patrol). Without A's question, B is an immunology fact. C identifies negative selection as the critical step, which is only meaningful given B established the display-and-check mechanism. Reversed: knowing about thymic selection tells you nothing about what self-nonself discrimination question prompted the explanation.",
            "real_world_application": "Science education, medical training, technical documentation, engineering onboarding, popular science writing"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (one component of a mechanism) ↔ sentence_Y (the complementary component without which X cannot function)",
            "example": "'MHC molecules on the surface of infected cells display peptide fragments of viral proteins that are being produced inside the cell.' ↔ 'T-cell receptors are specifically shaped during development to recognize the combination of a particular MHC molecule plus a foreign peptide, requiring both components to be simultaneously present for activation.'",
            "why_symmetric": "X describes the presenting side of the mechanism; Y describes the recognizing side. Neither can function without the other, and each makes the other's role comprehensible."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same biological terms, same cell types, or same disease names but provide discovery history, prevalence statistics, or drug mechanism instead of the specific self-nonself mechanism.",
            "examples": [
              "CLOSE: 'The immune system was first described in modern cellular terms by Elie Metchnikoff in the 1880s with his discovery of phagocytosis in starfish larvae.' (same system, historical attribution, zero mechanism chain value)",
              "CLOSE: 'Autoimmune diseases occur when the immune system incorrectly attacks the body's own tissues, affecting approximately 50 million Americans.' (same system, epidemiology, zero mechanism explanation value)",
              "DISTANT: 'mRNA vaccines train the immune system by instructing cells to produce a specific viral protein that the immune system then learns to recognize.'"
            ],
            "why_negative": "Discovery history and autoimmune disease statistics share immune system vocabulary but provide no mechanistic explanation of self-nonself discrimination."
          },
          "variation_parameters": {
            "mechanism_domain": {
              "values": ["immunology", "cryptography", "financial clearing", "memory consolidation", "chemical catalysis", "voting systems"],
              "why_this_varies": "Diverse mechanism domains prevent the model from learning immune system patterns rather than mechanism explanation patterns"
            },
            "abstraction_level": {
              "values": ["molecular", "cellular", "systems", "population", "conceptual"],
              "why_this_varies": "Different abstraction levels require different vocabularies and different levels of prior knowledge assumed in A"
            },
            "mechanism_complexity": {
              "values": ["single-step", "two-stage", "feedback loop", "cascade", "error-correction"],
              "why_this_varies": "Different complexity levels create different B and C structures and different hard negative opportunities"
            }
          },
          "combination_space": 270,
          "notes": "The level of abstraction in A's question must match the level in B's answer. If A asks a lay question, B must not answer at molecular detail. Level mismatch creates a weak A→B dependency."
        }
      ]
    },
    {
      "domain": "EPISTEMIC_OPPOSITION",
      "domain_description": "Adversarial knowledge relationships where B is topically maximally related to A but contradicts, undermines, or conflicts with it. Teaches the model that topical density and lexical overlap do not determine utility when the relationship is oppositional. This domain fixes the model's complete blindness to contradiction identified in Tests 1, 3, and 7.",
      "batch_allocation": 500,
      "information_types": [
        {
          "type_id": "empirical_rebuttal",
          "type_description": "A specific empirical claim is directly contradicted by specific empirical evidence. Both sentences reference the same phenomenon with near-identical vocabulary, but B shows A is false.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CONTRADICTORY",
            "linguistic_principle": "Empirical falsification - a claim and the evidence that falsifies it are maximally topically related but the relationship is one of opposition, not elaboration. High lexical overlap with direct negation = LOW utility.",
            "structure": "sentence_A (empirical claim) → sentence_B (specific evidence that directly contradicts A's claim with the same vocabulary) → sentence_C (explanation of why A was believed and what the correct understanding now is)",
            "example": "'Eating dietary fat directly causes fat accumulation in the body, which is why low-fat diets became the dominant recommendation for weight loss in the 1980s.' → 'Randomized controlled trials comparing low-fat and low-carbohydrate diets consistently show that fat intake does not directly determine body fat accumulation, and low-fat diets produce no better weight loss outcomes than higher-fat alternatives.' → 'Body fat accumulation is determined primarily by total caloric balance and insulin signaling rather than dietary fat percentage, and the low-fat hypothesis arose from observational studies that confounded fat intake with overall caloric restriction.'",
            "why_asymmetric": "B uses the same vocabulary (fat, diet, accumulation, weight loss) as A but directly contradicts its core claim. A→B scores LOW because B does not help you apply A; it tells you A is wrong. C provides the corrected understanding. SCORING: A→B should be 0.1-0.2 despite maximum relevance.",
            "real_world_application": "Scientific retraction context, health journalism correction, evidence-based medicine, systematic review methodology"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (the false claim) ↔ sentence_Y (the true claim about the same phenomenon, which is not the negation of X but a different accurate statement)",
            "example": "'Dietary fat consumption is not the primary driver of cardiovascular disease risk based on current evidence.' ↔ 'Refined carbohydrate and sugar consumption, particularly fructose, shows stronger correlation with cardiovascular risk markers than dietary fat in recent large cohort studies.'",
            "why_symmetric": "X corrects the false claim; Y provides a positive true claim about what does drive the risk. Each makes the other more complete as a replacement for A's false model. Note: in EPISTEMIC_OPPOSITION, the symmetric pair demonstrates the correct picture, not mutual elaboration."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same dietary vocabulary and same health outcomes but address a different mechanism that neither supports nor contradicts A.",
            "examples": [
              "CLOSE: 'The Mediterranean diet, which includes moderate amounts of healthy fats from olive oil and fish, is associated with reduced cardiovascular events in prospective studies.' (same domain, neither contradicts nor supports A's fat claim, nutritional context)",
              "CLOSE: 'The dietary fat hypothesis was promoted by nutritionist Ancel Keys, whose Seven Countries Study selected countries that supported his hypothesis while excluding contradictory data.' (same hypothesis, origin story, zero empirical contradiction value)",
              "DISTANT: 'Gut microbiome composition influences metabolic processing of nutrients, potentially explaining individual variation in response to the same diet.'"
            ],
            "why_negative": "Mediterranean diet studies and hypothesis history share dietary fat vocabulary but neither directly contradict A's specific claim nor provide the contradicting evidence B provides."
          },
          "variation_parameters": {
            "claim_domain": {
              "values": ["nutrition science", "pharmacology", "psychology", "economics", "physics", "epidemiology"],
              "why_this_varies": "Different domains have different types of empirical evidence and different false-claim vocabularies"
            },
            "contradiction_strength": {
              "values": ["single study contradicts", "meta-analysis contradicts", "multiple lines of evidence converge on contradiction", "claim was never tested and assumed"],
              "why_this_varies": "Contradiction strength affects the confidence of B's negation and the structure of C's explanation"
            },
            "persistence_of_false_claim": {
              "values": ["quickly corrected", "persisted for decades", "still widely believed despite evidence", "recently corrected"],
              "why_this_varies": "Persistence affects how C must explain why the false belief continued despite B's evidence"
            }
          },
          "combination_space": 252,
          "notes": "CRITICAL SCORING: A→B = 0.1-0.2 despite maximum lexical overlap. Include contradiction_low_utility flag in batch metadata. This is the primary fix for Tests 1 and 3."
        },
        {
          "type_id": "quantifier_scope_conflict",
          "type_description": "Two claims about the same phenomenon that conflict via quantifier scope - one claims universal applicability and the other demonstrates existential exception. The existence of even one exception falsifies universal claims.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CONTRADICTORY",
            "linguistic_principle": "Quantifier asymmetry in falsification - a universal claim is falsified by a single counterexample, but an existential claim cannot be falsified by showing the universal does not hold. One exception makes 'always' false; many confirmations do not make 'never' true.",
            "structure": "sentence_A (universal or near-universal claim about a phenomenon) → sentence_B (specific counterexample that demonstrates the exception, falsifying A as stated) → sentence_C (correct bounded claim that replaces A by specifying the conditions under which the tendency actually holds)",
            "example": "'Boiling water at 100 degrees Celsius is a universal physical law that applies to water everywhere.' → 'At the summit of Mount Everest, water boils at approximately 70 degrees Celsius due to reduced atmospheric pressure, directly contradicting the claim of universal applicability at 100 degrees.' → 'The correct statement is that water boils at 100 degrees Celsius specifically at 1 atmosphere of pressure, and the boiling point decreases predictably as pressure decreases, making the law conditional on pressure rather than universal.'",
            "why_asymmetric": "B directly falsifies A by providing a counterexample with the same vocabulary (water, boiling, degrees). A→B scores LOW because B undermines A rather than elaborating it. C provides the corrected bounded statement.",
            "real_world_application": "Scientific communication, policy debate fact-checking, logical reasoning training, statistics education"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (bounded true claim with specified conditions) ↔ sentence_Y (the complementary bounded claim that covers the conditions X excluded)",
            "example": "'Water boils at 100 degrees Celsius at sea level pressure and in its pure form without dissolved solutes.' ↔ 'Dissolved salts in water raise the boiling point by a predictable amount proportional to the concentration, which is why pasta water at culinary concentrations boils at approximately 100.5 degrees Celsius.'",
            "why_symmetric": "X specifies the baseline conditions; Y specifies how the boiling point shifts when the conditions change. Together they give a complete bounded account."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same phenomenon, same units, or same conditions but address a different property that does not contradict A's universal claim.",
            "examples": [
              "CLOSE: 'Water has a density of exactly 1 gram per cubic centimeter at 4 degrees Celsius, making it the historical basis for the metric system's definition of mass.' (same substance, different property, does not contradict boiling point claim)",
              "CLOSE: 'The specific heat capacity of water is unusually high compared to most substances, allowing it to absorb large amounts of heat with small temperature change.' (same substance, thermal property, does not address boiling point universality)",
              "DISTANT: 'Triple point conditions where water exists simultaneously as solid, liquid, and gas occur at exactly 0.01 degrees Celsius and 611.7 pascals.'"
            ],
            "why_negative": "Density and specific heat properties share water vocabulary but do not conflict with any claim about boiling temperature universality."
          },
          "variation_parameters": {
            "claim_form": {
              "values": ["always/never", "all/none", "universally", "in every case", "no exceptions"],
              "why_this_varies": "Different universal claim forms create different falsification structures for B"
            },
            "exception_type": {
              "values": ["extreme condition creates exception", "different context creates exception", "definition excludes the apparent exception", "scale creates exception"],
              "why_this_varies": "Different exception types create different C sentences - some correct A, some show A was definitionally imprecise"
            },
            "domain": {
              "values": ["physical science", "social science", "economics", "biology", "statistics"],
              "why_this_varies": "Different domains have different types of universal claims and different types of exceptions"
            }
          },
          "combination_space": 270,
          "notes": "The counterexample in B must use identical or near-identical vocabulary to A. The falsification must be surprising given A's claim."
        },
        {
          "type_id": "strategic_counterposition",
          "type_description": "Argumentative contexts where B presents a strategic or analytical counter to A's position that is maximally topically relevant but serves the opposing conclusion.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CONTRADICTORY",
            "linguistic_principle": "Argumentative relevance with opposing utility - the most relevant response to an argument is the strongest counter-argument. High relevance does not mean high utility for the original position.",
            "structure": "sentence_A (argument or recommendation for position P) → sentence_B (counter-argument that challenges P's premise or evidence using the same vocabulary) → sentence_C (third analytical perspective that evaluates the strength of each position)",
            "example": "'Remote work policies should be made permanent because employee satisfaction surveys show that 78 percent of workers prefer it, and productivity metrics have remained stable or improved in most organizations.' → 'Employee self-reports of productivity in remote settings systematically overestimate actual output because workers cannot observe their own coordination costs or the externalities they impose on colleagues who need spontaneous collaboration.' → 'The debate requires separating individual productivity metrics from organizational coordination efficiency, as policies optimizing for the former may degrade the latter in ways that only appear in long-run innovation output and team capability building.'',",
            "why_asymmetric": "B is maximally relevant to A - it directly challenges A's evidence (surveys and productivity metrics) using the same vocabulary. But B does not help you accept or implement A; it provides grounds for rejecting A's evidence. A→B scores LOW. C provides the analytical synthesis.",
            "real_world_application": "Policy debate, management consulting counter-analysis, academic peer review, strategic planning devil's advocate"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (argument for P) ↔ sentence_Y (argument for P from a different evidence base or angle that complements rather than contradicts X)",
            "example": "'Remote work reduces commute time by an average of 54 minutes per day per worker, providing a direct productivity and wellbeing benefit.' ↔ 'Remote work expands the available talent pool beyond commuting distance, allowing organizations to hire from the full geographic distribution of qualified candidates rather than those within 45 minutes of a specific office.'",
            "why_symmetric": "X and Y both support permanent remote work from different angles. Each adds independent value to the overall case without overlapping."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives use the same policy vocabulary, same statistics, or same organization vocabulary but provide implementation details rather than counter-arguments.",
            "examples": [
              "CLOSE: 'Most organizations implement remote work through a combination of video conferencing, asynchronous messaging platforms, and cloud document collaboration tools.' (same domain, implementation fact, zero counter-argument value)",
              "CLOSE: 'Employee satisfaction with remote work varies by role type, with knowledge workers reporting higher satisfaction than those in collaborative creative roles.' (same domain, nuance that partially qualifies A but does not challenge its core claim as B does)",
              "DISTANT: 'Office real estate costs represent approximately 10 percent of total operating expenses for knowledge-intensive businesses, making remote work policies financially significant.'"
            ],
            "why_negative": "Implementation facts and partial qualifications share remote work vocabulary but neither directly challenge A's core claim as B does nor provide strategic counter-analysis."
          },
          "variation_parameters": {
            "policy_domain": {
              "values": ["workplace policy", "public health intervention", "economic regulation", "technology platform governance", "educational policy"],
              "why_this_varies": "Different policy domains have different evidence types and different counter-argument structures"
            },
            "counter_argument_type": {
              "values": ["evidence quality challenge", "premise rejection", "unintended consequences", "alternative explanation of same data", "missing variable"],
              "why_this_varies": "Different counter-argument types attack different parts of A and require different C analytical frameworks"
            },
            "evidence_type_in_A": {
              "values": ["survey data", "controlled trial", "case study", "theoretical model", "expert consensus"],
              "why_this_varies": "Different evidence types have different vulnerabilities that B's counter can exploit"
            }
          },
          "combination_space": 270,
          "notes": "This directly fixes Test 7's ArguAna failure. B must score LOW (0.1-0.3) for A→B consistently regardless of vocabulary overlap. Include counter_argument_low_utility flag."
        },
        {
          "type_id": "incompatible_prescription",
          "type_description": "Two valid recommendations or guidelines that cannot both be followed simultaneously in the same situation. Tests whether the model detects operational conflict between individually valid prescriptions.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "CONTRADICTORY",
            "linguistic_principle": "Deontic conflict in the same action space - two normatively valid prescriptions that require incompatible actions cannot both be followed, making them operationally opposed despite each being individually correct.",
            "structure": "sentence_A (valid recommendation with specific scope) → sentence_B (equally valid recommendation with overlapping scope that conflicts with A's required action) → sentence_C (resolution principle that determines which prescription takes priority or how to reconcile them)",
            "example": "'Anesthesiologists should administer intravenous fluids liberally during abdominal surgery to maintain blood volume and prevent hypotension, typically 10 to 20 ml per kg per hour.' → 'Restrictive fluid management during abdominal surgery, with no more than 1 to 3 ml per kg per hour, reduces the risk of anastomotic leakage and pulmonary edema in bowel resection specifically.' → 'The prescriptions are both valid but for different patient subgroups: liberal fluid management applies to procedures without bowel anastomosis, while goal-directed restrictive management is indicated specifically for bowel resection, requiring the anesthesiologist to know the specific procedure being performed.'",
            "why_asymmetric": "B is maximally relevant to A because it addresses the same clinical action (IV fluid rate) with the same units and the same surgical context. But B prescribes the opposite action. A→B scores LOW because following B means violating A. C provides the disambiguation principle.",
            "real_world_application": "Clinical guideline reconciliation, regulatory conflict of laws, organizational policy conflict, financial regulation compliance"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (prescription valid in context C1) ↔ sentence_Y (prescription valid in context C2, where C1 and C2 are mutually exclusive in any given situation)",
            "example": "'In septic shock with suspected infection, empirical broad-spectrum antibiotics should be initiated within one hour of recognition to reduce mortality.' ↔ 'In patients with confirmed antibiotic resistance, empirical broad-spectrum coverage should be withheld until culture results allow targeted therapy, to prevent selection for further resistance.'",
            "why_symmetric": "X and Y are each correct in their specific contexts. Each makes the other meaningful by defining when it applies versus when the other takes precedence."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives are recommendations from the same clinical or regulatory domain that operate on different aspects of the situation and therefore do not conflict.",
            "examples": [
              "CLOSE: 'Anesthesiologists should monitor blood pressure continuously during abdominal surgery using an arterial line for accurate real-time readings.' (same surgical context, different clinical parameter, no conflict with fluid rate prescription)",
              "CLOSE: 'All surgical patients should receive prophylactic antibiotics within 60 minutes before incision to reduce surgical site infection rates.' (same patient population, different intervention, no conflict with fluid management)",
              "DISTANT: 'Postoperative pain management protocols should be multimodal, combining opioid and non-opioid analgesics to minimize total opioid dose.'"
            ],
            "why_negative": "Recommendations that address different clinical parameters in the same patient population share surgical vocabulary but do not create operational conflict with each other."
          },
          "variation_parameters": {
            "prescription_domain": {
              "values": ["clinical guidelines", "legal obligations", "financial regulation", "environmental compliance", "safety protocols"],
              "why_this_varies": "Different domains have different conflict resolution mechanisms and different priority principles"
            },
            "conflict_mechanism": {
              "values": ["opposite required actions", "resource competition", "timing conflict", "authority conflict", "scope overlap with different rule"],
              "why_this_varies": "Different conflict mechanisms require different C resolution structures"
            },
            "resolution_type": {
              "values": ["context determines which applies", "hierarchy resolves conflict", "specialist consultation required", "no established resolution"],
              "why_this_varies": "Different resolutions produce different C sentences with different actionability"
            }
          },
          "combination_space": 252,
          "notes": "The conflict must be real and operational, not just theoretical. If following A does not prevent following B, the prescriptions are not genuinely conflicting."
        }
      ]
    },
    {
      "domain": "LOGICAL_INFERENCE",
      "domain_description": "Strictly logical relationships where the truth of A guarantees or requires the truth of B in one direction only. Teaches the model to distinguish logical necessity from causal probability from topical association. Fixes entailment direction noise and specificity gradient absence identified in Tests 2 and 6.",
      "batch_allocation": 500,
      "information_types": [
        {
          "type_id": "necessary_condition_chain",
          "type_description": "Chains where each step is a necessary condition for the next - A is required for B to be possible, and B is required for C to be possible, making the chain logically ordered in one direction only.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "ENTAILMENT",
            "linguistic_principle": "Necessary condition ordering - if A is necessary for B, then B implies A was satisfied. But A's satisfaction does not guarantee B, only makes it possible. The implication runs from B to A, not A to B.",
            "structure": "sentence_A (precondition that is necessary but not sufficient for B) → sentence_B (event that requires A but adds additional necessary conditions) → sentence_C (event that requires B, making C dependent on A through B)",
            "example": "'A candidate must be a citizen of the country for at least 14 years to be constitutionally eligible for the presidency.' → 'Even meeting the citizenship requirement, a candidate must also win enough electoral votes in the general election to secure the presidency.' → 'Only upon winning the electoral college does the president-elect face the final step of surviving any challenges to the electoral certification before taking office.'",
            "why_asymmetric": "B implies A was satisfied - you cannot win the electoral vote without first being constitutionally eligible. But A does not imply B - millions of eligible citizens never run. C implies B was satisfied. SCORING: B→A HIGH (eligibility is necessarily implied by winning). A→B LOW (eligibility does not imply winning). This is the reverse of the intuitive utility direction.",
            "real_world_application": "Constitutional law, formal process verification, logic programming, prerequisite system design"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (necessary condition P) ↔ sentence_Y (another necessary condition Q that is co-required with P but independent of it)",
            "example": "'A valid will requires the testator to have been of sound mind at the time of signing, demonstrating capacity to understand what they own and who their heirs are.' ↔ 'A valid will also requires the signature to be witnessed by at least two people who are not beneficiaries, providing independent verification of the signing circumstances.'",
            "why_symmetric": "X and Y are both necessary conditions for will validity. Each is independently required and neither implies the other. Together they are mutually completing."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives describe the same process using the same vocabulary but are sufficient conditions rather than necessary ones, or are merely probable rather than certain.",
            "examples": [
              "CLOSE: 'Receiving the most votes in the popular vote across all states is typically, but not always, correlated with winning the electoral college.' (same election domain, probabilistic rather than logically necessary relationship with the outcome)",
              "CLOSE: 'Presidential inaugurations occur on January 20th following the election year, as established by the 20th Amendment.' (same process, timing fact, zero necessary condition chain value)",
              "DISTANT: 'Parliamentary systems determine the head of government differently, through majority coalition in the legislature rather than a separate executive election.'"
            ],
            "why_negative": "Probabilistic correlations and timing facts share electoral vocabulary but do not describe logical necessary conditions."
          },
          "variation_parameters": {
            "domain": {
              "values": ["legal process", "biological development", "software compilation", "academic progression", "financial transaction"],
              "why_this_varies": "Different domains have different necessary condition structures and different chain lengths"
            },
            "condition_type": {
              "values": ["constitutional requirement", "biological prerequisite", "technical dependency", "institutional requirement"],
              "why_this_varies": "Different condition types have different entailment strengths and different vocabulary"
            },
            "chain_length": {
              "values": ["two necessary conditions", "three necessary conditions", "four or more creating a full prerequisite chain"],
              "why_this_varies": "Longer chains create more complex entailment structures and more opportunities for partial scoring"
            }
          },
          "combination_space": 225,
          "notes": "CRITICAL SCORING: The entailment direction is from later in the chain to earlier (B implies A was satisfied), not the intuitive forward direction. This is the key difference from CAUSAL chains where A causes B."
        },
        {
          "type_id": "contrapositive_inference",
          "type_description": "Logical contrapositives where 'if A then B' implies 'if not B then not A'. The contrapositive has identical logical force to the original but opposite surface form, testing whether the model handles logical equivalence across negation.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "ENTAILMENT",
            "linguistic_principle": "Contrapositive equivalence - 'if A then B' is logically identical to 'if not B then not A'. Both have the same truth conditions despite surface negation.",
            "structure": "sentence_A (conditional statement in standard form) → sentence_B (contrapositive of A in negated form, logically equivalent) → sentence_C (application of either A or B to a specific case)",
            "example": "'If a chemical compound is soluble in water, it will disperse evenly throughout the water column rather than settling to the bottom.' → 'Equivalently, if a compound does not disperse evenly through the water column and instead settles to the bottom, it cannot be water-soluble.' → 'A forensic chemist observing a white powder settling to the bottom of a water sample can immediately conclude the powder is insoluble in water, without needing to measure solubility directly.'",
            "why_asymmetric": "A and B are logically equivalent - A→B scores HIGH and B→A scores HIGH because they have identical truth conditions. C is a one-directional application that only follows from the established principle. SCORING: A→B HIGH, B→A HIGH. C scores high from both A and B but A→C and B→C are asymmetric in their utility.",
            "real_world_application": "Logic education, mathematical proof technique, legal reasoning, detective reasoning, scientific inference"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (the conditional) ↔ sentence_Y (the contrapositive, which is logically equivalent)",
            "example": "'If a business entity is profitable, it generates more revenue than it spends on operations and debt service.' ↔ 'Any entity that does not generate more revenue than it spends on operations and debt service cannot be profitable by definition.'",
            "why_symmetric": "X and Y are logically equivalent - each implies the other with probability 1. This is one of the few genuinely symmetric cases where both directions score 1.0."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives are the inverse (not the contrapositive) which is a logical fallacy. 'If A then B' does NOT imply 'if not A then not B'.",
            "examples": [
              "CLOSE (FALLACIOUS INVERSE): 'If a compound is not water-soluble, it will not disperse evenly through water.' (this sounds like the contrapositive but is the inverse - a fallacy. A compound could be non-soluble AND disperse through suspension rather than settling, making this inference invalid)",
              "CLOSE: 'Water solubility is measured in grams of solute per 100 milliliters of solvent at a standard temperature of 25 degrees Celsius.' (same topic, measurement definition, zero contrapositive inference value)",
              "DISTANT: 'Chromatography separates compounds based on differential solubility in mobile and stationary phases.'"
            ],
            "why_negative": "The inverse fallacy looks exactly like the contrapositive but is logically invalid. Teaching the model to distinguish them is a critical logical reasoning signal."
          },
          "variation_parameters": {
            "conditional_domain": {
              "values": ["chemistry", "legal definition", "mathematical property", "biological condition", "economic rule"],
              "why_this_varies": "Different domains have different conditional structures and different application contexts"
            },
            "negation_form": {
              "values": ["explicit not", "absence marker", "opposite qualifier", "impossibility claim"],
              "why_this_varies": "Different negation forms test whether the model handles surface-form variation in contrapositives"
            },
            "application_specificity": {
              "values": ["abstract case", "concrete measurement", "real historical case", "hypothetical scenario"],
              "why_this_varies": "Application specificity in C affects how concretely the model must connect the logical principle to real inference"
            }
          },
          "combination_space": 225,
          "notes": "The fallacious inverse in the hard negatives is the most important teaching signal. The model must score the inverse low and the contrapositive high."
        },
        {
          "type_id": "transitive_implication",
          "type_description": "Chains where A implies B and B implies C, making A imply C by transitivity. Tests whether the model recognizes indirect entailment across multiple steps.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "ENTAILMENT",
            "linguistic_principle": "Transitivity of implication - if A entails B and B entails C, then A entails C. But C does not entail B, and B does not entail A, because the chain runs in one direction.",
            "structure": "sentence_A (specific claim that entails B) → sentence_B (intermediate claim that A entails and that itself entails C) → sentence_C (remote claim entailed by A through B)",
            "example": "'This corporation has been formally convicted of tax evasion by a federal court.' → 'A conviction for tax evasion constitutes a felony under federal law for the responsible officers.' → 'Individuals with federal felony convictions are prohibited from holding federal contractor status, meaning the corporation's officers cannot enter into new federal government contracts in their individual capacity.'",
            "why_asymmetric": "A entails B (conviction implies felony classification). B entails C (felony implies contractor prohibition). Therefore A entails C. But C does not entail B (many routes to contractor prohibition exist), and B does not entail A (felonies arise from many crimes, not just tax evasion). SCORING: A→B HIGH, B→C HIGH, A→C MODERATE (indirect entailment). C→A LOW, B→A LOW.",
            "real_world_application": "Legal reasoning, mathematical proof, logical argument evaluation, rule-based system design"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (sufficient condition for consequence R) ↔ sentence_Y (different sufficient condition for the same consequence R, independent of X)",
            "example": "'A federal felony conviction bars individuals from most security clearance applications under standard adjudicative guidelines.' ↔ 'A pattern of financial irresponsibility including multiple bankruptcies and unpaid judgments can also disqualify individuals from security clearance based on vulnerability to financial coercion.'",
            "why_symmetric": "X and Y are independent sufficient conditions for the same consequence (clearance disqualification). Each makes the other meaningful by showing the consequence has multiple independent triggers."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives break the transitivity chain by describing something entailed by C but not by A, or entailed by A but not transitively connected to C.",
            "examples": [
              "CLOSE: 'Federal contractors are required to maintain security protocols and undergo periodic audits of their compliance programs.' (federal contractor context, not entailed by A - corporation may still exist as a contractor entity even if officers are prohibited)",
              "CLOSE: 'Tax evasion investigations are conducted jointly by the IRS Criminal Investigation division and the Department of Justice Tax Division.' (same crime, procedural fact, no transitivity chain with contractor prohibition)",
              "DISTANT: 'Debarment proceedings are administrative actions separate from criminal prosecution that can also result in contractor exclusion.'"
            ],
            "why_negative": "Contractor compliance requirements and investigation procedures share vocabulary with the chain but do not participate in the A→B→C transitivity structure."
          },
          "variation_parameters": {
            "chain_domain": {
              "values": ["legal consequences", "biological processes", "software dependencies", "economic effects", "social network effects"],
              "why_this_varies": "Different domains have different transitivity structures and different chain vocabularies"
            },
            "chain_directness": {
              "values": ["one-hop indirect", "two-hop indirect", "three-hop indirect"],
              "why_this_varies": "More hops create weaker A→C entailment scores and test the model's handling of indirect implication"
            },
            "entailment_strength_at_each_step": {
              "values": ["both steps necessary", "first step necessary second probable", "both steps probable"],
              "why_this_varies": "Weaker individual steps create weaker transitivity and test the model's calibration of compounding uncertainty"
            }
          },
          "combination_space": 225,
          "notes": "A→C should score LOWER than A→B and B→C to reflect that indirect entailment is weaker than direct entailment. The model must calibrate to chain distance."
        },
        {
          "type_id": "universal_existential_boundary",
          "type_description": "The boundary between universal and existential claims and their logical relationships. Tests whether the model understands that existential claims do not reverse to universal claims.",
          "batch_count": 125,
          "asymmetric_pattern": {
            "asymmetry_type": "ENTAILMENT",
            "linguistic_principle": "Existential-universal asymmetry - a universal claim implies the corresponding existential, but an existential claim does not imply the universal. 'All X have property P' implies 'some X have property P', but 'some X have property P' does not imply 'all X have property P'.",
            "structure": "sentence_A (universal claim about all members of a category) → sentence_B (existential claim that A strictly implies - if all have it, some must have it) → sentence_C (specific instance that B licenses but A specifies more precisely)",
            "example": "'All licensed physicians in this state are required by law to complete 50 hours of continuing medical education every two years to maintain their license.' → 'Therefore, there exist physicians in this state who are currently engaged in or planning continuing medical education activities.' → 'Dr. Martinez, a licensed cardiologist at City Hospital, is registered for a cardiovascular update conference this month, which she is attending to satisfy part of her biennial CME requirement.'",
            "why_asymmetric": "B is strictly implied by A - if all physicians must complete CME, then some physicians are doing CME. C is a specific instance that B licenses but A entails more precisely than B (A says all are required, so any specific licensed physician must be completing CME). SCORING: A→B HIGH (universal implies existential). B→A LOW (existential does not imply universal). A→C HIGH (C is a specific instance of A's universal). C→A MODERATE (C is consistent with A but does not imply A).",
            "real_world_application": "Logic and reasoning education, database query semantics, legal interpretation, regulatory coverage analysis"
          },
          "symmetric_pattern": {
            "structure": "sentence_X (true universal claim) ↔ sentence_Y (true existential claim where X implies Y but Y is independently verifiable)",
            "example": "'Every professional sports team in the national basketball association must maintain a roster of between 13 and 15 active players throughout the regular season.' ↔ 'At any point during the regular season, there are between 390 and 450 active NBA players across all 30 teams.'",
            "why_symmetric": "X is the universal rule; Y is the aggregate existential consequence of X applied across all 30 teams. Each implies the other in a mutually verifying way."
          },
          "hard_negative_strategy": {
            "description": "CLOSE negatives are existential claims that are compatible with A but not implied by A - they could be false even if A is true.",
            "examples": [
              "CLOSE: 'Some physicians complete their CME requirements in the final month of the two-year cycle rather than distributing them throughout the period.' (compatible with A but not implied - some might complete early, making this merely possible, not necessary)",
              "CLOSE: 'The state medical board reviews CME completion records during license renewal and sends reminders six months before the deadline.' (same system, procedural fact, not implied by A's universal requirement)",
              "DISTANT: 'Online CME platforms have grown to represent over 60 percent of all CME hours completed nationally, reflecting the shift toward digital professional development.'"
            ],
            "why_negative": "Timing patterns and board procedures are compatible with A but not logically required by A. The model must score these lower than the strictly implied existential."
          },
          "variation_parameters": {
            "quantifier_form": {
              "values": ["all must", "no one may", "every instance is", "none are permitted", "all cases require"],
              "why_this_varies": "Different universal quantifier forms test whether the model handles surface variation in universal claims"
            },
            "domain": {
              "values": ["professional licensing", "legal rights", "mathematical sets", "biological categories", "economic regulations"],
              "why_this_varies": "Different domains have different universal claim structures and different existential consequences"
            },
            "implication_directness": {
              "values": ["direct existential implication", "aggregate statistical implication", "specific instance implication"],
              "why_this_varies": "Different implication types test different aspects of universal-existential reasoning"
            }
          },
          "combination_space": 225,
          "notes": "The asymmetry between A→B HIGH and B→A LOW is the core teaching signal. Mark with universal_existential_direction flag in batch metadata."
        }
      ]
    },
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
