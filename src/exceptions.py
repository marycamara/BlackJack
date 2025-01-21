class Exceptions:
    """Base class for all exceptions in the game."""
    pass

class DeckError(Exceptions):
    """Base class for exceptions related to the Deck."""
    pass

class DeckInitializationError(DeckError):
    """Raised when the Deck is not properly initialized."""
    pass

class CardError(Exceptions):
    """Base class for exceptions related to Cards."""
    pass

class InvalidCardError(CardError):
    """Raised when a Card is created with an invalid rank or suit."""
    pass
