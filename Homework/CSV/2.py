"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
import csv
dict_csv = {}

with open('Task1.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for i in reader:
        dict_csv[(i[0], i[1])] = {i[2] : i[3]}
    print(dict_csv)