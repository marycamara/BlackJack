from .hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()  # Assuming you have a Hand class that contains the player's cards

    def calculate_total(self):
        total = 0
        ace_count = 0

        for card in self.hand.cards:
            if card.rank in ['J', 'Q', 'K']:  # Face cards are worth 10
                total += 10
            elif card.rank == 'A':  # Ace can be 1 or 11
                total += 11
                ace_count += 1
            else:
                total += int(card.rank)  # Number cards are worth their face value

        # Adjust for Aces being worth 1 if the total exceeds 21
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1

        return total

    def is_busted(self):
        # Returns True if the player's total exceeds 21 (busted)
        return self.calculate_total() > 21
