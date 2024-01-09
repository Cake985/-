"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json
task = ["oleg",24,["Belarus","Russia"]]
dict = {'name': task[0],
        'age': task[1],
        'countries': task[2][0]}
with open('kaplan.json', 'w') as file:
    json.dump(dict, file, indent=4)