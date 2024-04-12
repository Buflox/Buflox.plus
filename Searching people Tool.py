def guess_profile(name):
    profiles = {
        "John": {"Age": 30, "Profession": "Engineer", "Hobbies": ["reading", "hiking"]},
        "JOHN LHARRY BONDOY": {"Age":16, "Profession": "Student", "Birthday": "5|23|2007", "Phone No": "09709446419", "Facebook": "John Lharry Bondoy", "Physical Attributes": ["Good physic", "Good facial structure", "Ectomorph"], "Strength": "Communication", "Weakness": "Introvert", "Hobbies": ["exercising", "singing"]},
        "GERALD BONDOY": {"Age": 14, "Profession": "Student", "Birthday": "10|14|2009", "Phone No": "09518694152", "Facebook": "Gerald Bondoy",  "Hobbies": ["playing cellphone games", "using cellphone"]},
        "Emily": {"Age": 25, "Profession": "Teacher", "Hobbies": ["painting", "gardening"]},
        "ERWIN BONDOY": {"Age":52, "Profession": "Tricycle Driver", "Birthday": "1|13|1972", "Phone No": "Unknown", "Facebook": "Gerwin Banda",  "Hobbies": ["watching tv", "doing chores"]},
        "SHIRLEY BONDOY": {"Age":50, "Profession": "Primary School Teacher","Birthday": "1|1|1974", "Phone No": "09453405612", "Facebook": "Gerwinlhar",  "Hobbies": ["gardening", "singing"]},
        "FE BONDOY": {"Age":70, "Profession": "Gardener", "Birthday": "5|23|2007", "Phone No": "09070189360", "Facebook": "Fe Bondoy", "Hobbies": ["sewing", "gardening"]},
        "RENATO BONDOY": {"Age":74, "Profession": "Farmer", "Birthday": "5|23|2007",  "Hobbies": ["watching tv", "sleeping"]},
        "LIZA CALLA": {"Age":48, "Profession": "Sari sari Store owner", "Birthday": "5|23|2007", "Phone No": "09388030579", "Facebook": "Liza Banda",  "Hobbies": ["Unknown"]},
        "MICHAEL ANGELO CALLA": {"Age":13, "Profession": "Student","Birthday": "10|14|2010", "Phone No": "Unknown", "Facebook": "Mark Colis", "Hobbies": ["playing roblox", "using cellphone"]},
        "ALEX CALLA": {"Age":49, "Profession": "Electrician", "Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Alco Silco", "Hobbies": ["unknown"]},
        "NESTOR VALERA": {"Age":76, "Profession": "Retired", "Birthday": "1|1|1948", "Hobbies": ["walking", "watching tv"]},
        "LITA VALERA": {"Age":72, "Profession": "Retired", "Birthday": "1|1|1952", "Phone No": "09082444639", "Hobbies": ["praying", "going to church every saturday"]},
        "ILDE FONSO VALERA": {"Age":46, "Profession": "Bus Conductor", "Birthday": "5|23|2007", "Phone No": "09777660634", "Facebook": "Osnofedli", "Hobbies": ["unknown"]},
        "LEAH VALERA": {"Age":42, "Profession": "Baranggay Hall Helper","Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Leah B. Valera",  "Hobbies": ["unknown"]},
        "LEIDY LYN VALERA": {"Age":19, "Profession": "College Student", "Birthday": "5|23|2007", "Phone No": "09279567677", "Facebook": "Leidy Lyn Valera", "Hobbies": ["unknown"]},
        "ZEDRICK FONZ VALERA": {"Age":16, "Profession": "Student", "Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Zedrick Fonz Valera", "Hobbies": ["unknown"]},
        "CHARLZ IVAN VALERA": {"Age":15, "Profession": "Student", "Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Charlz Ivan Valera", "Hobbies": ["unknown"]},
        "SHEINA BONEO": {"Age":34, "Profession": "Elementary School Teacher", "Birthday": "5|23|2007", "Phone No": "09095150678", "Facebook": "Sheina Valera Boneo", "Hobbies": ["unknown"]},
        "EDCEL BOBILES": {"Age":17, "Profession": "Student", "Birthday": "3|27|2007", "Phone No": "Unknown", "Facebook": "Edcel Bobiles", "Hobbies": ["playing basketball", "watching reel or manga"]},
        "FRANCO TUSCANO": {"Age":16, "Profession": "Student", "Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Franco Tuscano", "Hobbies": ["exercising", "biking"]},
        "BRADLEY JAMES COMOT": {"Age":16, "Profession": "Student", "Birthday": "1|30|2007", "Phone No": "Unknown", "Facebook": "Bradley James", "Hobbies": ["writing poem", "joyride"]},
        "IVAN CLARK BUBAN": {"Age":15, "Profession": "Student", "Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Clark Marjelo", "Hobbies": ["playing drum", "biking"]},
        "ALJAYMAR ABUEVA": {"Age":16, "Profession": "Student", "Birthday": "5|23|2007", "Phone No": "Unknown", "Facebook": "Aljaymar abueva", "Hobbies": ["going to gym", "running"]},
         "JULIA FRANCE BONAFE": {"Age":16, "Profession": "Student", "Birthday": "   |   |   ", "Phone No": "Unknown", "Facebook": "France Julia Bonafe", "Hobbies": ["unknown"]},
         "MAJAN FYE BONGON": {"Age":16, "Profession": "Student", "Birthday": "2|23|2007", "Phone No": "Unknown", "Facebook": "Majan Fye Bongon", "Hobbies": ["unknown"]},
         "JANINE GRACE CARDANO": {"Age":16, "Profession": "Student", "Birthday": "10|18|2007", "Phone No": "Unknown", "Facebook": "Janine Cerafica Cardano", "Hobbies": ["unknown"]},
         "KIM ANGEL DIAZ": {"Age":16, "Profession": "Student", "Birthday": "10|9|2007", "Phone No": "Unknown", "Facebook": "Kim Angel Diaz", "Hobbies": ["unknown"]},
         "RAVEN MAE MABASA": {"Age":16, "Profession": "Student", "Birthday": "2|23|2007", "Phone No": "Unknown", "Facebook": "Raven Mabasa", "Hobbies": ["unknown"]},
         "GIAN CARLO RAQUION": {"Age":17, "Profession": "Student", "Birthday": "12|10|2006", "Phone No": "Unknown", "Facebook": "Gian Raquion", "Hobbies": ["unknown"]},
         "JUSTIN SERRANO": {"Age":17, "Profession": "Student", "Birthday": "7|11|2006", "Phone No": "Unknown", "Facebook": "Justin Serrano", "Hobbies": ["unknown"]},
         "BRIBERT BRENT BERCES": {"Age":17, "Profession": "Student/Sakristan", "Birthday": "7|1|2006", "Phone No": "Unknown", "Facebook": "Brent Berces", "Hobbies": ["playing basketball", "going to gym"]},
         "MIKE ANDREW VASQUEZ": {"Age":17, "Profession": "Student", "Birthday": "12|19|2006", "Phone No": "Unknown", "Facebook": "Mike Andre", "Hobbies": ["playing basketball"]},
         "EIRA CASSANDRA BRON": {"Age": "Unknown", "Profession": "Student", "Birthday": "6|13|  ", "Phone No": "Unknown", "Facebook": "Eira Cassandra Bron", "Hobbies": ["unknown"]},
         "ELAIZA MAE VOLANTE": {"Age": "Unknown", "Profession": "Student", "Birthday": "5|24|   ", "Phone No": "Unknown", "Facebook": "Elaiza Mae Volante", "Hobbies": ["unknown"]},
         "MARC JOHN CENA": {"Age":17, "Profession": "Student", "Birthday": "1|30|2006", "Phone No": "Unknown", "Facebook": "Marc John Brutas", "Hobbies": ["playing basketball"]},
         "FRANERRY IBALLAR": {"Age": "Unknown", "Profession": "Student", "Birthday": "10|25|   ", "Phone No": "Unknown", "Facebook": "Franerry Tecson Iballar", "Hobbies": ["dancing"]},
         "JUDE ANGELO MILLA": {"Age": "Unknown", "Profession": "Student", "Birthday": "11|11|   ", "Phone No": "Unknown", "Facebook": "Jude Angelo", "Hobbies": ["unknown"]},
         "KATRINA CASSANDRA PAZ": {"Age":16, "Profession": "Student", "Birthday": "6|25|2007", "Phone No": "Unknown", "Facebook": "Katrina Cassandra", "Hobbies": ["unknown"]},
         "STEPHINE REGIDOR": {"Age": "Unknown", "Profession": "Student", "Birthday": "9|29|   ", "Phone No": "Unknown", "Facebook": "Stephine Regidor", "Hobbies": ["playing basketball"]},
         "ASHLYN RUTH BRONCANO": {"Age": "Unknown", "Profession": "Student", "Birthday": "9|6|   ", "Phone No": "Unknown", "Facebook": "Ashlyn Ruth Broncano", "Hobbies": ["unknown"]},
         "KEIRA ANGELINE MAGDAONG": {"Age":16, "Profession": "Student", "Birthday": "2|10|2007", "Phone No": "Unknown", "Facebook": "Keira Angeline","Hobbies": ["unknown"]},
         "GEANN VELOSO": {"Age": "Unknown", "Profession": "Student", "Birthday": "9|2|   ", "Phone No": "Unknown", "Facebook": "Geann Veloso", "Hobbies": ["unknown"]},
         "JELIANE MAGDARAOG": {"Age": "17", "Profession": "Student", "Birthday":"10|18|2005", "Phone No": "Unknown", "Facebook": "Jeliane Bendal Magdaraog", "Hobbies": ["unknown"]},
         "JOAN BASE": {"Age":16, "Profession": "Student", "Birthday": "10|1|2007", "Phone No": "Unknown", "Facebook": "Joan Base", "Hobbies": ["unknown"]},
         "MANUEL QUEZON": {"Age": 60, "Profession": "Former President", "Birthday": "8|19|1878", "Phone No": "09123456789", "Twitter": "@MQuezon", "Physical Attributes": ["Stately appearance", "Strong jawline", "Mesomorph"], "Strength": "Leadership", "Weakness": "Impatience", "Hobbies": ["Reading", "Chess"]},
          "SERGIO OSMENA": {"Age": 65, "Profession": "Former President", "Birthday": "9|9|1878", "Phone No": "09234567890", "Instagram": "@SergioOsmena", "Physical Attributes": ["Distinguished look", "Kind eyes", "Endomorph"], "Strength": "Diplomacy", "Weakness": "Perfectionism", "Hobbies": ["Painting", "Golfing"]},
           "MANUEL ROXAS": {"Age": 58, "Profession": "Former President", "Birthday": "1|1|1892", "Phone No": "09345678901", "Facebook": "Manuel Roxas PH", "Physical Attributes": ["Charismatic presence", "Charming smile", "Mesomorph"], "Strength": "Negotiation", "Weakness": "Indecisiveness", "Hobbies": ["Fishing", "Playing piano"]},
             "ELPIDIO QUIRINO": {"Age": 68, "Profession": "Former President", "Birthday": "11|16|1890", "Phone No": "09456789012", "LinkedIn": "linkedin.com/in/elpidioquirino", "Physical Attributes": ["Dignified stature", "Thoughtful expression", "Endomorph"], "Strength": "Stability", "Weakness": "Overthinking", "Hobbies": ["Writing", "Birdwatching"]},
              "RAMON MAGSAYSAY": {"Age": 50, "Profession": "Former President", "Birthday": "8|31|1907", "Phone No": "09567890123", "Twitter": "@MagsaysayRamon", "Physical Attributes": ["Down-to-earth demeanor", "Friendly smile", "Mesomorph"], "Strength": "Integrity", "Weakness": "Impulsiveness", "Hobbies": ["Cooking", "Mountain climbing"]},
               "FERDINAND MARCOS": {"Age": 72, "Profession": "Former President", "Birthday": "9|11|1917", "Phone No": "09678901234", "Instagram": "@FMarcos", "Physical Attributes": ["Authoritative presence", "Sharp features", "Mesomorph"], "Strength": "Strategic thinking", "Weakness": "Authoritarian tendencies", "Hobbies": ["Painting", "Scuba diving"]},
                "CORAZON AQUINO": {"Age": 65, "Profession": "Former President", "Birthday": "1|25|1933", "Phone No": "09789012345", "Facebook": "CoryAquinoPH", "Physical Attributes": ["Graceful demeanor", "Warm smile", "Endomorph"], "Strength": "Courage", "Weakness": "Trust issues", "Hobbies": ["Gardening", "Calligraphy"]},
                  "FIDEL V. RAMOS": {"Age": 88, "Profession": "Former President", "Birthday": "3|18|1928", "Phone No": "09890123456", "Twitter": "@FVRamos", "Physical Attributes": ["Energetic posture", "Friendly demeanor", "Mesomorph"], "Strength": "Peacemaking", "Weakness": "Micromanagement", "Hobbies": ["Flying", "Playing basketball"]},
                  "JOSEPH ESTRADA": {"Age": 84, "Profession": "Former President", "Birthday": "4|19|1937", "Phone No": "09901234567", "Facebook": "ErapManila", "Physical Attributes": ["Charismatic personality", "Resilient spirit", "Endomorph"], "Strength": "Populism", "Weakness": "Scandals", "Hobbies": ["Playing billiards", "Watching movies"]},
                  "GLORIA MACAPAGAL-ARROYO": {"Age": 74, "Profession": "Former President", "Birthday": "4|5|1947", "Phone No": "09123456789", "Instagram": "@GMArroyo", "Physical Attributes": ["Intellectual aura", "Confident demeanor", "Mesomorph"], "Strength": "Political savvy", "Weakness": "Controversy", "Hobbies": ["Reading", "Playing piano"]},
                    "BENIGNO AQUINO III": {"Age": 61, "Profession": "Former President", "Birthday": "2|8|1960", "Phone No": "09234567890", "Twitter": "@NoynoyAquino", "Physical Attributes": ["Relaxed demeanor", "Friendly disposition", "Endomorph"], "Strength": "Good governance", "Weakness": "Health issues", "Hobbies": ["Basketball", "Photography"]},
                       "RODRIGO DUTERTE": {"Age": 77, "Profession": "Current President", "Birthday": "3|28|1945", "Phone No": "09345678901", "Facebook": "President Duterte", "Physical Attributes": ["Tough appearance", "Intense gaze", "Mesomorph"], "Strength": "Decisiveness", "Weakness": "Controversial statements", "Hobbies": ["Motorcycling", "Singing"]},


         
         
        
        
        # Add more profiles as needed
    }

    # Check if the name is in the predefined profiles
    if name in profiles:
        return profiles[name]
    else:
        return None

if __name__ == "__main__":
    Title = input("          ---------- Buflox.plus----------                                            ")
    Introduction = input("Hello my name is Boflox.plus. I'm an ai and upcourse I can help you find person. ")
    Instruction = input("-This tool can show you the personal information of your target")
    Target = input("(Just type the name and the surname of your target in all capital letter enjoy) ")
    name = input("Who do you want to search?: ")
    profile = guess_profile(name)
    
    if profile:
        print("\n--- Profile ---")
        print(f"Name: {name}")
        for key, value in profile.items():
            print(f"{key}: {value}")
    else:
        print("Sorry, I couldn't find that person.")
