from tabulate import tabulate
from colorama import Fore, Style
from .hand import Hand
import time

class Interface:
    def __init__(self, max_players=4):
        self.game_started = False
        self.max_players = max_players  # Maximum number of players
        self.card_symbols = {
            'hearts': '♥',
            'diamonds': '♦',
            'clubs': '♣',
            'spades': '♠'
        }

    def display_welcome_message(self):
        """Displays the welcome message at the start of the game."""
        print(Fore.GREEN + Style.BRIGHT + "Welcome to Blackjack!" + Style.RESET_ALL)
        print(Fore.MAGENTA + "=" * 40 + Style.RESET_ALL)  # More prominent separator

    def prompt_num_players(self):
        """Prompts the user to input the number of players, with a limit."""
        while True:
            try:
                num_players = int(input(f"Enter the number of players (max {self.max_players}): "))
                if num_players < 1 or num_players > self.max_players:
                    print(f"Please enter a number between 1 and {self.max_players}.")
                    continue
                return num_players
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def prompt_player_name(self, player_num):
        """Prompts the user to input a player's name."""
        player_name = input(f"Enter the name for player {player_num}: ")
        return player_name

    def display_table(self, players_info):
        """Displays the current state of the table (players, their hands, and totals)."""
        print(Fore.RED + "\n" + "=" * 40 + Style.RESET_ALL)  # Use clear separator
        print(Fore.RED + "Current Game State:" + Style.RESET_ALL)

        table_headers = ['Rank', 'Player Name', 'Hand', 'Total']
        table_rows = []

        for index, player_info in enumerate(players_info):
            name, hand, total, player_type = player_info
            # Colour code the player's name based on their type
            if player_type == 'human':
                name_colored = Fore.GREEN + name + Style.RESET_ALL  # Player in green
            else:
                name_colored = Fore.YELLOW + name + Style.RESET_ALL  # AI in yellow

            # Format the hand
            hand_str = ', '.join([f"{card.rank} of {self.card_symbols.get(card.suit, card.suit)}" for card in hand.cards])
            table_rows.append([index + 1, name_colored, hand_str, total])

        # Display the table after each round
        print(tabulate(table_rows, headers=table_headers, tablefmt='fancy_grid', stralign='center'))
        print(Fore.RED + "=" * 40 + Style.RESET_ALL)  # Clear separator after the table

    def display_busted(self, player_name):
        """Displays a message when a player busts."""
        print(Fore.RED + f"{player_name} has busted!" + Style.RESET_ALL)

    def prompt_action(self, player_name):
        """Prompts the player (human) for an action (hit or stand)."""
        action = ''
        while action not in ['h', 's']:
            action = input(f"{player_name}, do you want to (h)it or (s)tand? ").lower()
        return action

    def display_final_results(self, players_info):
        """Displays the final results in a table format, ranked by total score."""
        # Sort players by total score, highest first
        players_info_sorted = sorted(players_info, key=lambda x: x[2], reverse=True)
        
        # Prepare the table for final results
        table_headers = ['Rank', 'Player Name', 'Hand', 'Total']
        table_rows = []
        
        for index, player_info in enumerate(players_info_sorted):
            rank = index + 1
            name, hand, total, player_type = player_info
            # Format the hand
            hand_str = ', '.join([f"{card.rank} of {self.card_symbols.get(card.suit, card.suit)}" for card in hand.cards])
            table_rows.append([rank, name, hand_str, total])

        # Print the final result in a table format
        print(Fore.RED + "\n" + "=" * 40 + Style.RESET_ALL)  # Clear separator before final results
        print(Fore.RED + "Final Results:" + Style.RESET_ALL)
        print(tabulate(table_rows, headers=table_headers, tablefmt='fancy_grid', stralign='center'))
        print(Fore.RED + "=" * 40 + Style.RESET_ALL)  # Clear separator after final results

    def display_deck_status(self, remaining_cards):
        """Displays the number of remaining cards in the deck."""
        print(Fore.RED + f"Remaining cards in deck: {remaining_cards}" + Style.RESET_ALL)

    def display_shuffling(self):
        """Displays shuffling animation."""
        print(Fore.RED + "=" * 40 + Style.RESET_ALL)  # Add a separator for clarity
        print(Fore.RED + "Shuffling deck..." + Style.RESET_ALL)
        time.sleep(1)  # Simulate time for shuffling
        print(Fore.RED + "Deck shuffled!" + Style.RESET_ALL)
        print(Fore.RED + "=" * 40 + Style.RESET_ALL)  # Clear separator after shuffling

    def draw_card(self):
        """Displays the drawing of a card in red."""
        print(Fore.RED + "Drawing a card..." + Style.RESET_ALL)
