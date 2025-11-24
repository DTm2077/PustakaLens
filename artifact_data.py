# artifact_data.py

# !!! IMPORTANT !!!
# The KEYS (left side) must match your filenames EXACTLY (including .jpg and capital letters).

DATABASE = {
    # ==========================================
    # 1. BATIK
    # ==========================================
    "Batik_Salvia_batik.jpg": {
        "title": "Batik Salvia",
        "place_of_discovery": "Pekalongan, Central Java",
        "origin": "Modern Contemporary Motif",
        "summary": "A beautiful modern batik pattern featuring the Salvia flower. In batik philosophy, flowers represent the blossoming of the soul and natural beauty. This motif uses bright colors typical of the 'Pesisiran' (coastal) style.",
        "fun_fact": "The name 'Salvia' implies healing, derived from the Latin word 'salvere'."
    },

    "Peksi_batik.jpg": {
        "title": "Batik Peksi (Bird Motif)",
        "place_of_discovery": "Yogyakarta / Solo",
        "origin": "Traditional Royal Motif",
        "summary": "'Peksi' is the Javanese Krama Inggil word for Bird. Bird motifs in batik often symbolize freedom and the upper world. In some contexts, it represents the journey of the human spirit toward the divine.",
        "fun_fact": "In classical Kraton batik, certain bird wings (Lar) were once reserved only for royalty."
    },

    # ==========================================
    # 2. STATUES (PATUNG)
    # ==========================================
    "Garuda_Wisnu_Kencana.jpg": {
        "title": "Garuda Wisnu Kencana",
        "place_of_discovery": "Ungasan, Bali",
        "origin": "Nyoman Nuarta (2018)",
        "summary": "This colossal statue depicts the Hindu god Vishnu riding his mount, the mythical eagle Garuda. Standing 121 meters tall, it symbolizes the mission to save the world and environmental wisdom.",
        "fun_fact": "It is the 4th tallest statue in the world, taller than the Statue of Liberty."
    },

    "Patung_Dirgantara.jpg": {
        "title": "Patung Dirgantara",
        "place_of_discovery": "Pancoran, Jakarta",
        "origin": "Edhi Sunarso (1964)",
        "summary": "Commonly known as the Pancoran Monument, this statue depicts a man pointing to the sky. Commissioned by Bung Karno, it represents the courage of the Indonesian nation in exploring aerospace technology.",
        "fun_fact": "President Soekarno posed for the statue himself to demonstrate the specific gesture he wanted."
    },

    "patung_surabaya.jpg": {  # Note: Your file is lowercase 'p'
        "title": "Sura and Baya Monument",
        "place_of_discovery": "Surabaya, East Java",
        "origin": "City Symbol (1952)",
        "summary": "The iconic symbol of Surabaya, depicting the battle between a Shark (Sura) and a Crocodile (Baya). It symbolizes the struggle for life and the bravery of the city's people.",
        "fun_fact": "The name 'Surabaya' literally translates to 'bravely facing danger' (Sura = brave, Baya = danger)."
    },

    # ==========================================
    # 3. WAYANG
    # ==========================================
    "wayang_madya.jpg": { # Note: Your file is lowercase 'w'
        "title": "Wayang Madya",
        "place_of_discovery": "Surakarta (Solo)",
        "origin": "Created by Mangkunegara IV",
        "summary": "Wayang Madya is a specific set of puppets that bridge the gap between the ancient Mahabharata stories (Purwa) and modern history. They tell stories of the Javanese kings of the middle era.",
        "fun_fact": "These puppets are rare and focus on the genealogy of Javanese royalty."
    },

    "Wayang_Purwa.jpg": {
        "title": "Wayang Purwa",
        "place_of_discovery": "Java, Indonesia",
        "origin": "Ancient Tradition (10th Century)",
        "summary": "The most popular form of Wayang Kulit. 'Purwa' means 'First' or 'Ancient'. These puppets perform the great Hindu epics of the Ramayana and Mahabharata.",
        "fun_fact": "A single Dalang (puppeteer) controls all puppets, voices, and sound effects all night long."
    },

    "Wayang_Rama.jpg": {
        "title": "Sri Rama (Wayang Figure)",
        "place_of_discovery": "Java / Bali",
        "origin": "Ramayana Epic",
        "summary": "Rama is the protagonist of the Ramayana epic and the seventh avatar of Vishnu. In Wayang, he is depicted with a slender form and a bowed head, symbolizing humility, wisdom, and moral perfection.",
        "fun_fact": "Rama's green or black face color in Wayang usually symbolizes inner peace and maturity."
    }
}

# ==========================================
# HELPER FUNCTION
# ==========================================
def get_artifact_info(filename):
    # 1. Try to find exact match
    if filename in DATABASE:
        return DATABASE[filename]
    
    # 2. Debugging: If not found, print what we were looking for
    print(f"⚠️ WARNING: Could not find key '{filename}' in database.")
    
    # 3. Return default
    return {
        "title": "Unknown Artifact",
        "place_of_discovery": "-",
        "origin": "-",
        "summary": f"We identified this file as '{filename}', but no details were found in artifact_data.py.",
        "fun_fact": "Check if the filename in the folder matches the key in the python file exactly."
    }