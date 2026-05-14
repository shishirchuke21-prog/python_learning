class BankAccount:
    def __init__(self,name,balance):   #__init__    → sets up data when object is born
        self.name=name
        self.balance=balance

    def __str__(self):   #__str__     → reads and displays current state
        return(f"account name {self.name} \n balance is {self.balance}")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self,amount):
        if (self.balance<amount):
            print("low balance !!")
        else:
         self.balance = self.balance- amount
        
account = BankAccount("Shishir", 1000)
print(account)
account.deposit(500)
print(account) 
account.withdraw(200) 
print(account)   
account.withdraw(2000)
print(account) 

