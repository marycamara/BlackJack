from .player import Player 

class AIPlayer(Player):
    def __init__(self, name="AI"):
        super().__init__(name)

    def decide_action(self):
        """AI decides whether to hit or stand based on the current hand total."""
        total = self.calculate_total()
        
        # Basic strategy: stand on 17 or higher, hit otherwise
        if total >= 17:
            return 's'  # Stand
        return 'h'  # Hit
