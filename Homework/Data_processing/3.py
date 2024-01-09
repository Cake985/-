"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
temperatur = [20, 25, 30, 35]
def kaplan(temperatur):
    for temp in temperatur:
        print("Сегодня {} градусов".format(temp))
kaplan(temperatur)