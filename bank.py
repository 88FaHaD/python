class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

# Example usage
account1 = BankAccount("12345")
account1.deposit(1000)
account1.display_balance()
account1.withdraw(500)
account1.display_balance()
