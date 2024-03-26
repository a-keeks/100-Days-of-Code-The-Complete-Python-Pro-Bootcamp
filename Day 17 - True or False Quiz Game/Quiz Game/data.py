from random import sample

question_database = [
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Science: Mathematics",
        "question": "E = mc3",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Books",
        "question": "'Green Eggs and Ham' consists of only 50 different words.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "In Rocket League, you can play Basketball.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science & Nature",
        "question": "A plant that has a life cycle for more than a year is known as an annual.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "In Pokémon Sun and Moon, a male Salandit can evolve to a Salazzle.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "General Knowledge",
        "question": "The scientific name for the Southern Lights is Aurora Australis?",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Vehicles",
        "question": "The snowmobile was invented by Canadian Joseph-Armand Bombardier in 1937.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Politics",
        "question": "Russia passed a law in 2013 which outlaws telling children that homosexuals exist.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "hard",
        "category": "History",
        "question": "The man that shot Alexander Hamilton was named Aaron Burr.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "Tony Hawk's Pro Skater was released in 1999.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "The character that would eventually become Dr. Eggman was considered for the role of Sega's new flagship mascot before Sonic was.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Politics",
        "question": "In 2016, the United Kingdom voted to stay in the EU.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "In Pokémon, Arbok evolves into Seviper.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "History",
        "question": "Martin Luther King Jr. and Anne Frank were born the same year. ",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "hard",
        "category": "Entertainment: Television",
        "question": "The Klingon home planet is Qo'noS.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Japanese Anime & Manga",
        "question": "In Kill La Kill, the weapon of the main protagonist is a katana. ",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "General Knowledge",
        "question": "'Santa Claus' is a variety of melon.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "hard",
        "category": "Mythology",
        "question": "Rannamaari was a sea demon that haunted the people of the Maldives and had to be appeased monthly with the sacrifice of a virgin girl.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Music",
        "question": "Muse is a British (English) rock band",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Science: Computers",
        "question": "It's not possible to format a write-protected DVD-R Hard Disk.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Music",
        "question": "Musical artist, Future, collaborated with Kendrick Lamar for the song: 'Mask Off'.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "In the video game 'Splatoon', the playable characters were originally going to be rabbits instead of squids.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Music",
        "question": "'Neutral Milk Hotel' is a real band.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "In 'Space Station 13',  the station has a clown aboard it.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Science & Nature",
        "question": "Steel is an alloy of Iron and Carbon.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The Windows ME operating system was released in the year 2000.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Geography",
        "question": "St. Louis is the capital of the US State Missouri.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science & Nature",
        "question": "Igneous rocks are formed by excessive heat and pressure.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "In the Season One Championship of 'League of Legends', the highest achievable rank was Diamond.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Geography",
        "question": "Israel is 7 hours ahead of New York.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "hard",
        "category": "Mythology",
        "question": "Janus was the Roman god of doorways and passageways.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Mythology",
        "question": "In Norse mythology, Thor once dressed as a woman.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "hard",
        "category": "Entertainment: Video Games",
        "question": "In The Witcher 3, the Zoltan Chivay Gwent card can be found under the Hanged Man's Tree.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Geography",
        "question": "Is Tartu the capital of Estonia?",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science & Nature",
        "question": "Not including false teeth; A human has two sets of teeth in their lifetime.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "'Metal Gear Solid 3: Snake Eater' takes place on Shadow Moses Island.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Vehicles",
        "question": "The Japanese Shinkansen beat the French TGV's speed record for fastest electric rail train.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Politics",
        "question": "George W. Bush lost the popular vote in the 2004 United States presidential election.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Video Games",
        "question": "The game Garry's Mod originally took assets and codes from the popular Half Life 2 mod JBmod.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "The game 'Jetpack Joyride' was created by 'Redbrick Studios'.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Science: Mathematics",
        "question": "Zero factorial is equal to zero. ",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "History",
        "question": "United States President John F. Kennedy was assassinated during his presidential motorcade in Atlanta, Georgia on November 22nd, 1963.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "History",
        "question": "Thomas Crapper was a plumber who invented the flushing toilet.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Entertainment: Film",
        "question": "The color of the pills in the Matrix were Blue and Yellow.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Video Games",
        "question": "Codemasters is the developer of the Gran Turismo series.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "General Knowledge",
        "question": "Vietnam's national flag is a red star in front of a yellow background.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "General Knowledge",
        "question": "The bikini is named after the 'Bikini Atoll', an island where the United States conducted tests on atomic bombs.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Animals",
        "question": "Kangaroos keep food in their pouches next to their children.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "type": "boolean",
        "difficulty": "medium",
        "category": "Science: Mathematics",
        "question": "The proof for the Chinese Remainder Theorem used in Number Theory was NOT developed by its first publisher, Sun Tzu.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Entertainment: Film",
        "question": "In the original script of 'The Matrix', the machines used humans as additional computing power instead of batteries.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }
]


question_data = sample(question_database, 12)

