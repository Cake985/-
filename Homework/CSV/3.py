"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
import csv

data = [
    ["Название", "Препод", "Любовь"],
    ["Вышмат", "Борис", 100],
    ["Прога", "Олег", 11],
    ["ОС", "Выживалово", 8],
    ["Компы", "Торшин", 1000]
]
filename = "klapan.csv"
with open(filename, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print(f'создал {filename} и ушел спать')