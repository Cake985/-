"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""
import os
b = os.environ['COMPUTERNAME']
c = os.getlogin()
print(os.name)
print(b)
print(c)