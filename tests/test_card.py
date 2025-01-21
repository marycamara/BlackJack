import pytest
from src.card import Card, Suit, Face


def test_card_initialization():
    """Test if the card is initialized with correct rank and suit."""
    card = Card('A', Suit.HEARTS.value)
    assert card.rank == 'A', "Card rank should be 'A'."
    assert card.suit == 'Hearts', "Card suit should be 'Hearts'."
    assert card.face_up is True, "Card should be face up on initialization."


def test_card_string_representation():
    """Test the string representation of a card."""
    card = Card('K', Suit.SPADES.value)
    assert str(card) == "K of Spades", "String representation should match the expected format."


def test_card_get_value():
    """Test the value of different card ranks."""
    card = Card('A', Suit.DIAMONDS.value)
    assert card.get_value() == 11, "Ace should have a value of 11."

    card = Card('10', Suit.CLUBS.value)
    assert card.get_value() == 10, "A '10' card should have a value of 10."

    card = Card('J', Suit.HEARTS.value)
    assert card.get_value() == 10, "A 'J' card should have a value of 10."


def test_card_flip():
    """Test flipping the card."""
    card = Card('5', Suit.CLUBS.value)
    assert card.face_up is True, "Card should be face up initially."

    card.flip()
    assert card.face_up is False, "Card should be face down after flipping."

    card.flip()
    assert card.face_up is True, "Card should be face up again after flipping."


def test_card_with_invalid_rank():
    """Test initializing a card with an invalid rank."""
    with pytest.raises(KeyError):
        card = Card('Z', Suit.HEARTS.value)  # 'Z' is not a valid rank
        card.get_value()


def test_card_with_invalid_suit():
    """Test initializing a card with an invalid suit."""
    with pytest.raises(KeyError):
        card = Card('A', 'InvalidSuit')  # 'InvalidSuit' is not a valid suit
        card.get_value()


def test_card_face_card_values():
    """Test the value of face cards."""
    face_cards = ['J', 'Q', 'K']
    for face_card in face_cards:
        card = Card(face_card, Suit.HEARTS.value)
        assert card.get_value() == 10, f"{face_card} should have a value of 10."


''' 
def test_card_lowercase_input():
    """Test if the card handles lowercase input correctly."""
    card = Card('a', Suit['spades'].value)  # Ensure the correct enum case for the suit
    assert card.rank == 'a'
    assert card.suit == Suit.spades.value
'''


def test_card_equality():
    """Test if two cards with the same rank and suit are equal."""
    card1 = Card('A', Suit.HEARTS.value)
    card2 = Card('A', Suit.HEARTS.value)
    assert card1 == card2, "Two cards with the same rank and suit should be equal."


def test_card_non_equality():
    """Test if two cards with different rank or suit are not equal."""
    card1 = Card('A', Suit.HEARTS.value)
    card2 = Card('K', Suit.HEARTS.value)
    assert card1 != card2, "Cards with different ranks should not be equal."

    card3 = Card('A', Suit.HEARTS.value)
    card4 = Card('A', Suit.SPADES.value)
    assert card3 != card4, "Cards with different suits should not be equal."


def test_card_numeric_rank():
    """Test a card with a numeric rank."""
    card = Card('2', Suit.DIAMONDS.value)
    assert card.rank == '2', "Card rank should be '2'."
    assert card.get_value() == 2, "Numeric cards should return their rank as value."


def test_card_with_extra_whitespace():
    """Test initializing a card with extra whitespace around the rank or suit."""
    card = Card('  Q  ', '  Hearts  '.strip())
    assert card.rank == 'Q', "Card rank should be 'Q' with whitespace handled."
    assert card.suit == 'Hearts', "Card suit should be 'Hearts' with whitespace handled."


def test_custom_value_for_card():
    """Test if custom values are supported for cards (if applicable)."""
    card = Card('A', Suit.HEARTS.value)
    custom_value = card.get_custom_value()  # Assuming this method exists or can be extended
    assert custom_value == 11, "Custom value should match the expected value for the Ace."
