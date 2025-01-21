import random
from .card import Card


class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def draw_card(self):
        """Draws the top card from the deck and updates the deck status."""
        card = self.cards.pop() if self.cards else None
        if card:
            print(f"Drew card: {card}")
        return card

    def remaining_cards(self):
        """Returns the number of remaining cards in the deck."""
        return len(self.cards)
    
    def reset(self):
        """Resets the deck to its initial state with 52 cards."""
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()  # Shuffle the deck after resetting.
