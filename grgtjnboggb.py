def precedence(m):
    if (m == '+' or m == '-'):
        return(1)
    elif m == '*' or m == '/':
        return(2)
    elif m == '^':
        return(3)
    else:
        return(-1)


def main():
    mathematical_operator = input("Введите оператор: ")
    a_priority = precedence(mathematical_operator)
    if a_priority == 1:
        print('Приоритет 1')
    elif a_priority == 2:
        print('Приоритет 2')
    elif a_priority == 3:
        print('Приоритет 3')
    else:
        print('Неккорректный ввод')

if __name__ == "__main__":
    main()