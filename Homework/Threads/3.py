"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time

def reminder_thread():
    while True:
        print("Вводите быстрее")
        time.sleep(3)

reminder_thread = threading.Thread(target=reminder_thread, daemon=True)

reminder_thread.start()

try:
    bomb_code = input("Введите код от бомбы: ")
    if bomb_code == "12345":
        print("Бомба разминирована")
    else:
        print("Вы взорвались")
except KeyboardInterrupt:
    print("Программа прервана пользователем")