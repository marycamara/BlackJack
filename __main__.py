# __main__.py
from src.game import Game
from src.menu import BlackjackMenu


def main():
    """ Start the Blackjack game menu. """
    menu = BlackjackMenu() # Instance for the menu
    choice = menu.display_menu() # Get user's choice 
    
    if choice == "1":
        """ Starts the Blackjack game if choosen  """
    game = Game() #  Create an instance for the game 
    game.play_game() # Runs the game after the menu has been display and the game option has been choosen. 
  

if __name__ == "__main__":
    main() # sStarts the game after menu interaction 
