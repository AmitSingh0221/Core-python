class Account:

    def __init__(self):
        print("Account details ")

        self.__account_type = None
        self.__account_number = None
        self.__account_mode = None
        self.__account_balance = 0.0

    def get_account_type(self):
        return self.__account_type

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_mode(self):
        return self.__account_mode

    def set_account_mode(self, account_mode):
        self.__account_mode = account_mode

    def get_account_balance(self):
        return self.__account_balance

    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance


a1 = Account()

a1.set_account_type("Savings")
a1.set_account_number(1234567890)
a1.set_account_mode("Online")
a1.set_account_balance(5587.85)

print("Account Type :", a1.get_account_type())
print("Account Number :", a1.get_account_number())
print("Account Mode :", a1.get_account_mode())
print("Balance :", a1.get_account_balance())

a2 = Account()

a2.set_account_type("Current")
a2.set_account_number(985214763)
a2.set_account_mode("Net Banking")
a2.set_account_balance(123654.54)

print("Account Type :", a2.get_account_type())
print("Account Number :", a2.get_account_number())
print("Account Mode :", a2.get_account_mode())
print("Balance :", a2.get_account_balance())

