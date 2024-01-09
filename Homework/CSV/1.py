"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""
import csv

with open('Task1.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))
    for i in reader:
        print(f'{i[0]} - {i[3]}')