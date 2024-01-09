"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests

response = requests.get('https://randomuser.me/api/')
data = response.json()

name = data['results'][0]['name']['first'] + " " + data['results'][0]['name']['last']
country = data['results'][0]['location']['country']
phone = data['results'][0]['phone']

print(f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}")