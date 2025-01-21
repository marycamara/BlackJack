from  src.deck import Deck
from  src.interface import Interface
from  src.player import Player
from  src.ai_player import AIPlayer



class Game:
    def __init__(self, max_players=4):
        self.deck = Deck()
        self.interface = Interface(max_players)  # Pass the max players limit
        self.players = []

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
        self.interface.display_table([(player.name, player.hand, player.calculate_total(), 'human' if not isinstance(player, AIPlayer) else 'ai') for player in self.players])
        for player in self.players:
            if not player.is_busted():
                self.player_turn(player)

    def player_turn(self, player):
        """Handles each player's turn (human or AI)."""
        if isinstance(player, AIPlayer):
            action = player.decide_action()
            print(f"\nAI's turn: {action.upper()}")
            if action == 'h':
                card = self.deck.draw_card()
                player.hand.add_card(card)
                print(f"AI hits and receives the {card}.")
                if player.is_busted():
                    self.interface.display_busted(player.name)
                    return
        else:
            action = self.interface.prompt_action(player.name)
            if action == 'h':
                card = self.deck.draw_card()
                player.hand.add_card(card)
                print(f"{player.name} hits and receives the {card}.")
                if player.is_busted():
                    self.interface.display_busted(player.name)
                    return

    def play_game(self):
        """Starts the game and handles the rounds."""
        self.interface.display_welcome_message()
        num_players = self.interface.prompt_num_players()

        # Add the players (including one AI player)
        for i in range(1, num_players + 1):
            player_name = self.interface.prompt_player_name(i)
            self.players.append(Player(player_name))

        # Add one AI player at the end
        self.players.append(AIPlayer())

        self.deal_initial_cards()

        self.play_round()

        self.interface.display_final_results([(player.name, player.hand, player.calculate_total(), 'human' if not isinstance(player, AIPlayer) else 'ai') for player in self.players])