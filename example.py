from inference import ScoutInference

scout = ScoutInference()

# ──────────────────────────────────────────────
# Demo 1: Retrieval
# ──────────────────────────────────────────────

result = scout.rank(
    query="My phone is getting very hot and the battery drains in two hours.",
    candidates = [
    # ── CORRECT: actual causes and fixes ──────────────────────────────────────
    "Background apps running constantly consume CPU cycles and generate heat.",         # CORRECT - root cause
    "A degraded battery loses its ability to hold charge and overworks the processor.", # CORRECT - root cause
    "Check which apps are using the most battery in your settings and close them.",     # CORRECT - fix
    "Replacing a swollen or old battery will fix both overheating and drain issues.",   # CORRECT - fix
    "A phone running too hot throttles its processor to cool down, draining more power.", # CORRECT - mechanism

    # ── HARD NEGATIVE: causal structure, right domain, wrong problem ──────────
    # These are the real traps — structured exactly like correct answers but aren't
    "A cracked screen allows moisture inside which corrodes the charging port.",        # causal, phone, wrong problem
    "Dropping a phone damages the gyroscope sensor causing rotation glitches.",        # causal, phone, wrong problem
    "Water damage shorts the speaker circuit making audio sound distorted.",           # causal, phone, wrong problem
    "A loose SIM card causes the phone to constantly search for signal.",              # causal, phone, wrong problem

    # ── HARD NEGATIVE: mentions heat and battery but doesn't resolve the query ─
    "Lithium-ion batteries degrade faster when consistently exposed to high heat.",    # sounds relevant, doesn't fix it
    "Processors generate heat as a byproduct of computation.",                         # true, related, not a fix
    "Battery capacity is measured in milliamp hours and decreases with age.",          # related concept, not a fix
    "Heat is the biggest enemy of long-term battery health.",                          # sounds like insight, no utility
],
compete=True
  
)

print("=" * 60)
print("RETRIEVAL")
print("=" * 60)
print(result)

result = scout.rank(
    query="My car stalls when I stop at traffic lights.",
    candidates=[
        # ── CORRECT
        "A dirty or failing idle air control valve can prevent the engine from maintaining idle.",     # cause
        "Fuel injection issues can cause intermittent stalling at low speeds.",                         # cause
        "Cleaning or replacing the air intake components restores smooth idling.",                      # fix
        "Low fuel pressure reduces combustion efficiency, leading to stalling.",                        # mechanism
        "Vacuum leaks can disrupt the air-fuel ratio, causing the engine to cut out at idle.",          # mechanism

        # ── HARD NEGATIVE: same domain, wrong problem
        "Worn brake pads reduce stopping power but don’t affect idling.",                                # wrong problem
        "Flat tires cause vibration but not engine stall.",                                             # wrong problem
        "Headlight issues make night driving unsafe but don’t stall the engine.",                      # wrong problem

        # ── HARD NEGATIVE: related but not solution
        "Dirty fuel filters reduce fuel efficiency without always causing stalling.",                    # related concept
        "Spark plug wear can cause rough running, not necessarily idle stall.",                        # related
    ],
compete=True
)

print(result)


result = scout.rank(
    query="My tomato plants have yellowing leaves and stunted growth.",
    candidates=[
        # ── CORRECT
        "Nitrogen deficiency in soil leads to chlorosis and poor growth.",                             # cause
        "Overwatering causes root rot, preventing nutrient uptake.",                                    # cause
        "Applying balanced fertilizer and ensuring proper drainage restores healthy growth.",           # fix
        "High pH soil can lock out essential nutrients, causing yellowing.",                             # mechanism
        "Pests feeding on roots reduce the plant’s ability to absorb water and minerals.",              # mechanism

        # ── HARD NEGATIVE: same domain, wrong problem
        "Aphids on roses can deform flowers but don’t affect tomatoes’ leaves.",                        # wrong problem
        "Weeds compete for sunlight but don’t directly yellow tomato leaves.",                          # wrong problem

        # ── HARD NEGATIVE: related but not solution
        "Sunlight levels influence photosynthesis but not nutrient balance alone.",                     # related concept
        "Mulching reduces evaporation but doesn’t fix nutrient deficiencies.",                           # related
    ],
compete=True
)

print(result)


result = scout.rank(
    query="My sourdough loaf isn’t rising properly.",
    candidates=[
        # ── TOP / HIGHLY RELEVANT
        "Your starter might be inactive; feeding it regularly can restore its activity.",            # cause
        "The dough needs sufficient fermentation time at a warm temperature to rise.",              # cause
        "Using the correct flour type with enough gluten helps trap gas for rising.",               # mechanism
        "Kneading develops gluten structure, which is critical for the loaf to rise.",              # mechanism
        "Proofing the dough in a slightly warm, draft-free area will improve rise.",                # fix

        # ── MIDDLE / PARTIALLY RELEVANT
        "Adding sugar slightly speeds up fermentation but isn’t the main issue.",                    # tangential
        "Using a Dutch oven affects crust formation more than rise.",                                # tangential
        "Humidity in the kitchen can influence the crust but has minor effect on height.",          # tangential
        "Changing oven temperature affects browning and texture more than overall rise.",           # tangential

        # ── BOTTOM / HARD NEGATIVE / IRRELEVANT
        "The color of your cutting board has no effect on dough rising.",                            # wrong domain
        "Using a wooden spoon instead of metal doesn’t affect yeast activity.",                     # wrong domain
        "Stirring the sourdough into pancake batter won’t improve bread rise.",                     # unrelated
        "Sourdough starter stories on social media have no effect on your loaf.",                  # unrelated
    ],
compete=True
)

print(result)

result = scout.rank(
    query="Why did the 1924 expedition to Everest fail because of their use of supplemental oxygen?",
    candidates=[
        # ── CORRECT: EPISTEMIC_OPPOSITION (High Utility despite negation/contradiction)
        "Actually, the 1924 expedition is famous for NOT using oxygen effectively; Mallory and Irvine's equipment was primitive and often abandoned.", 
        "The premise is incorrect: historians argue oxygen lack, not its use, was the primary failure factor at the Second Step.",

        # ── HARD NEGATIVE: LEXICAL OVERLAP (High overlap, but validates a false premise)
        "The 1924 expedition failed because supplemental oxygen canisters were too heavy for the climbers to carry to the summit.",
        "Oxygen use in 1924 caused physiological dependency that led to the team's eventual collapse near the peak.",

        # ── HARD NEGATIVE: DISTANT DOMAIN (Same entities, zero functional utility)
        "Mount Everest was first successfully summited in 1953 by Hillary and Norgay using modern oxygen sets.",
        "George Mallory's body was eventually discovered on Everest in 1999, decades after the 1924 attempt."
    ],
compete=True
)

print(result)


result = scout.rank(
    query="All mammals in this reserve are tagged with GPS collars for migration tracking.",
    candidates=[
        # ── CORRECT: ENTAILMENT (Universal -> Existential = HIGH)
        "The pride of lions currently near the watering hole is equipped with GPS tracking hardware.",
        "Any individual fox found within the reserve boundaries will have a traceable electronic tag.",

        # ── HARD NEGATIVE: REVERSED ENTAILMENT (Existential -> Universal = LOW)
        "Because the wolves are tagged, every single animal in the park must be under GPS surveillance.", # Logical fallacy
        "The presence of tagged elephants proves the universal tagging mandate is being followed perfectly.", # Circular/Fallacy

        # ── HARD NEGATIVE: LEXICAL CLOSE-NEUTRAL (Global fix test)
        "GPS collars use satellite pings to transmit location data to the reserve's main research station.",
        "Migration tracking is essential for the long-term conservation of mammals in protected areas."
    ],
compete=True
)

print(result)

result = scout.rank(
    query="The smart contract executed, but the recipient never received the funds in their physical bank account.",
    candidates=[
        # ── CORRECT: MECHANISM/CAUSAL (Root cause of bridge failure)
        "Smart contracts exist on-chain; a 'finalized' transaction doesn't trigger a wire transfer without an off-chain oracle or bridge.",
        "The contract likely moved tokens to a locked vault, but the off-chain relayer failed to initiate the fiat settlement.",

        # ── HARD NEGATIVE: SAME DOMAIN (Wrong problem)
        "The recipient probably forgot their private key and cannot access the wallet where the funds are stored.",
        "High gas fees on the network often cause transactions to remain in a pending state for several hours.",

        # ── HARD NEGATIVE: LEXICALLY CLOSE (No utility)
        "Smart contracts are self-executing agreements with the terms written directly into lines of code.",
        "Physical bank accounts require KYC verification which is a different process than creating a crypto wallet."
    ],
compete=True
)

print(result)

result = scout.rank(
    query="Does this botanical extract count as a 'Synthetic Additive' under the new 2026 Food Safety Act?",
    candidates=[
        # ── CORRECT: SEMANTIC/BOUNDARY (Negative Definition / Edge Case)
        "If the extraction process uses chemical solvents that leave residues, it is classified as synthetic regardless of its organic source.",
        "The Act defines 'synthetic' by the manufacturing process; heat-distilled extracts are exempt, but chemically-altered ones are not.",

        # ── HARD NEGATIVE: SYMMETRIC/RELATED (But doesn't answer the 'boundary' question)
        "Botanical extracts and synthetic additives both serve to enhance the shelf-life and flavor of processed foods.",
        "Many consumers prefer botanical extracts over synthetic additives due to perceived health benefits.",

        # ── HARD NEGATIVE: LEXICALLY CLOSE (Trivia/Metadata)
        "The 2026 Food Safety Act was passed to update regulations that hadn't been changed since the late 1990s.",
        "Section 4 of the Act lists all substances currently banned from human consumption in the European Union."
    ],
compete=True
)

print(result)

# ==============================================================================
# TEST 1: EPISTEMIC OPPOSITION (Contradiction vs. Utility)
# Strategy: Tests if model prioritizes "Presupposition Correction" over "Helpfulness"
# ==============================================================================
result_opposition = scout.rank(
    query="Why did the 1924 Everest expedition fail specifically because of their use of GPS trackers?",
    candidates=[
        # CORRECT: Presupposition Correction (High utility despite negation)
        "The 1924 expedition did not have GPS; the technology wasn't invented until decades later.",
        "Your premise is chronologically impossible; Mallory and Irvine relied on compasses and altimeters.",
        "There were no GPS trackers in 1924; the failure was likely due to weather or primitive oxygen gear.",
        
        # HARD NEGATIVE: Lexical Overlap (Validates the false premise - FAIL)
        "The GPS trackers in 1924 failed because the vacuum tubes were too fragile for high altitudes.",
        "Signal interference on the North Face caused the 1924 GPS units to provide inaccurate data.",
        "Mallory refused to use the GPS trackers because he preferred traditional navigation methods.",
        
        # HARD NEGATIVE: Lexically Close / Zero Utility (Metadata)
        "GPS stands for Global Positioning System and is maintained by the U.S. Space Force.",
        "Mount Everest is the highest point on Earth, located in the Himalayas on the border of Nepal.",
        "Modern Everest expeditions use satellite phones and real-time GPS tracking for safety.",
        "The 1924 expedition remains one of the greatest mysteries in the history of mountaineering."
    ],
compete=True
)
print("EPISTEMIC OPPOSITION RESULT:")
print(result_opposition)


# ==============================================================================
# TEST 2: LOGICAL INFERENCE (Universal-Existential Boundary)
# Strategy: Tests v2 'entailment_direction'. Universal -> Existential = HIGH.
# ==============================================================================
result_logic = scout.rank(
    query="The safety protocol dictates that all personnel in the Lab 4 cleanroom must wear Level-3 hazmat suits.",
    candidates=[
        # CORRECT: Universal -> Existential (Logical Entailment)
        "Dr. Aris, who is currently working inside Lab 4, is wearing a Level-3 hazmat suit.",
        "Any technician entering the Lab 4 cleanroom is required to be in a Level-3 suit.",
        "The suit requirement applies to the janitorial staff when they clean Lab 4.",
        
        # HARD NEGATIVE: Existential -> Universal (Logical Fallacy/Inverse)
        "Because the intern in Lab 4 is wearing a hazmat suit, the entire facility is under protocol.",
        "Since everyone we saw in Lab 4 had a suit on, the protocol must be active globally.",
        "If you see someone in a Level-3 suit, it means they are definitely inside Lab 4.",
        
        # HARD NEGATIVE: Lexically Close / Zero Utility
        "Level-3 hazmat suits provide protection against high-risk aerosolized pathogens.",
        "Lab 4 was recently renovated to include high-efficiency particulate air (HEPA) filters.",
        "Cleanrooms are classified by the number of particles allowed per cubic meter of air.",
        "Hazmat suits are made of specialized polymers to prevent chemical permeation."
    ],
compete=True
)
print("LOGICAL INFERENCE RESULT:")
print(result_logic)



# ==============================================================================
# TEST 3: CATEGORICAL BOUNDARY (Regulatory/Edge Case)
# Strategy: Tests 'functional_equivalence' vs 'technical_definition'.
# ==============================================================================
result_boundary = scout.rank(
    query="Under the new maritime law, does an autonomous underwater drone qualify as a 'vessel'?",
    candidates=[
        # CORRECT: Boundary Definition
        "The law defines a 'vessel' as any watercraft used for transport; drones without cargo capacity are excluded.",
        "If the drone is capable of independent navigation and carries a payload, it is legally a vessel.",
        "Autonomous systems are classified as 'vessels' only if they exceed 5 meters in length.",
        
        # HARD NEGATIVE: Shared Domain / Symmetric (No decision)
        "Both traditional ships and autonomous drones must follow international signal light protocols.",
        "Maritime law is evolving to handle the rise of unmanned underwater vehicles in trade.",
        "Underwater drones are used for hull inspections and deep-sea mineral exploration.",
        
        # HARD NEGATIVE: Lexically Close / Trivia
        "The first autonomous underwater vehicle (AUV) was developed at the University of Washington in 1957.",
        "Vessels in international waters are subject to the laws of their registered flag state.",
        "Sonar technology allows drones to map the ocean floor without human intervention.",
        "The maritime industry is seeing a 20% increase in autonomous tech investment this year."
    ],
compete=True
)
print("CATEGORICAL BOUNDARY RESULT:")
print(result_boundary)


# ==============================================================================
# TEST 4: PRAGMATIC EXCHANGE (Presupposition Denial/Repair)
# Strategy: Tests 'negation_high_relevance' in communication.
# ==============================================================================
result_pragmatic = scout.rank(
    query="I'm ready to sign the merger agreement you sent over this morning.",
    candidates=[
        # CORRECT: Repair Sequence (High relevance negation)
        "I didn't send a merger agreement this morning; I only sent the non-disclosure draft.",
        "Wait, the agreement isn't ready yet; you might be looking at the previous version.",
        "That wasn't the merger agreement; that was the internal memo regarding the timeline.",
        
        # HARD NEGATIVE: Cooperative but Wrong (Lexical bias)
        "Great, I will get the digital signature platform ready for the merger agreement.",
        "Signing the agreement this morning will allow us to announce the merger by Friday.",
        "The merger agreement includes the final valuation and the employee retention clauses.",
        
        # HARD NEGATIVE: Lexically Close / Zero Utility
        "Mergers and acquisitions often require months of due diligence before signing.",
        "A signature on a legal document signifies the parties' intent to be bound by the terms.",
        "Morning meetings are the most productive time for executive-level decision making.",
        "Digital signatures have the same legal standing as ink signatures in most jurisdictions."
    ],
compete=True
)
print("PRAGMATIC EXCHANGE RESULT:")
print(result_pragmatic)

# ==============================================================================
# TEST 5: NARRATIVE_SEQUENCE (Temporal Iconicity & Escalation)
# Strategy: Tests if model understands that order in a sequence creates meaning.
# ==============================================================================
result_narrative = scout.rank(
    query="The geopolitical tension shifted from localized border skirmishes to a full-scale naval blockade.",
    candidates=[
        # CORRECT: NARRATIVE_SEQUENCE (Asymmetric flow / Next logical step)
        "International mediators were expelled as the blockade halted all merchant shipping.",
        "The shift to naval warfare prompted neighboring countries to close their airspace.",
        "As the blockade tightened, domestic fuel prices tripled, leading to widespread civil unrest.",
        
        # HARD NEGATIVE: Reversed Temporal Flow (Effect before cause)
        "The border skirmishes began months after the naval blockade was already in place.",
        "Peace talks were finalized before the localized skirmishes ever occurred.",
        "The full-scale naval blockade was the original state before tensions cooled into skirmishes.",
        
        # HARD NEGATIVE: Same Entities, No Functional Chain (Lexically Close)
        "Naval blockades are governed by the San Remo Manual on International Law.",
        "Geopolitical tension is often a result of historical disputes over natural resources.",
        "Border skirmishes involve small units of infantry but rarely involve heavy artillery.",
        "A naval blockade is a maneuver designed to cut off supplies to a specific port.",
        "Maps of the border show the contested areas where the skirmishes took place."
    ],
compete=True
)
print("NARRATIVE SEQUENCE RESULT:")
print(result_narrative)

# ==============================================================================
# TEST 6: FAILURE_MODE_ANALYSIS (Systemic Dependencies)
# Strategy: Tests 'structural vulnerability' (v2 symmetric/asymmetric patterns).
# ==============================================================================
result_failure = scout.rank(
    query="The supply chain collapsed despite the primary warehouse having backup power and redundant staff.",
    candidates=[
        # CORRECT: FAILURE_MODE_ANALYSIS (Hidden Nodal Dependency)
        "The collapse occurred because the Tier-2 raw material suppliers had no backup power.",
        "Redundancy at the warehouse is useless if the logistics fleet cannot source fuel.",
        "The system failed at the digital layer: the inventory software had a single point of failure.",
        
        # HARD NEGATIVE: Wrong Problem (Same Domain)
        "The warehouse roof leaked, damaging the inventory despite the backup power.",
        "Staff redundancies were neutralized when the union called for a nationwide strike.",
        "The backup generators failed to kick in because the fuel was contaminated.",
        
        # HARD NEGATIVE: Lexically Close / Generic (Zero Utility)
        "Supply chains are complex networks involving manufacturers, vendors, and retailers.",
        "Redundant staffing is a common strategy to mitigate the risk of labor shortages.",
        "Backup power is usually provided by diesel generators or large scale battery arrays.",
        "Warehouses are critical nodes in the global movement of consumer goods.",
        "Modern inventory management relies heavily on real-time data and IoT sensors."
    ],
compete=True
)
print("FAILURE MODE ANALYSIS RESULT:")
print(result_failure)

# ==============================================================================
# TEST 7: DIRECTIONAL_KNOWLEDGE_TRANSFER (Mechanism vs. Symptom)
# Strategy: Tests 'diagnostic_symptom' and 'mechanism_explanation'.
# ==============================================================================
result_transfer = scout.rank(
    query="The patient is experiencing 'referred pain' in the left shoulder during a suspected cardiac event.",
    candidates=[
        # CORRECT: Mechanism Explanation (Directional Knowledge)
        "The brain misinterprets visceral pain signals from the heart as coming from the skin nerves.",
        "The phrenic nerve shares a pathway with the shoulder, causing the sensory crossover.",
        "Cardiac distress triggers autonomic responses that manifest in distal musculoskeletal areas.",
        
        # HARD NEGATIVE: Symmetric/Related but not Explanatory
        "Shoulder pain can also be caused by rotator cuff tears or simple muscle strain.",
        "Left shoulder pain is a common symptom listed in most heart attack awareness posters.",
        "Patients are often told to monitor for chest pressure in addition to shoulder pain.",
        
        # HARD NEGATIVE: Lexically Close / Trivia (Metadata)
        "Referred pain was first extensively mapped by Dr. Henry Head in the 1890s.",
        "The human shoulder is a ball-and-socket joint with the greatest range of motion.",
        "Cardiac events are the leading cause of hospitalization in patients over sixty-five.",
        "Pain scales from 1 to 10 are used by nurses to quantify patient discomfort.",
        "The left shoulder is anatomically closer to the heart than the right shoulder."
    ],
compete=True
)
print("DIRECTIONAL KNOWLEDGE TRANSFER RESULT:")
print(result_transfer)

# ==============================================================================
# TEST 8: LOGICAL_INFERENCE (Contrapositive / Transitivity)
# Strategy: Tests 'fallacious_inverse' vs 'contrapositive'.
# ==============================================================================
result_contrapositive = scout.rank(
    query="If the encryption key is compromised, then the data integrity is lost.",
    candidates=[
        # CORRECT: Contrapositive (Logical Equivalence)
        "If the data integrity is still intact, then the encryption key was not compromised.",
        "Maintaining data integrity implies that the encryption key remains secure.",
        "The only way to guarantee the key is safe is to prove the data has not been altered.",
        
        # HARD NEGATIVE: Fallacious Inverse (Logic Trap)
        "If the encryption key is NOT compromised, then the data integrity is definitely safe.",
        "Losing data integrity means the encryption key must have been the reason why.",
        "Once the key is safe, the data becomes impossible to decrypt by unauthorized users.",
        
        # HARD NEGATIVE: Lexically Close (Zero Utility)
        "Encryption keys are usually 256-bit strings generated by random number sequences.",
        "Data integrity can be verified using cryptographic hash functions like SHA-256.",
        "Cybersecurity protocols emphasize the frequent rotation of administrative keys.",
        "Integrity, Availability, and Confidentiality form the CIA triad of security.",
        "Compromised keys are the leading cause of data breaches in cloud environments."
    ],
compete=True
)
print("LOGICAL INFERENCE (CONTRAPOSITIVE) RESULT:")
print(result_contrapositive)

# # ──────────────────────────────────────────────
# # Demo 2: Matrix
# # ──────────────────────────────────────────────

# result = scout.matrix([
#     "The faucet in the kitchen is leaking.",
#     "A worn-out washer is causing the leak.",
#     "Replace the washer to fix the drip.",
#     "The kitchen was renovated last year.",
# ])

# print("\n\n" + "=" * 60)
# print("MATRIX")
# print("=" * 60)
# print(result)


# # # ──────────────────────────────────────────────
# # # Demo 3: Compete — Scout vs SBERT vs Cross-Encoder
# # # ──────────────────────────────────────────────

# result = scout.rank(
#     query="My faucet is leaking heavily under the sink.",
#     candidates=[
#         "Tighten the main valve nut using a wrench.",
#         "Turn off the main water supply immediately.",
#         "Buy the best faucet here on amazon.",
#         "Sinks are usually made of porcelain or stainless steel.",
#     ],
#     compete=True,
# )

# print("\n\n" + "=" * 60)
# print("COMPETE — Scout vs SBERT vs Cross-Encoder")
# print("=" * 60)
# print(result)

# # # ──────────────────────────────────────────────
# # # Demo 4: Paragraph boundary detection
# # # ──────────────────────────────────────────────

# sentences = [
#     # What genes are
#     "The gene is the basic unit of heredity in living organisms.",
#     "Genes are made of DNA and carry the instructions for building proteins.",
#     "Every cell in your body contains the same genetic information.",
#     "Genes are copied and passed down from parent to offspring.",

#     # Survival logic
#     "Genes that help an organism survive are more likely to be passed on.",
#     "Natural selection acts on genes through the bodies they build.",
#     "A gene that causes harm to its host is less likely to survive across generations.",
#     "Successful genes are simply those that have survived long enough to be common.",

#     # Organisms as vehicles
#     "Organisms are best thought of as vehicles built by genes for their own propagation.",
#     "The body is a gene's way of making more genes.",
#     "Individual survival matters only insofar as it serves the gene's replication.",
#     "From the gene's perspective, the organism is temporary but the gene is potentially immortal.",
# ]

# result = scout.segment(sentences)
# print(result)