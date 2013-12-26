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
        self.limit = -100
        self.trans = []

    def __getitem__(self, index):
        return self.trans[index]
        
    def withdraw(self,amount):
        if self.state != 'FR' or 'OD':
            self.balance -= amount
            self.trans.append(-amount)
            if self.balance.__abs__() != self.balance:
                self.state = 'DR'
            else:
                self.state = 'CR'
            if self.balance < self.limit:
                self.state = 'OD'
        else:
            print 'Account frozen or overdrawn'

    def deposit(self,amount):
        if self.state != 'FR':
            self.balance =+ amount
            self.trans.append(amount)
            if self.balance.__abs__() != self.balance:
                self.state = 'DR'
            else:
                self.state = 'CR'
            if self.balance < -100:
                self.state = 'OD'
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

    def get_transactions(self):
        return self.trans
    

class PAccount(Account):
    pass



b1 = Account('gerry')
# tests
assert b1.get_balance()[1] == 0
b1.deposit(100)
assert b1.get_balance()[1] == 100
b1.withdraw(500)
assert b1.get_balance()[1] == -400


p1 = PAccount('ann')

assert p1.get_balance()[1] == 0


print 'All tests passed'
