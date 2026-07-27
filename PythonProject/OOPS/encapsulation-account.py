class BankAccount:

    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(5000)
account.withdraw(2000)

print(account.get_balance())