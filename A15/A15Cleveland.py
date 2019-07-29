class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def dump(self):
        print ("Dump Account Info")
        s = '%s, %s, balance: %s\n' % (self._name, self._no, self._balance)
        print (s)
        
# Main
print ("Assignment 15 - written by Matt Weisfeld")
