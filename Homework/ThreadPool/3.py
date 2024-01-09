"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
import threading
import queue
import os

def process_names_file(file_path, queue):
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            file_path = f"{name}.txt"
            queue.put(file_path)

def create_txt_file(queue):
    while True:
        file_path = queue.get()
        if file_path == 'exit':
            break
        with open(file_path, 'w') as file:
            file.write(f"Hello, {os.path.basename(file_path)[:-4]}!")

if __name__ == "__main__":
    names_queue = queue.Queue()
    names_thread = threading.Thread(target=process_names_file, args=("Names.txt", names_queue))
    names_thread.start()
    txt_thread = threading.Thread(target=create_txt_file, args=(names_queue,))
    txt_thread.start()
    names_thread.join()
    names_queue.put('exit')
    txt_thread.join()
    print("Основной поток завершен.")