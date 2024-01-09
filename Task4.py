
'''z = [7, 8]
z.append(5)
y = [8, 9]
print(type(z))'''
'''объект - единица информации в памяти
экземпляр - конкретный объект какого-го класса
класс - инструкция по созданию объектов определённого типа
метод - функция в классе для воздействия на объект'''

#from tkinter import Tk
#root = Tk()
#root.mainloop()

class Purse:
    def __init__(self, valuta, name = 'Unknown'):
        self.money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.money = self.money + howmany

    def top_down_balance(self, howmany):
        if self.money < 0:
            print('Не достаточно средств')
            raise ValueError('Недостаточно средств')
        self.money = self.money - howmany

    def info(self):
        return self.money

    def __del__(self):
        print('Кошелёк удалён')

x = Purse('USD')
y = Purse('EUR','Bill')

x.top_up_balance(100)
x.money = 200
x.info()
