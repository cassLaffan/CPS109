'''
More Class Examples!
'''
class BankAccount:
    # This is a class attribute!
    total_accounts = 0
    
    def __init__(self, balance):
        self.balance = balance
        BankAccount.total_accounts += 1

    @property
    def USD(self):
        return self.balance * 0.72
    
    @USD.setter
    def USD(self, value):
        self.balance = value * 0.72
    
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)


if __name__ == "__main__":
    ba = BankAccount(1000)
    print(ba.USD)

    ba.USD = 8000

    print(ba.balance)