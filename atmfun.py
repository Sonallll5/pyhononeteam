class Banking:
    def __init__(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
    def display (self):
        print()
        print("_____account details_______")
        print("Account holder name:",self.name)
        print("Account number :",self.acc_no)

    def deposit(self,deposit):
        self.dp=deposit
        self.balance=self.balance+self.dp
        print("amount add")

    def withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("Amount withdraw")
        else:
            print("less amount")

    def get_balance(self):
        return self.balance

name=input("Enter te name")
acc_no=int(input("Account number"))
obj=Banking(name,acc_no)
obj.display()
print()
print("1 . Deposit")
print("2 . withdraw")
print("3 . view")
print("4 . Exit")

while(True):
    n=int(input("Enter ur choice"))
    if n==1:
        deposit=int(input("ENter The Amount"))
        obj.deposit(deposit)
    elif n==2:
        wrd=int(input("Enter the Amount"))
        obj.withdraw(wrd)
    elif n==3:
       print( obj.get_balance())
    elif n==4:
        print("Exit")
        break
    else:
        print("Invalid")
    
