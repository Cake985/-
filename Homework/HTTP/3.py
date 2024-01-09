"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
import requests
import json

response1 = requests.get('https://rickandmortyapi.com/api/character/?page=2')
characters1 = response1.json()['results']

response2 = requests.get('https://rickandmortyapi.com/api/character/?page=3')
characters2 = response2.json()['results']

response3 = requests.get('https://rickandmortyapi.com/api/character/?page=4')
characters3 = response3.json()['results']

characters = characters1 + characters2 + characters3

characters = characters[14:75]

for character in characters:
    response = requests.get(character['url'])
    character_details = response.json()
    character['name'] = character_details['name']
    character['origin'] = character_details['origin']['name']
    character['episodes'] = character_details['episode']

with open('kaplan.json', 'w') as f:
    json.dump(characters, f, indent=4)