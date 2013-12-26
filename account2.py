class OverDrawnException(Exception):
    pass

class Account(object):
    num_accs = 0

    @staticmethod
    def get_num_accs():
        return Account.num_accs
    
    def __init__(self,name):
        Account.num_accs += 1
        self.account_number = Account.num_accs
        self.name = name
        self.balance = 0
        self.state = 'CR'
        
    def withdraw(self,amount):
        if amount > self.balance:
            raise(OverDrawnException, 'Overdrawn')
        else:
            self.balance -= amount

    def deposit(self,amount):
        self.balance =+ amount
        
    def get_balance(self):
        return self.account_number,self.balance,self.state

    def freeze(self):
        self.state = 'FR'

    def unfreeze(self):
        if self.balance.__abs__() != self.balance:
            self.state = 'DR'
        else:
            self.state = 'CR'
    

class PAccount(Account):

    def withdraw(self,amount):
        if amount > (self.balance + 50):
            raise(OverDrawnException, 'PAccount Overdrawn')
        else:
            self.balance -= amount


try:
    b1 = Account('gerry')
    # tests
    assert b1.get_balance()[1] == 0
    b1.deposit(100)
    assert b1.get_balance()[1] == 100
    b1.withdraw(100)
    assert b1.get_balance()[1] == 0
    p1 = PAccount('ann')
    assert p1.get_balance()[1] == 0
    p1.withdraw(51)
except(OverDrawnException):
    print 'Overdrawn' 
else:
    print 'All tests passed'
