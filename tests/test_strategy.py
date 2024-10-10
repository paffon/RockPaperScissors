"""
This module contains unit tests for the strategy classes in the Rock-Paper-Scissors game,
 including:
- The abstract `Strategy` base class.
- The `RandomStrategy` class, which selects a weapon randomly.
- The `UserInputStrategy` class, which allows a user to input their weapon choice.
"""

import unittest
from unittest.mock import Mock, patch
from rps.strategy import Strategy, RandomStrategy, UserInputStrategy
from rps.exceptions import FailedWeaponChoiceException, MaxAttemptsExceededError
from rps.rps_logic import RPSLogic

class TestStrategy(unittest.TestCase):
    """
    Test cases for the Strategy abstract base class.
    """

    def test_strategy_instantiation(self):
        # Attempting to instantiate an abstract class should raise TypeError
        with self.assertRaises(TypeError):
            strategy = Strategy(strategy_name="AbstractStrategy")

    def test_strategy_execute_not_implemented(self):
        # Create a subclass without implementing execute
        class IncompleteStrategy(Strategy):
            pass

        with self.assertRaises(TypeError):
            IncompleteStrategy(strategy_name="Incomplete")

class TestRandomStrategy(unittest.TestCase):
    """
    Test cases for the RandomStrategy class.
    """

    def test_random_strategy_initialization(self):
        strategy = RandomStrategy()
        self.assertEqual(strategy.name, "Random")

    @patch('random.choice', return_value='s')
    def test_random_strategy_execute(self, mock_random_choice):
        # Mock RPSLogic
        mock_rps_logic = Mock(spec=RPSLogic)
        mock_rps_logic.options = ['r', 'p', 's']

        strategy = RandomStrategy()
        weapon = strategy.execute(mock_rps_logic)

        # Assertions
        mock_random_choice.assert_called_once_with(['r', 'p', 's'])
        self.assertEqual(weapon, 's')

class TestUserInputStrategy(unittest.TestCase):
    """
    Test cases for the UserInputStrategy class.
    """

    def test_user_input_strategy_initialization(self):
        strategy = UserInputStrategy()
        self.assertEqual(strategy.name, "User Input")

    @patch('rps.strategy.get_user_input_with_verification', return_value='r')
    def test_user_input_strategy_execute(self, mock_get_user_input):
        # Mock RPSLogic
        mock_rps_logic = Mock(spec=RPSLogic)
        mock_rps_logic.options = ['r', 'p', 's']
        mock_rps_logic.short_names_to_full_names = {
            'r': 'Rock',
            'p': 'Paper',
            's': 'Scissors'
        }

        strategy = UserInputStrategy()
        weapon = strategy.execute(mock_rps_logic)

        # Assertions
        # Check that get_user_input_with_verification was called with correct arguments
        expected_message = (
            'Choose from the following options: \n\t'
            'r- Rock\n\tp- Paper\n\ts- Scissors\n'
        )
        mock_get_user_input.assert_called_once_with(
            message=expected_message,
            options=['r', 'p', 's']
        )
        self.assertEqual(weapon, 'r')

    @patch('rps.strategy.get_user_input_with_verification',
           side_effect=MaxAttemptsExceededError("Max attempts exceeded"))
    def test_user_input_strategy_execute_failure(self, mock_get_user_input):
        # Mock RPSLogic
        mock_rps_logic = Mock(spec=RPSLogic)
        mock_rps_logic.options = ['r', 'p', 's']
        mock_rps_logic.short_names_to_full_names = {
            'r': 'Rock',
            'p': 'Paper',
            's': 'Scissors'
        }

        strategy = UserInputStrategy()

        # Expect FailedWeaponChoiceException to be raised
        with self.assertRaises(FailedWeaponChoiceException) as context:
            strategy.execute(mock_rps_logic)

        self.assertIn('Invalid weapon choice by UserInput Strategy', str(context.exception))
        # Check that get_user_input_with_verification was called
        self.assertEqual(mock_get_user_input.call_count, 1)

if __name__ == '__main__':
    unittest.main()
