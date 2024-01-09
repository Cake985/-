"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import os
import sys
if len(sys.argv) == 3:
    path = sys.argv[1]
    target_name = sys.argv[2]
    target_path = os.path.join(path, target_name)
    os.mkdir(target_path)
else:
    print('опять этот каплан')