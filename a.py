class BankAccount: 
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float) -> float: 
        if amount <= 0:
            raise ValueError("deposit amt must be positive")
        self.balance += amount
        print(f"Deposited ${amount: .2f}. New Balance: ${self.balance: .2f}")
        return self.balance 
    def withdraw(self, amount: float) -> float: 
        if amount <= 0: 
            raise ValueError("deposit amt must be positive")
        if self.balance < amount: 
            raise ValueError("insufficient funds")
        
        self.balance  -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return self.balance

acc = BankAccount("Kishore", 100.0)
acc.deposit(50.0)
acc.withdraw(30.0)