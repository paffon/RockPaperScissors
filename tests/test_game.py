"""
This module contains unit tests for the Game class in the Rock-Paper-Scissors game.

The tests cover the following scenarios:
- Initializing the game with a valid number of rounds.
- Handling invalid input during game initialization.
- Simulating a single round where player1 wins, player2 wins, or there is a tie.
- Handling an invalid weapon choice during a round.

Mocks are used to simulate player choices and user input without requiring actual gameplay
 interaction.
"""

import unittest
from unittest.mock import Mock, patch
from rps.game import Game
from rps.exceptions import FailedWeaponChoiceException, FailedGameException, MaxAttemptsExceededError


class TestGame(unittest.TestCase):

    @patch('rps.game.get_user_input_with_verification', return_value='3')
    def test_game_initialization_valid_rounds(self, mock_user_input):
        # Arrange: Mock players and rps_logic
        player1 = Mock()
        player2 = Mock()
        rps_logic = Mock()

        # Act: Initialize the game
        game = Game(player1, player2, rps_logic)

        # Assert: Ensure the num_rounds is set and user input is verified
        mock_user_input.assert_called_once()
        self.assertEqual(game.num_rounds, 3)

    @patch('rps.game.get_user_input_with_verification', side_effect=MaxAttemptsExceededError)
    def test_game_initialization_invalid_rounds(self, mock_user_input):
        # Arrange: Mock players and rps_logic
        player1 = Mock()
        player2 = Mock()
        rps_logic = Mock()

        # Act & Assert: Ensure exception is raised for invalid rounds
        with self.assertRaises(FailedGameException):
            Game(player1, player2, rps_logic)

    @patch('rps.game.get_user_input_with_verification', return_value=1)
    def test_play_one_round_player1_wins(self, mock_user_input):
        # Arrange: Mock players, rps_logic, and game object
        player1 = Mock()
        player1.choose.return_value = 'r'  # Player1 chooses Rock
        player1.name = 'Player1'
        player1.score = 0

        player2 = Mock()
        player2.choose.return_value = 's'  # Player2 chooses Scissors
        player2.name = 'Player2'
        player2.score = 0

        rps_logic = Mock()
        rps_logic.compare.return_value = 1  # Player1 wins
        rps_logic.short_names_to_full_names = {'r': 'rock', 's': 'scissors'}

        game = Game(player1, player2, rps_logic)

        # Act: Play one round
        game.play_one_round()

        # Assert: Check that player1's score is incremented
        self.assertEqual(player1.score, 1)
        self.assertEqual(player2.score, 0)
        player1.choose.assert_called_once()
        player2.choose.assert_called_once()

    @patch('rps.game.get_user_input_with_verification', return_value=1)
    def test_play_one_round_player2_wins(self, mock_user_input):
        # Arrange: Mock players, rps_logic, and game object
        player1 = Mock()
        player1.choose.return_value = 'r'  # Player1 chooses Rock
        player1.name = 'Player1'
        player1.score = 0

        player2 = Mock()
        player2.choose.return_value = 'p'  # Player2 chooses Paper
        player2.name = 'Player2'
        player2.score = 0

        rps_logic = Mock()
        rps_logic.compare.return_value = -1  # Player2 wins
        rps_logic.short_names_to_full_names = {'r': 'rock', 'p': 'paper'}

        game = Game(player1, player2, rps_logic)

        # Act: Play one round
        game.play_one_round()

        # Assert: Check that player2's score is incremented
        self.assertEqual(player1.score, 0)
        self.assertEqual(player2.score, 1)
        player1.choose.assert_called_once()
        player2.choose.assert_called_once()

    @patch('rps.game.get_user_input_with_verification', return_value=1)
    def test_play_one_round_tie(self, mock_user_input):
        # Arrange: Mock players, rps_logic, and game object
        player1 = Mock()
        player1.choose.return_value = 'r'  # Player1 chooses Rock
        player1.name = 'Player1'
        player1.score = 0

        player2 = Mock()
        player2.choose.return_value = 'r'  # Player2 also chooses Rock
        player2.name = 'Player2'
        player2.score = 0

        rps_logic = Mock()
        rps_logic.compare.return_value = 0  # Tie
        rps_logic.short_names_to_full_names = {'r': 'rock'}

        game = Game(player1, player2, rps_logic)

        # Act: Play one round
        game.play_one_round()

        # Assert: Ensure scores do not change for a tie
        self.assertEqual(player1.score, 0)
        self.assertEqual(player2.score, 0)
        player1.choose.assert_called_once()
        player2.choose.assert_called_once()

    @patch('rps.game.get_user_input_with_verification', return_value=1)
    def test_play_one_round_invalid_weapon_choice(self, mock_user_input):
        # Arrange: Mock players and rps_logic
        player1 = Mock()
        player1.choose.side_effect = FailedWeaponChoiceException("Invalid choice")  # Invalid choice for player1

        player2 = Mock()
        rps_logic = Mock()

        game = Game(player1, player2, rps_logic)

        # Act & Assert: Ensure FailedGameException is raised when an invalid weapon is chosen
        with self.assertRaises(FailedGameException):
            game.play_one_round()


if __name__ == "__main__":
    unittest.main()
