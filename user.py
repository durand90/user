

from cgi import print_directory


class User:
    def __init__(self, name, email, age, account):
        self.name = name
        self.email = email
        self.age = age
        self.account = account

    def balance(self):
        print(f'name: {self.name}')
        print(f'email: {self.email}')
        print(f'age: {self.age}')
        print (f'amount: {self.amount}')
        return self

    def withdrawal(self, account):
        self.account -= account
        return self

    def deposit(self, account):
        self.account += account
        return self

fanfan_account = User('fanfan', 'live@yahoo.com', 37, 200)
joey_account = User('joey', 'kick@hotmail.com', 42, 1000)

fanfan_account.balance().withdrawal(70).deposit(25).info()