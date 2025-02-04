# game.py
from src.deck import Deck
from src.interface import Interface
from src.player import Player
from src.ai_player import AIPlayer
from src.betting_system import BettingSystem


class Game:
    def __init__(self, max_players=4, starting_balance=500):
        self.deck = Deck()
        self.interface = Interface(max_players)
        self.players = []
        self.current_bet = 0
        self.betting_system = {}
        self.starting_balance = starting_balance

    def deal_initial_cards(self):
        """Deals two cards to each player."""
        self.interface.display_shuffling()
        self.deck.shuffle()
        self.interface.display_deck_status(self.deck.remaining_cards())
        for player in self.players:
            card1 = self.deck.draw_card()
            card2 = self.deck.draw_card()
            player.hand.add_card(card1)
            player.hand.add_card(card2)

    def play_round(self):
        """Handles the game logic for one round."""
        # Display's the current game with the details 
        self.interface.display_table([
            (player.name, player.hand, player.calculate_total(),
             'human' if not isinstance(player, AIPlayer) else 'ai') 
            for player in self.players
        ])
        
        # Process each player's turn if they have not busted 
        for player in self.players:
            if not player.is_busted():  # Check if player is still in the game
                self.player_turn(player)
        
        # After all players have taken their turns, resolve bets
        self.resolve_bet()

    def player_turn(self, player):
        """Handles each player's turn (human or AI)."""
        while not player.is_busted():
            if isinstance(player, AIPlayer):
                action = player.decide_action()
                print(f"\nAI's turn: {action.upper()}")

                # AI turn logic
                if action == 'h': 
                    card = self.deck.draw_card()
                    player.hand.add_card(card)
                    print(f"AI hits and receives the {card}.")
                    if player.is_busted():
                        self.interface.display_busted(player.name)
                        break
                elif action == 's':  # AI stands
                    print("AI stands.")
                    break  # Exit loop after standing

            else:  # For human players
                action = self.interface.prompt_action(player.name)
                if action == 'h':  # Player hits
                    card = self.deck.draw_card()
                    player.hand.add_card(card)
                    print(f"{player.name} hit and receives the {card}")
                    if player.is_busted():
                        self.interface.display_busted(player.name)
                        break
                elif action == 's':  # Player stands
                    print(f"{player.name} stands.")
                    break  # Exit loop after standing

    def place_bet(self):
        """Handles bet placement for all players, prompting at the beginning of the game."""
        for player in self.players:
            if isinstance(player, AIPlayer):
                bet = 500  # Fixed bet for AI (can be dynamic based on balance)
                print(f"AIPlayer places a bet of £{bet}.")
            else:
                while True:
                    try:
                        current_balance = self.betting_system[player.name].get_balance()
                        bet = int(self.interface.prompt_bet(player.name, current_balance))
                        if bet > current_balance:
                            print(f"Insufficient balance! You only have £{current_balance}.")
                            continue

                        self.betting_system[player.name].place_bet(bet)
                        player.current_bet = bet  # saves the bet amount for this round
                        break
                    except ValueError as e:
                        print(e)

    def resolve_bet(self):
        """Resolve bets and update game state based on players' hands."""
        for player in self.players:
            if player.is_busted():
                print(f"{player.name} loses their bet of £{player.current_bet}.")
                self.betting_system[player.name].update_balance(-player.current_bet)
            
            elif player.calculate_total() > 17:
                winnings = player.current_bet * 2
                print(f"{player.name} wins £{winnings}!")
                self.betting_system[player.name].update_balance(winnings)
            else:
                print(f"{player.name} loses their bet of £{player.current_bet}.")
                self.betting_system[player.name].update_balance(-player.current_bet)


    def play_game(self):
        """Starts the game and handles the rounds."""
        self.interface.display_welcome_message()
        num_players = self.interface.prompt_num_players()

        # Add the players (including one AI player)
        for i in range(1, num_players + 1):
            player_name = self.interface.prompt_player_name(i)
            self.players.append(Player(player_name))
            self.betting_system[player_name] = BettingSystem(self.starting_balance)
        
        # Add one AI player at the end with a name
        self.players.append(AIPlayer("AI Dealer"))
        self.betting_system["AI Dealer"] = BettingSystem(self.starting_balance)
        
        self.place_bet()  # Prompt for bets before any round starts
        self.deal_initial_cards()
        self.play_round()
        
        while True:
            self.deal_initial_cards()
            self.play_round()
            
            # Display player balance 
            for player in self.players:
                balance = self.betting_system[player.name].get_balance()
                print(f"{player.name}'s balance: £{balance}")
                
            # check if players want to continue
            cont = self.interface.prompt_continue()
            if not cont:
                print("Thanks for playing!")
                break

        self.interface.display_final_results([(player.name, player.hand, player.calculate_total(), 'human' if not isinstance(player, AIPlayer) else 'ai') for player in self.players])
