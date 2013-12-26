import account

class PAccount(Account):
    pass


p1 = PAccount('ann')

assert p1.get_balance()[1] == 0

print 'ok'
