"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
import threading
import queue

def add_student_to_queue(student_queue):
    while True:
        surname = input("Введите фамилию студента или 'off' для завершения: ")
        if surname.lower() == 'off':
            break
        student_queue.put(surname)

def expel_student_from_queue(student_queue):
    while True:
        expelled_student = student_queue.get()
        print(f"Студент {expelled_student} отчислен.")

if __name__ == "__main__":
    student_queue = queue.Queue()
    initial_students = ['Иванов', 'Петров']
    for student in initial_students:
        student_queue.put(student)
    add_thread = threading.Thread(target=add_student_to_queue, args=(student_queue,))
    add_thread.start()
    expel_thread = threading.Thread(target=expel_student_from_queue, args=(student_queue,))
    expel_thread.start()
    add_thread.join()
    print("Основной поток завершен.")