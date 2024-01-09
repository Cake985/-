"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""
import sys
if len(sys.argv) == 2:
    file = sys.argv[1]
    with open(file, 'r') as f:
        for line in f:
            commands = line.strip()
            exec(commands)
else:
    print('все каплан хватит пж')