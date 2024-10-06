"""
This module contains unit tests for the RPSLogic class in the Rock-Paper-Scissors game.

The tests cover the following scenarios:
- Initializing the RPSLogic class with valid input files (JSON for weapon names and CSV for
 relationships).
- Handling invalid input data during initialization, ensuring ConfigurationError is raised when
 validation fails.
- Testing the `compare` method, which determines the result of a Rock-Paper-Scissors round.
- Simulating a FileNotFoundError when the necessary configuration files are missing during
 initialization.

Mocks are used to simulate file reading (JSON and CSV) and to validate input, allowing the logic to
 be tested in isolation without relying on actual files.
"""

import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from rps.rps_logic import RPSLogic
from rps.exceptions import ConfigurationError

class TestRPSLogic(unittest.TestCase):
    """
    Test cases for the RPSLogic class.
    """

    @patch('rps.rps_logic.validate_config_files_input')
    @patch('rps.rps_logic.pd.read_csv')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    def test_rps_logic_initialization(self, mock_path_join, mock_open_file, mock_read_csv,
                                      mock_validate_input):
        # Arrange
        # Mock the os.path.join to return the file paths as-is
        def join_mock(*args):
            return '/'.join(args)
        mock_path_join.side_effect = join_mock

        # Mock the contents of the short_names.json file
        mock_short_names_content = '[["r", "Rock"], ["p", "Paper"], ["s", "Scissors"]]'
        mock_open_file.return_value.read.return_value = mock_short_names_content

        # Mock the relationship DataFrame
        mock_relationship_df = pd.DataFrame({
            'r': {'r': 0, 'p': 2, 's': 1},
            'p': {'r': 1, 'p': 0, 's': 2},
            's': {'r': 2, 'p': 1, 's': 0}
        })
        mock_read_csv.return_value = mock_relationship_df

        # Act
        rps_logic = RPSLogic()

        # Assert
        # Check that the names_tuples are loaded correctly
        expected_names_tuples = [['r', 'Rock'], ['p', 'Paper'], ['s', 'Scissors']]
        self.assertEqual(rps_logic.names_tuples, expected_names_tuples)

        # Check that the relationship DataFrame is set correctly
        pd.testing.assert_frame_equal(rps_logic.relationship, mock_relationship_df)

        # Check that the short_names_to_full_names dictionary is correct
        expected_short_names_to_full_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        self.assertEqual(rps_logic.short_names_to_full_names, expected_short_names_to_full_names)

        # Check that the options list is correct
        expected_options = ['r', 'p', 's']
        self.assertEqual(rps_logic.options, expected_options)

        # Ensure that validate_input was called with correct arguments
        mock_validate_input.assert_called_once_with(rps_logic.names_tuples, rps_logic.relationship)

    @patch('rps.rps_logic.validate_config_files_input', side_effect=AssertionError("Invalid data"))
    @patch('rps.rps_logic.pd.read_csv')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    def test_rps_logic_initialization_invalid_input(self, mock_path_join, mock_open_file,
                                                    mock_read_csv, mock_validate_input):
        # Arrange
        # Mock the os.path.join to return the file paths as-is
        def join_mock(*args):
            return '/'.join(args)
        mock_path_join.side_effect = join_mock

        # Mock the contents of the short_names.json file
        mock_short_names_content = '[["r", "Rock"], ["p", "Paper"], ["s", "Scissors"]]'
        mock_open_file.return_value.read.return_value = mock_short_names_content

        # Mock the relationship DataFrame
        mock_relationship_df = pd.DataFrame({
            'r': {'r': 0, 'p': 2, 's': 1},
            'p': {'r': 1, 'p': 0, 's': 2},
            's': {'r': 2, 'p': 1, 's': 0}
        })
        mock_read_csv.return_value = mock_relationship_df

        # Act & Assert
        with self.assertRaises(ConfigurationError) as context:
            rps_logic = RPSLogic()

        self.assertIn("Invalid input data: Invalid data", str(context.exception))
        # Ensure that validate_input was called
        mock_validate_input.assert_called_once()

    @patch('rps.rps_logic.validate_config_files_input')
    @patch('rps.rps_logic.pd.read_csv')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    def test_compare_method(self, mock_path_join, mock_open_file, mock_read_csv,
                            mock_validate_input):
        # Arrange
        # Mock os.path.join
        def join_mock(*args):
            return '/'.join(args)
        mock_path_join.side_effect = join_mock

        # Mock short_names.json
        mock_short_names_content = '[["r", "Rock"], ["p", "Paper"], ["s", "Scissors"]]'
        mock_open_file.return_value.read.return_value = mock_short_names_content

        # Mock relationship DataFrame
        mock_relationship_df = pd.DataFrame({
            'r': {'r': 0, 'p': 2, 's': 1},
            'p': {'r': 1, 'p': 0, 's': 2},
            's': {'r': 2, 'p': 1, 's': 0}
        }).T  # Transpose to match input structure
        mock_read_csv.return_value = mock_relationship_df

        # Initialize RPSLogic
        rps_logic = RPSLogic()

        # Act & Assert
        # Test tie
        result = rps_logic.compare('r', 'r')
        self.assertEqual(result, 0)

        # Test weapon1 wins
        result = rps_logic.compare('r', 's')
        self.assertEqual(result, 1)

        # Test weapon2 wins
        result = rps_logic.compare('r', 'p')
        self.assertEqual(result, 2)

    @patch('rps.rps_logic.validate_config_files_input')
    @patch('rps.rps_logic.pd.read_csv', side_effect=FileNotFoundError("File not found"))
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    def test_rps_logic_initialization_file_not_found(self, mock_path_join, mock_open_file,
                                                     mock_read_csv, mock_validate_input):
        # Arrange
        # Mock os.path.join
        def join_mock(*args):
            return '/'.join(args)
        mock_path_join.side_effect = join_mock

        # Mock short_names.json
        mock_short_names_content = '[["r", "Rock"], ["p", "Paper"], ["s", "Scissors"]]'
        mock_open_file.return_value.read.return_value = mock_short_names_content

        # Act & Assert
        with self.assertRaises(FileNotFoundError) as context:
            rps_logic = RPSLogic()

        self.assertIn("File not found", str(context.exception))

if __name__ == '__main__':
    unittest.main()
