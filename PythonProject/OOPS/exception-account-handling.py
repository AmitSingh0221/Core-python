from itertools import count
from logging import exception


class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class FundExceedingLimit(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Current Balance: {self.balance}")

        if amount > 100000:
            raise FundExceedingLimit("you cannot deposit 100000 in a single transaction.")

    def withdrawal(self, amount):
        if amount > 20000:
            raise FundExceedingLimit("You cannot withdraw more than ₹20000 in a single transaction.")

        if self.count >= 3:
            raise InsufficientFundException("Withdrawal limit exceeded. Maximum 3 withdrawals allowed.")

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdraw: {amount}, Remaining Balance: {self.balance}")
        else:
            raise InsufficientFundException("Insufficient balance. Minimum ₹2000 must remain in the account.")


# Example
acc = Account()
acc.set_balance(50000)
print(acc.get_balance())

try:
    acc.deposit(11000)
    acc.withdrawal(20000)
    acc.withdrawal(20000)
    acc.withdrawal(15000)
    acc.withdrawal(1000)
                                 # acc.withdrawal(1000)
                                 # will raise exception (balance would go below 2000)
                                 # acc.withdrawal(2500)  # will raise exception (balance would go below 2000)
except Exception as e:                   #if there is only one exception class then we'll call that excepton class
    print("exception:", e)               #if there is 2 or more exception class then we'll use {Exception} for calling all exception class
