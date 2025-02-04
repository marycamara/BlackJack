# menu.py 
from src.game import Game 

class BlackjackMenu:
    def __init__(self):
        self.running = True
    
    
    def display_menu(self):
        while self.running:
            print("\n===================Main Menu===================")
            print("1. Start Game")
            print("2. View Rules")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            self.handle_choice(choice)
            
    def handle_choice(self, choice):
        if choice == "1":
            print("\nStarting game.........\n")
            game = Game() # Create an instance of the game
            game.play_game() # Call the game function 
            self.running = False # Exit the loop menu after playing 
               
        
        elif choice == "2":
            self.show_rules()
                
        elif choice == "3":
            print("\nExiting game. Goodbye") 
            self.running = False # Exiting the loop   
            
        else:
            print("\Invalid choice. Please enter 1,2 or 3")
                
    def show_rules(self):
        print("==== BlackJack Rules ====")
        print("1.Try to get as close to 21 as possible without exceeding it. ")
        print("2. Face cards are worth 10, Aces are worth 1 or 11.")
        print("3. Players can hit (draw a card) or stand (keep their hand).")
        print("4. The dealer must hit on 16 and stand on 17.")
        print("5. The closest hand to 21 without going over wins!\n")