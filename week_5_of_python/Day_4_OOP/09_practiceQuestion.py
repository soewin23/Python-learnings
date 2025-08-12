# Create Account class with 2 attributes- balance & account no.
# Create methods for debt and printing the balance


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc = acc

#debit method
    def debit(self,ammount):
        self.balance -= ammount 
        print(f"$. {ammount}, was dibited")
        print(f"total balance is = {self.get_balance()}")

#credit method
    def credit(self,ammount):
        self.balance += ammount 
        print(f"$. {ammount}, was credited")
        print(f"total balance is = {self.get_balance()}")


    def get_balance(self):
        return self.balance

bal = int(input("Enter balance to dibit :"))
acc = int(input("Enter your banak account :"))
        
acc1 = Account(bal, acc)
acc1.debit(9000)
acc1.credit(40000)
acc1.debit(10000)


