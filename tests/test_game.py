import pytest
from unittest.mock import MagicMock
from src.game import Game
from src.deck import Deck
from src.interface import Interface
from src.player import Player
from src.ai_player import AIPlayer

@pytest.fixture
def game():
    game_instance = Game()
    game_instance.deck = MagicMock(Deck)
    game_instance.interface = MagicMock(Interface)

    # Mock players
    player_mock = MagicMock(Player)
    player_mock.name = "Player1"
    player_mock.hand = MagicMock()
    player_mock.hand.add_card = MagicMock()
    player_mock.calculate_total.return_value = 15
    player_mock.is_busted.return_value = False

    ai_player_mock = MagicMock(AIPlayer)
    ai_player_mock.name = "AI"
    ai_player_mock.hand = MagicMock()
    ai_player_mock.hand.add_card = MagicMock()
    ai_player_mock.calculate_total.return_value = 17
    ai_player_mock.is_busted.return_value = False

    game_instance.players = [player_mock, ai_player_mock]

    return game_instance

def test_game_initialization(game):
    # Ensure the game starts with the mocked players
    assert len(game.players) == 2
    assert game.players[0].name == "Player1"
    assert game.players[1].name == "AI"

def test_start_game(game):
    # Mock interface methods used in play_game
    game.interface.display_welcome_message = MagicMock()
    game.interface.prompt_num_players.return_value = 1
    game.interface.prompt_player_name.return_value = "Player1"
    game.interface.display_final_results = MagicMock()

    game.play_game()

    # Assert the interface methods were called
    game.interface.display_welcome_message.assert_called_once()
    game.interface.display_final_results.assert_called_once()
