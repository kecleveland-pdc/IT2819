class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!!\n")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def dump(self):
        s = ("Dump Account Info: {0}, {1}, balance of {2}\n\nFinal balance: {3}".format(self._name, self._no, self._balance, self._balance))
        return s
# Main
print ("Assignment 15 - written by Keaunna Cleveland\n")
JohnSmith = AccountP('John Smith', '19371554951', 20000)
JohnSmith.deposit(1000)
JohnSmith.withdraw(4000)
JohnSmith.withdraw(3500)
print(JohnSmith.dump())