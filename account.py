class Account(object):
    num_accs = 0
    def __init__(self,name):
        Account.num_accs += 1
        self.account_number = Account.num_accs
        self.name = name
        self.balance = 0
        self.state = 'CR'
        
    def withdraw(self,amount):
        if self.state != 'FR':
            self.balance -= amount
            if self.balance.__abs__() != self.balance:
                self.state = 'DR'
            else:
                self.state = 'CR'
        else:
            print 'Account frozen'

    def deposit(self,amount):
        if self.state != 'FR':
            self.balance =+ amount
            if self.balance.__abs__() != self.balance:
                self.state = 'DR'
            else:
                self.state = 'CR'
        else:
            print 'Account frozen'
        
    def get_balance(self):
        return self.account_number,self.balance,self.state

    def freeze(self):
        self.state = 'FR'

    def unfreeze(self):
        if self.balance.__abs__() != self.balance:
            self.state = 'DR'
        else:
            self.state = 'CR'
    




b1 = Account('gerry')
# tests
assert b1.get_balance()[1] == 0
b1.deposit(100)
assert b1.get_balance()[1] == 100
b1.withdraw(500)
assert b1.get_balance()[1] == -400

print 'All tests passed'
