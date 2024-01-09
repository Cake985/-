"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import requests

response = requests.get('https://cataas.com/cat')
with open('cat1.jpg', 'wb') as f:
    f.write(response.content)
with open('cat2.png', 'wb') as f1:
    f1.write(response.content)

response1 = requests.get('https://cataas.com/cat/cute')
with open('cat3.jpg', 'wb') as f2:
    f2.write(response1.content)
response2 = requests.get('https://cataas.com/cat/funny')
with open('cat4.png', 'wb') as f3:
    f3.write(response2.content)


response3 = requests.get('https://cataas.com/cat?filter=pixel')
with open('cat5.jpg', 'wb') as f4:
    f4.write(response3.content)
with open('cat6.png', 'wb') as f5:
    f5.write(response3.content)