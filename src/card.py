from enum import Enum

class Face(Enum):
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'

class Card:
    def __init__(self, rank, suit):
        # Capitalize the suit to match the Enum values
        suit = suit.strip().capitalize()
        if suit not in [s.value for s in Suit]:
            raise KeyError(f"Invalid suit: {suit}")
        
        self.rank = rank.strip().upper()  # Ensure the rank is uppercase and strip whitespace
        self.suit = suit
        self.face_up = True

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def get_value(self):
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
        return card_values[self.rank]

    def flip(self):
        """Flip the card (face up or face down)."""
        self.face_up = not self.face_up

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False

    def get_custom_value(self):
        # Implement custom value logic if necessary
        return self.get_value()
