import pytest
from src.deck import Deck
from src.card import Card


@pytest.fixture
def deck():
    """Fixture to create a fresh deck before each test."""
    return Deck()


def test_deck_initialization(deck):
    """Test if the deck is initialized correctly with 52 cards."""
    assert len(deck.cards) == 52, "Deck should contain 52 cards."
    # Verify that all cards are unique
    unique_cards = set((card.rank, card.suit) for card in deck.cards)
    assert len(unique_cards) == 52, "Deck should contain 52 unique cards."


def test_shuffle(deck):
    """Test if shuffle changes the order of the cards."""
    original_order = deck.cards.copy()
    deck.shuffle()
    # Assert that the shuffled deck is not in the same order
    assert deck.cards != original_order, "Shuffle should change the order of cards."
    # Ensure deck still has 52 cards after shuffling
    assert len(deck.cards) == 52, "Deck should still contain 52 cards after shuffling."


def test_draw_card(deck):
    """Test if drawing a card removes it from the deck."""
    card_before = deck.cards[-1]  # Last card in the deck
    drawn_card = deck.draw_card()
    assert drawn_card == card_before, f"Expected card {card_before}, but got {drawn_card}."
    assert len(deck.cards) == 51, "Deck should contain 51 cards after drawing a card."


def test_remaining_cards(deck):
    """Test if the number of remaining cards is accurate after drawing cards."""
    deck.draw_card()  # Remove one card
    assert deck.remaining_cards() == 51, "Remaining cards should be 51 after drawing one card."


def test_draw_empty_deck():
    """Test if drawing a card from an empty deck returns None."""
    deck = Deck()
    # Remove all cards from the deck
    while deck.remaining_cards() > 0:
        deck.draw_card()
    
    drawn_card = deck.draw_card()  # Try to draw from an empty deck
    assert drawn_card is None, "Drawing from an empty deck should return None."


def test_deck_after_draw(deck):
    """Test if drawing multiple cards decreases the number of remaining cards."""
    initial_count = deck.remaining_cards()
    # Draw a card and check if the remaining cards decrease by 1
    deck.draw_card()
    assert deck.remaining_cards() == initial_count - 1, "Deck should have one less card after a draw."


def test_deck_reset(deck):
    """Test if resetting the deck properly reinitializes it to 52 cards."""
    deck.draw_card()  # Remove one card
    deck.reset()  # Reset the deck
    assert len(deck.cards) == 52, "Deck should contain 52 cards after reset."


def test_card_class():
    """Test if the Card class behaves as expected."""
    card = Card('Ace', 'Spades')
    assert card.rank == 'ACE', "Card rank should be 'ACE'."  # Check uppercase rank
    assert card.suit == 'Spades', "Card suit should be 'Spades'."
    assert str(card) == 'ACE of Spades', "String representation should match 'ACE of Spades'."

