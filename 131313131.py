class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append('Внесение наличных на счёт: ' + amount)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append('Снятие наличных: ' + amount)
        else:
            print('Недостаточно средств на счёте')

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append("Начислены проценты по вкладу:" + interest)

    def history(self):
        for transaction in self.__transactions:
            print(transaction)
