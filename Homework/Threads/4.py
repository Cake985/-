"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import threading
import time


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        content = content.replace("ids", "id")

        with open(file_path, 'w') as file:
            file.write(content)

        print(f"Файл {file_path} обработан успешно.")
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")


def process_files_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    threads = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        thread = threading.Thread(target=process_file, args=(file_path,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = time.time()
    folder_path = "Files"
    process_files_in_folder(folder_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения программы: {elapsed_time:.2f} секунд")