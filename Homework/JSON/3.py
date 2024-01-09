"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
import json
task = ["oleg",24,["Belarus","Russia"],(24,1),["Moscow","Vladikavkaz",'Krasnodar',"Rostov","Nalchik"]]
dict = {'name': task[0],
        'age': task[1],
        'countries': [{'name': task[2][0],
                       'time': task[3][0],
                       'cities': task[4][0]}]
        }
with open('kaplan1.json', 'w') as file:
    json.dump(dict, file, indent=4)