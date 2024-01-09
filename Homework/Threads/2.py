"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time

def reminder_thread():
    reminder_text = input("О чем напомнить? ")
    delay_seconds = int(input("Через сколько секунд напомнить? "))

    time.sleep(delay_seconds)
    print(f"Напоминание: {reminder_text}")

reminder_thread = threading.Thread(target=reminder_thread)

reminder_thread.start()

try:
    time.sleep(10)
    print("Программа завершается")
except KeyboardInterrupt:
    print("Программа прервана пользователем")

reminder_thread.join()