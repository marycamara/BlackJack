# betting_system.py
# Manages bets and player funds.

class BettingSystem:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        
        
    def place_bet(self, amount):
        if amount > self.balance:
            print(f"Insuffient funds! You only have £{self.balance}.")
            return False
        
        elif amount <=0:
            print("Bet amount must be greater than zero.")
            return False
        
        self.balance -= amount
        print(f"Bet of £{amount} placed. Reamining balance: £{self.balance}")
        return True
    
    def update_balance(self, amount):
        self.balance += amount
        print(f"Your balance is now £{self.balance}.")
        
    def get_balance(self):
        return self.balance
        
