"""
This module contains unit tests for the Player classes in the Rock-Paper-Scissors game, including:
- The abstract `Player` class.
- The `HumanPlayer` class.
- The `ComputerPlayer` class.
"""


import unittest
from unittest.mock import Mock, patch
from rps.player import Player, HumanPlayer, ComputerPlayer
from rps.rps_logic import RPSLogic

class TestPlayer(unittest.TestCase):
    """
    Test cases for the Player class.
    """

    def test_player_initialization(self):
        # Mock RPSLogic and Strategy
        mock_rps_logic = Mock(spec=RPSLogic)
        mock_strategy = Mock()

        # Initialize Player with mock objects
        player = Player(name="TestPlayer", strategy=mock_strategy, rps_logic=mock_rps_logic)

        # Assertions
        self.assertEqual(player.name, "TestPlayer")
        self.assertEqual(player.strategy, mock_strategy)
        self.assertEqual(player.rps_logic, mock_rps_logic)
        self.assertEqual(player.score, 0)

    def test_player_choose(self):
        # Mock RPSLogic and Strategy
        mock_rps_logic = Mock(spec=RPSLogic)
        mock_strategy = Mock()
        mock_strategy.execute.return_value = 'rock'

        # Initialize Player with mock objects
        player = Player(name="TestPlayer", strategy=mock_strategy, rps_logic=mock_rps_logic)

        # Call the choose method
        weapon = player.choose()

        # Assertions
        mock_strategy.execute.assert_called_once_with(mock_rps_logic)
        self.assertEqual(weapon, 'rock')


class TestHumanPlayer(unittest.TestCase):
    """
    Test cases for the HumanPlayer class.
    """

    @patch('rps.player.UserInputStrategy')
    def test_human_player_initialization(self, mock_user_input_strategy):
        # Mock RPSLogic
        mock_rps_logic = Mock(spec=RPSLogic)
        # Mock the strategy instance
        mock_strategy_instance = Mock()
        mock_user_input_strategy.return_value = mock_strategy_instance

        # Initialize HumanPlayer
        player = HumanPlayer(rps_logic=mock_rps_logic)

        # Assertions
        self.assertEqual(player.name, "Human")
        self.assertEqual(player.strategy, mock_strategy_instance)
        self.assertEqual(player.rps_logic, mock_rps_logic)
        self.assertEqual(player.score, 0)
        mock_user_input_strategy.assert_called_once()

    @patch('rps.player.UserInputStrategy')
    @patch('rps.player.RPSLogic')
    def test_human_player_choose(self, mock_rps_logic, mock_user_input_strategy):
        # Mock strategy and its execute method
        mock_strategy_instance = Mock()
        mock_strategy_instance.execute.return_value = 'paper'
        mock_user_input_strategy.return_value = mock_strategy_instance

        # Initialize HumanPlayer
        player = HumanPlayer(rps_logic=mock_rps_logic)

        # Call the choose method
        weapon = player.choose()

        # Assertions
        mock_strategy_instance.execute.assert_called_once_with(mock_rps_logic)
        self.assertEqual(weapon, 'paper')


class TestComputerPlayer(unittest.TestCase):
    """
    Test cases for the ComputerPlayer class.
    """

    @patch('rps.player.RandomStrategy')
    def test_computer_player_initialization(self, mock_random_strategy):
        # Mock RPSLogic
        mock_rps_logic = Mock(spec=RPSLogic)
        # Mock the strategy instance
        mock_strategy_instance = Mock()
        mock_random_strategy.return_value = mock_strategy_instance

        # Initialize ComputerPlayer
        player = ComputerPlayer(rps_logic=mock_rps_logic)

        # Assertions
        self.assertEqual(player.name, "Computer")
        self.assertEqual(player.strategy, mock_strategy_instance)
        self.assertEqual(player.rps_logic, mock_rps_logic)
        self.assertEqual(player.score, 0)
        mock_random_strategy.assert_called_once()

    @patch('rps.player.RandomStrategy')
    def test_computer_player_choose(self, mock_random_strategy):
        # Mock RPSLogic
        mock_rps_logic = Mock(spec=RPSLogic)
        # Mock strategy and its execute method
        mock_strategy_instance = Mock()
        mock_strategy_instance.execute.return_value = 'scissors'
        mock_random_strategy.return_value = mock_strategy_instance

        # Initialize ComputerPlayer
        player = ComputerPlayer(rps_logic=mock_rps_logic)

        # Call the choose method
        weapon = player.choose()

        # Assertions
        mock_strategy_instance.execute.assert_called_once_with(mock_rps_logic)
        self.assertEqual(weapon, 'scissors')


if __name__ == '__main__':
    unittest.main()
