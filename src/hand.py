class Hand:
    """Represents a player's hand of cards."""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        if card:
            self.cards.append(card)

    def calculate_total(self):
        """Calculates the total value of the hand."""
        total = 0
        ace_count = 0
        for card in self.cards:
            if card.rank in ['J', 'Q', 'K']:
                total += 10
            elif card.rank == 'A':
                total += 11
                ace_count += 1
            else:
                total += int(card.rank)

        # Adjust for Aces
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1

        return total
