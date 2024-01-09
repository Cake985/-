"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

def find_divisors(number, result_queue):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    result_queue.put((number, divisors))

if __name__ == "__main__":
    numbers_queue = queue.Queue()
    initial_numbers = [12, 20, 30, 42]

    for number in initial_numbers:
        numbers_queue.put(number)

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(find_divisors, number, numbers_queue) for number in initial_numbers]

        for future in futures:
            future.result()

    while not numbers_queue.empty():
        number, divisors = numbers_queue.get()
        print(f"Делители числа {number}: {divisors}")