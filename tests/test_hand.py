import pytest
from src.card import Card
from src.hand import Hand

@pytest.fixture
def hand():
    """Fixture to create a fresh hand before each test."""
    return Hand()

def test_add_card(hand):
    """Test if a card is added correctly to the hand."""
    card = Card('5', 'Hearts')
    hand.add_card(card)
    assert len(hand.cards) == 1, "Hand should contain one card."
    assert hand.cards[0] == card, f"Expected {card}, but got {hand.cards[0]}."

def test_calculate_total_no_aces(hand):
    """Test the total calculation without any Aces."""
    hand.add_card(Card('5', 'Hearts'))
    hand.add_card(Card('10', 'Spades'))
    assert hand.calculate_total() == 15, "Total should be 15."

def test_calculate_total_with_aces(hand):
    """Test the total calculation with Aces as 11 initially."""
    hand.add_card(Card('A', 'Hearts'))
    hand.add_card(Card('10', 'Spades'))
    assert hand.calculate_total() == 21, "Total should be 21 with an Ace as 11."

def test_calculate_total_with_multiple_aces(hand):
    """Test the total calculation with multiple Aces, adjusting the value to avoid busting."""
    hand.add_card(Card('A', 'Hearts'))
    hand.add_card(Card('A', 'Spades'))
    hand.add_card(Card('10', 'Diamonds'))
    assert hand.calculate_total() == 12, "Total should be 12 after adjusting Aces to 1."

def test_calculate_total_with_face_cards(hand):
    """Test the total calculation with face cards (J, Q, K)."""
    hand.add_card(Card('J', 'Hearts'))
    hand.add_card(Card('Q', 'Spades'))
    hand.add_card(Card('K', 'Diamonds'))
    assert hand.calculate_total() == 30, "Total should be 30 (J+Q+K = 10 + 10 + 10)."

def test_calculate_total_busted(hand):
    """Test the total calculation when the hand exceeds 21 and Aces are adjusted to 1."""
    hand.add_card(Card('A', 'Hearts'))  # 11
    hand.add_card(Card('10', 'Spades'))  # 10
    hand.add_card(Card('10', 'Diamonds'))  # 10
    hand.add_card(Card('3', 'Clubs'))  # 3
    assert hand.calculate_total() == 24, "Total should be 24 (busted)."

def test_empty_hand_total(hand):
    """Test if the total of an empty hand is 0."""
    assert hand.calculate_total() == 0, "Empty hand should have a total of 0."

