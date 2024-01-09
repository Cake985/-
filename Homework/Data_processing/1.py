"""
В соответствии с вашим номер в журнале выведите на экран Имя персонажа и ссылку на него.
"""
characters = {
    "1": {
        "Rick Sanchez": {
            "https://rickandmortyapi.com/api/character/1": "Male"
        }
    },
    "2": {
        "Morty Smith": {
            "https://rickandmortyapi.com/api/character/2": "Male"
        }
    },
    "3": {
        "Summer Smith": {
            "https://rickandmortyapi.com/api/character/3": "Female"
        }
    },
    "4": {
        "Beth Smith": {
            "https://rickandmortyapi.com/api/character/4": "Female"
        }
    },
    "5": {
        "Jerry Smith": {
            "https://rickandmortyapi.com/api/character/5": "Male"
        }
    },
    "6": {
        "Abadango Cluster Princess": {
            "https://rickandmortyapi.com/api/character/6": "Female"
        }
    },
    "7": {
        "Abradolf Lincler": {
            "https://rickandmortyapi.com/api/character/7": "Male"
        }
    },
    "8": {
        "Adjudicator Rick": {
            "https://rickandmortyapi.com/api/character/8": "Male"
        }
    },
    "9": {
        "Agency Director": {
            "https://rickandmortyapi.com/api/character/9": "Male"
        }
    },
    "10": {
        "Alan Rails": {
            "https://rickandmortyapi.com/api/character/10": "Male"
        }
    },
    "11": {
        "Albert Einstein": {
            "https://rickandmortyapi.com/api/character/11": "Male"
        }
    },
    "12": {
        "Alexander": {
            "https://rickandmortyapi.com/api/character/12": "Male"
        }
    },
    "13": {
        "Alien Googah": {
            "https://rickandmortyapi.com/api/character/13": "unknown"
        }
    },
    "14": {
        "Alien Morty": {
            "https://rickandmortyapi.com/api/character/14": "Male"
        }
    },
    "15": {
        "Alien Rick": {
            "https://rickandmortyapi.com/api/character/15": "Male"
        }
    },
    "16": {
        "Amish Cyborg": {
            "https://rickandmortyapi.com/api/character/16": "Male"
        }
    },
    "17": {
        "Annie": {
            "https://rickandmortyapi.com/api/character/17": "Female"
        }
    },
    "18": {
        "Antenna Morty": {
            "https://rickandmortyapi.com/api/character/18": "Male"
        }
    }
}
character_name = list(characters["14"].keys())[0]
character_link = characters["14"][character_name]
print(f"Имя: {character_name}\nСсылка: {character_link}")