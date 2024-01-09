"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""
import sys
if len(sys.argv) == 3:
    file = sys.argv[2]
    with open(file, 'w') as f:
        f.write(sys.argv[1])
else:
    print('Опять ошибка...')