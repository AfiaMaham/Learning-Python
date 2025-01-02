# 1. Bank Account
# Create a class BankAccount with attributes account_number and balance. Initialize these in the constructor and create methods for:

# Deposit (adds to the balance)
# Withdraw (subtracts from the balance if sufficient funds exist)
# Check balance


class BankAccount:
    def __init__(self, num, bal):
        self.accountNum = num
        self.balance = bal

    def Deposit(self): 
        amount = int(input("Enter the amount: "))   
        self.balance += amount
        print("amount deposited successfully......")
    def Withdraw(self):
         amount = int(input("Enter the amount: "))   
         if(self.balance < amount):
             print("Insufficient balance")
         else:
           self.balance -= amount
           print(f"Account Number: {self.accountNum}\nBalance: {self.balance}")
         
    def Check(self):
           print(f"Account Number: {self.accountNum}\nBalance: {self.balance}")
    
obj = BankAccount(1111,10000)
obj.Deposit()
obj.Check()
obj.Withdraw()