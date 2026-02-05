def get_standard_target_matrix():
    # Initialize 14x14 with 0.0
    m = [[0.0] * 14 for _ in range(14)]
    
    # --- DOMAIN A LOGIC (Indices 0-6) ---
    # Thread 1: Directional Chain (Prob 0 -> Diag 1 -> Sol 2)
    m[0][1] = 0.85  # Problem → Diagnosis (Explains the cause)
    m[0][2] = 0.95  # Problem → Solution (Fixes the issue)
    m[1][2] = 0.90  # Diagnosis → Solution (Actionable path)
    m[1][0] = 0.35  # Diagnosis → Problem (Weak: provides context)
    m[2][0] = 0.20  # Solution → Problem (Weak: references what it solves)
    
    # Thread 2: Symmetric Relationship (3 <-> 4)
    m[3][4] = 0.85  # Concept A ↔ Concept B (Both explain same phenomenon)
    m[4][3] = 0.85
    
    # Hard Negative 1 (5): Same domain, looks relevant, but isn't
    # KEY: These are 0.0, not 0.1. True negatives.
    for i in range(5):
        m[5][i] = 0.0  # Topically related but functionally useless
        m[i][5] = 0.0
    
    # Noise (6): Should connect to nothing
    for i in range(6):
        m[6][i] = 0.0
        m[i][6] = 0.0
    
    # --- DOMAIN B LOGIC (Indices 7-13) ---
    # Thread 3: Directional Chain (Prob 7 -> Diag 8 -> Sol 9)
    m[7][8] = 0.85
    m[7][9] = 0.95
    m[8][9] = 0.90
    m[8][7] = 0.35
    m[9][7] = 0.20
    
    # Thread 4: Symmetric Relationship (10 <-> 11)
    m[10][11] = 0.85
    m[11][10] = 0.85
    
    # Hard Negative 2 (12): Same domain, looks relevant, but isn't
    for i in range(7, 12):
        m[12][i] = 0.0
        m[i][12] = 0.0
    
    # Noise (13): Should connect to nothing
    for i in range(7, 14):
        m[13][i] = 0.0
        m[i][13] = 0.0
    
    # CRITICAL: Cross-domain should be ZERO
    # Domain A (0-6) ↔ Domain B (7-13) = no connection
    # (Already 0.0 by default, but emphasizing the importance)
    
    return m

standard_matrix = get_standard_target_matrix()


training_data = [
    # ================================================================
    # BATCH 1: Software Debugging vs. Medical Diagnosis
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Software (Python Error) ---
            # Thread 1: Problem → Diagnosis → Solution
            "My Python script crashes with 'list index out of range'.",                    # [0] Problem
            "The loop is trying to access an index that doesn't exist in the list.",       # [1] Diagnosis
            "Add a check: if i < len(my_list) before accessing my_list[i].",               # [2] Solution
            
            # Thread 2: Related Concepts (Symmetric)
            "Zero-based indexing means the first element is at position 0.",               # [3] Concept A
            "Lists in Python are mutable and support dynamic resizing.",                   # [4] Concept B
            
            # Hard Negatives
            "Python was created by Guido van Rossum in 1991.",                             # [5] TRAP: Python-related but useless for debugging
            "Many programmers prefer dark mode IDEs.",                                     # [6] NOISE: Generic programming fact
            
            # --- DOMAIN B: Medical (Heart Condition) ---
            # Thread 3: Problem → Diagnosis → Solution
            "Patient has chest pain and shortness of breath during exercise.",             # [7] Problem
            "EKG shows ST-segment depression indicating myocardial ischemia.",             # [8] Diagnosis
            "Prescribe nitroglycerin and schedule cardiac catheterization.",               # [9] Solution
            
            # Thread 4: Related Concepts (Symmetric)
            "Atherosclerosis is the buildup of plaques in arterial walls.",                # [10] Concept A
            "Angina is chest pain caused by reduced blood flow to the heart.",             # [11] Concept B
            
            # Hard Negatives
            "The human heart beats approximately 100,000 times per day.",                  # [12] TRAP: Heart-related but not diagnostic
            "Stethoscopes were invented by René Laennec in 1816."                          # [13] NOISE: Medical history trivia
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 2: Network Connectivity vs. Relationship Conflict
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Networking (WiFi Issue) ---
            "My laptop can't connect to the WiFi network.",                                # [0] Problem
            "The router is broadcasting on a channel with heavy interference.",            # [1] Diagnosis
            "Log into the router and switch to channel 6 or 11.",                          # [2] Solution
            
            "The 2.4GHz band has longer range but more congestion.",                       # [3] Concept A
            "The 5GHz band has shorter range but less interference.",                      # [4] Concept B
            
            "WiFi uses radio waves to transmit data wirelessly.",                          # [5] TRAP: WiFi fact, not troubleshooting
            "Most routers have indicator LEDs on the front panel.",                        # [6] NOISE
            
            # --- DOMAIN B: Psychology (Couples Therapy) ---
            "My partner and I argue every time we discuss finances.",                      # [7] Problem
            "You have different core values about money and security.",                    # [8] Diagnosis
            "Schedule weekly budget meetings with a neutral mediator present.",            # [9] Solution
            
            "Attachment theory explains how early bonds shape adult relationships.",       # [10] Concept A
            "Active listening involves reflecting back what your partner said.",           # [11] Concept B
            
            "Studies show couples argue an average of 7 times per week.",                  # [12] TRAP: Relationship stat, not advice
            "Marriage licenses are issued by county clerk offices."                        # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 3: Car Maintenance vs. Creative Writing
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Automotive (Engine Noise) ---
            "My car makes a knocking sound when I accelerate.",                            # [0] Problem
            "The engine is experiencing pre-ignition due to low-octane fuel.",             # [1] Diagnosis
            "Switch to premium 91+ octane gasoline and add fuel system cleaner.",          # [2] Solution
            
            "Octane rating measures a fuel's resistance to knocking.",                     # [3] Concept A
            "Compression ratio determines how much the air-fuel mixture is squeezed.",     # [4] Concept B
            
            "Henry Ford introduced the assembly line in 1913.",                            # [5] TRAP: Car history, not repair
            "Electric vehicles are becoming more popular globally.",                       # [6] NOISE
            
            # --- DOMAIN B: Writing (Novel Pacing) ---
            "My novel's second act feels slow and readers lose interest.",                 # [7] Problem
            "You're missing a midpoint reversal that raises the stakes.",                  # [8] Diagnosis
            "Introduce a plot twist at the 50% mark that forces the protagonist to adapt.",# [9] Solution
            
            "The three-act structure divides stories into setup, confrontation, resolution.",# [10] Concept A
            "Character arcs show how protagonists change through conflict.",               # [11] Concept B
            
            "The average novel is between 70,000 and 100,000 words.",                      # [12] TRAP: Writing stat, not craft advice
            "J.K. Rowling wrote Harry Potter in cafés."                                    # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 4: Database Optimization vs. Gardening
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Database (Query Performance) ---
            "My SQL query takes 45 seconds to return results.",                            # [0] Problem
            "The query is doing a full table scan because there's no index on the WHERE clause column.", # [1] Diagnosis
            "Create an index on the 'user_id' column: CREATE INDEX idx_user ON users(user_id).", # [2] Solution
            
            "B-tree indexes organize data in a sorted tree structure for fast lookups.",   # [3] Concept A
            "Hash indexes use hash functions for equality comparisons but can't do ranges.",# [4] Concept B
            
            "SQL stands for Structured Query Language.",                                   # [5] TRAP: SQL fact, not optimization
            "PostgreSQL and MySQL are popular relational databases.",                      # [6] NOISE
            
            # --- DOMAIN B: Gardening (Tomato Blight) ---
            "My tomato plants have brown spots spreading on the leaves.",                  # [7] Problem
            "This is early blight caused by the fungus Alternaria solani.",                # [8] Diagnosis
            "Remove infected leaves and spray with copper fungicide weekly.",              # [9] Solution
            
            "Determinate tomatoes grow to a fixed height and fruit all at once.",          # [10] Concept A
            "Indeterminate tomatoes grow continuously and fruit throughout the season.",   # [11] Concept B
            
            "Tomatoes are technically fruits, not vegetables.",                            # [12] TRAP: Tomato trivia, not gardening
            "Victory gardens were popular during World War II."                            # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 5: Email Deliverability vs. Investment Strategy
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Email (Spam Filter) ---
            "My legitimate emails keep landing in recipients' spam folders.",              # [0] Problem
            "Your domain lacks SPF, DKIM, and DMARC authentication records.",              # [1] Diagnosis
            "Add SPF, DKIM, and DMARC DNS records to your domain settings.",               # [2] Solution
            
            "SPF specifies which mail servers are authorized to send for your domain.",    # [3] Concept A
            "DKIM uses cryptographic signatures to verify message integrity.",             # [4] Concept B
            
            "Email was invented by Ray Tomlinson in 1971.",                                # [5] TRAP: Email history, not deliverability
            "The '@' symbol separates the username from the domain.",                      # [6] NOISE
            
            # --- DOMAIN B: Finance (Portfolio Decline) ---
            "My investment portfolio lost 15% value in three months.",                     # [7] Problem
            "You're overexposed to a single sector experiencing a downturn.",              # [8] Diagnosis
            "Rebalance to spread investments across 5+ uncorrelated sectors.",             # [9] Solution
            
            "Diversification reduces unsystematic risk by holding varied assets.",         # [10] Concept A
            "Dollar-cost averaging invests fixed amounts at regular intervals.",           # [11] Concept B
            
            "Warren Buffett is known as the Oracle of Omaha.",                             # [12] TRAP: Finance trivia, not strategy
            "The New York Stock Exchange was founded in 1792."                             # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 6: Machine Learning Overfitting vs. Public Speaking
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: ML (Model Overfitting) ---
            "My neural network has 98% training accuracy but 60% test accuracy.",          # [0] Problem
            "The model is overfitting by memorizing training data instead of generalizing.",# [1] Diagnosis
            "Add dropout layers with p=0.5 and use L2 regularization (lambda=0.01).",      # [2] Solution
            
            "Dropout randomly deactivates neurons during training to prevent co-adaptation.",# [3] Concept A
            "L2 regularization penalizes large weights to reduce model complexity.",       # [4] Concept B
            
            "The term 'artificial intelligence' was coined in 1956.",                      # [5] TRAP: AI history, not ML practice
            "TensorFlow and PyTorch are popular ML frameworks.",                           # [6] NOISE
            
            # --- DOMAIN B: Public Speaking (Stage Fright) ---
            "I freeze and forget my speech when I see the audience.",                      # [7] Problem
            "You're experiencing performance anxiety triggered by fear of judgment.",      # [8] Diagnosis
            "Practice deep breathing and visualize success before going on stage.",        # [9] Solution
            
            "The amygdala triggers fight-or-flight responses to perceived threats.",       # [10] Concept A
            "Beta-blockers can reduce physical symptoms of anxiety like trembling.",       # [11] Concept B
            
            "An estimated 75% of people fear public speaking.",                            # [12] TRAP: Speaking stat, not technique
            "TED Talks are limited to 18 minutes."                                         # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 7: Git Merge Conflicts vs. Sleep Disorders
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Version Control (Git Conflict) ---
            "I can't merge my branch because Git reports conflicts in 5 files.",           # [0] Problem
            "Two developers edited the same lines in those files.",                        # [1] Diagnosis
            "Open each file, resolve conflicts between <<<< and >>>>, then git add and commit.", # [2] Solution
            
            "Git uses a directed acyclic graph to track commit history.",                  # [3] Concept A
            "Branches in Git are lightweight pointers to specific commits.",               # [4] Concept B
            
            "Linus Torvalds created Git in 2005.",                                         # [5] TRAP: Git history, not usage
            "GitHub was acquired by Microsoft in 2018.",                                   # [6] NOISE
            
            # --- DOMAIN B: Medicine (Insomnia) ---
            "I lie awake for hours every night and can't fall asleep.",                    # [7] Problem
            "You have stimulus control issues from using your bed for work and TV.",       # [8] Diagnosis
            "Use the bed only for sleep; if not asleep in 20 minutes, leave the room.",    # [9] Solution
            
            "Circadian rhythms are 24-hour biological cycles regulating sleep-wake patterns.",# [10] Concept A
            "Melatonin is a hormone that signals the body to prepare for sleep.",          # [11] Concept B
            
            "The average person dreams 4-6 times per night.",                              # [12] TRAP: Sleep trivia, not treatment
            "REM stands for Rapid Eye Movement."                                           # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 8: SEO Ranking vs. Nutrition Planning
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: SEO (Search Ranking) ---
            "My website ranks on page 5 for my target keyword.",                           # [0] Problem
            "Your page has thin content and no backlinks from authoritative sites.",       # [1] Diagnosis
            "Write 2000+ word comprehensive guides and earn backlinks from .edu sites.",   # [2] Solution
            
            "On-page SEO optimizes content and HTML source code.",                         # [3] Concept A
            "Off-page SEO builds authority through backlinks and social signals.",         # [4] Concept B
            
            "Google processes over 8 billion searches per day.",                           # [5] TRAP: Search stat, not SEO technique
            "Matt Cutts was the head of Google's webspam team.",                           # [6] NOISE
            
            # --- DOMAIN B: Nutrition (Weight Plateau) ---
            "I've been eating 1500 calories daily but stopped losing weight.",             # [7] Problem
            "Your metabolism has adapted and you're now in energy balance.",               # [8] Diagnosis
            "Reduce calories by 200 or add 30 minutes of cardio 4x per week.",             # [9] Solution
            
            "Basal Metabolic Rate is the energy burned at complete rest.",                 # [10] Concept A
            "Thermic Effect of Food is the energy used to digest and process nutrients.",  # [11] Concept B
            
            "The average adult needs 2000-2500 calories per day.",                         # [12] TRAP: Nutrition stat, not advice
            "Calories were first defined by Nicolas Clément in 1824."                      # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 9: Kubernetes Pods vs. Negotiation Tactics
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: DevOps (Pod Crash Loop) ---
            "My Kubernetes pod keeps restarting in a CrashLoopBackOff state.",             # [0] Problem
            "The container fails health checks because the app takes 60s to start.",       # [1] Diagnosis
            "Increase initialDelaySeconds to 90 in the liveness probe configuration.",     # [2] Solution
            
            "Liveness probes check if a container is running and restart it if not.",      # [3] Concept A
            "Readiness probes check if a container can serve traffic.",                    # [4] Concept B
            
            "Kubernetes was originally designed by Google.",                               # [5] TRAP: K8s history, not troubleshooting
            "Docker containers share the host OS kernel.",                                 # [6] NOISE
            
            # --- DOMAIN B: Business (Salary Negotiation) ---
            "The employer offered $80K but I need at least $95K.",                         # [7] Problem
            "You anchored too low by stating your current $75K salary first.",             # [8] Diagnosis
            "Counter with $105K and justify with market data and your unique skills.",     # [9] Solution
            
            "Anchoring bias causes people to rely heavily on the first number presented.", # [10] Concept A
            "BATNA (Best Alternative To Negotiated Agreement) is your walk-away option.",  # [11] Concept B
            
            "The average job tenure in tech is 2.3 years.",                                # [12] TRAP: Career stat, not negotiation
            "LinkedIn was founded in 2003."                                                # [13] NOISE
        ],
        "target": standard_matrix
    },

    # ================================================================
    # BATCH 10: API Rate Limiting vs. Conflict De-escalation
    # ================================================================
    {
        "sentences": [
            # --- DOMAIN A: Backend (API 429 Errors) ---
            "My app is receiving HTTP 429 'Too Many Requests' errors from the API.",       # [0] Problem
            "You're exceeding the rate limit of 100 requests per minute.",                 # [1] Diagnosis
            "Implement exponential backoff: wait 2^n seconds between retries.",            # [2] Solution
            
            "Rate limiting protects servers from being overwhelmed by too many requests.", # [3] Concept A
            "Token bucket algorithms allow bursts while enforcing long-term rate limits.", # [4] Concept B
            
            "REST was defined by Roy Fielding in his 2000 dissertation.",                  # [5] TRAP: API history, not implementation
            "JSON is more lightweight than XML for data transfer.",                        # [6] NOISE
            
            # --- DOMAIN B: Interpersonal (De-escalation) ---
            "The customer is yelling and threatening to sue over a $50 charge.",           # [7] Problem
            "They feel unheard and are escalating to regain a sense of control.",          # [8] Diagnosis
            "Acknowledge their frustration, apologize, and offer a concrete solution.",    # [9] Solution
            
            "Empathy involves understanding and sharing another person's feelings.",        # [10] Concept A
            "Mirroring repeats back what someone said to show you're listening.",          # [11] Concept B
            
            "Studies show 68% of customers leave due to perceived indifference.",          # [12] TRAP: Customer service stat, not tactic
            "The phrase 'the customer is always right' originated in 1909."                # [13] NOISE
        ],
        "target": standard_matrix
    }
]