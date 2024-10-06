"""
This module contains unit tests for the main module of the Rock-Paper-Scissors game.

The tests cover the following scenarios:
- Successfully running the game, ensuring that the game initializes and runs without errors.
- Handling a failure in the game due to a custom exception (FailedGameException).

Mocks are used to simulate the behavior of the RPSLogic, AssetManager, and Game classes,
allowing for testing without invoking the actual game logic or requiring real game assets.
"""

import unittest
from unittest.mock import patch

from rps.exceptions import FailedGameException
from rps.main import main


class TestMain(unittest.TestCase):

    @patch('rps.main.Game')
    @patch('rps.main.AssetManager')
    @patch('rps.main.RPSLogic')
    def test_main_game_success(self, mock_rps_logic, mock_asset_manager, mock_game):
        # Arrange
        mock_asset_manager.return_value.get_asset.return_value = "Rock-Paper-Scissors Game Title"
        mock_game_instance = mock_game.return_value
        mock_game_instance.play_game.return_value = None

        # Act
        main()

        # Assert
        mock_game_instance.play_game.assert_called_once()

    @patch('rps.main.Game', side_effect=FailedGameException("Test Game Failure"))
    @patch('rps.main.AssetManager')
    @patch('rps.main.RPSLogic')
    def test_main_game_failure(self, mock_rps_logic, mock_asset_manager, mock_game):
        # Arrange
        mock_asset_manager.return_value.get_asset.return_value = "Rock-Paper-Scissors Game Title"

        # Act
        with patch('builtins.print') as mock_print:
            main()

        # Assert
        mock_print.assert_called_with("The game could not complete and will now end: Test Game Failure")
        mock_game.assert_called_once()


if __name__ == "__main__":
    unittest.main()
