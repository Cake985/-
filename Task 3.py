'''a = int(input())
b = int(input())
q = 0
for a in range(a, b+1):
    print(a)
    q = q+1
print('кол-во чисел:', q)'''

'''prace = int(input())
i = 1
for i in range(1, 11):
    print('Стоимость',i,'кг. конфет',prace*i)'''


'''ch = int(input())
k = int(input())
su = 0
for ch in range(1, ch + 1):
    if k < 0:
        su = su+k
print(su)'''

'''import math
a = 5.6
print(round(a)) #округление по факту
print(math.floor(a)) #округление в меньшую принудительно
print(math.ceil(a))  #округление в большую принудительно
print(math.pi)'''

'''a = input()
print(type(a))'''#число или текст

'''x =int(input())
if x == 0:
    print('x был равен нулю')
    x = 1
elif type(x) == type(5) or type(x) == type(5.5):
    print('x допустимое значение')
else:
    print('В x недопустимый тип данных')
    x = 1
print(100/x)'''

'''x ='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
y = input('Введите строку:\n')
for i in x:
    count = 0
    for r in y:
        count += 1
if count > 0:
    print('Букв:', y, '-', count)'''

