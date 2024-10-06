"""
This module contains unit tests for the user input handling functions in the
 Rock-Paper-Scissors game.

The tests cover:
- The `get_user_input_with_verification` function, which prompts the user for input and verifies
 it.
  - Ensures valid inputs are handled correctly.
  - Tests behavior when invalid inputs are followed by valid ones.
  - Ensures the function raises a `MaxAttemptsExceededError` when the user exceeds the allowed
   number of attempts.
  - Verifies input validation when provided with options or a custom verification method (like
   `verify_positive_integer`).

- The `verify_user_input` function, which checks whether the user's input matches valid options or
 passes a custom verification function.
  - Tests input validation with and without options.
  - Ensures proper exception handling for invalid inputs.

- The `verify_positive_integer` function, which verifies whether the input is a valid positive
 integer.
  - Tests various inputs, including valid integers, negative numbers, non-integer strings, and
   special characters.

Mocks are used to simulate user input and validate the function behavior under different scenarios.
"""

import unittest
from unittest.mock import patch
from rps.user_input import (
    get_user_input_with_verification,
    verify_user_input,
    verify_positive_integer
)
from rps.exceptions import InvalidInputError, MaxAttemptsExceededError


class TestGetUserInputWithVerification(unittest.TestCase):
    """Test cases for get_user_input_with_verification function."""

    @patch('builtins.input', return_value='valid_input')
    def test_valid_input_first_attempt(self, mock_input):
        # Test with no options or verification method
        result = get_user_input_with_verification("Enter input:")
        self.assertEqual(result, 'valid_input')
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['invalid', 'valid_input'])
    def test_invalid_then_valid_input(self, mock_input):
        # Mock verify_user_input to raise an error on 'invalid' input
        with patch('rps.user_input.verify_user_input') as mock_verify:
            # Configure the mock to raise InvalidInputError on 'invalid'
            def side_effect(input_value, *args, **kwargs):
                if input_value == 'invalid':
                    raise InvalidInputError("Invalid input.")
                else:
                    return True
            mock_verify.side_effect = side_effect

            result = get_user_input_with_verification("Enter input:")
            self.assertEqual(result, 'valid_input')
            self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', side_effect=['invalid'] * 3)
    def test_exceed_max_attempts(self, mock_input):
        # Mock verify_user_input to always raise InvalidInputError
        with patch('rps.user_input.verify_user_input',
                   side_effect=InvalidInputError("Invalid input.")):
            with self.assertRaises(MaxAttemptsExceededError):
                get_user_input_with_verification("Enter input:", attempts=3)
            self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', return_value='option1')
    def test_with_options_valid_input(self, mock_input):
        options = ['option1', 'option2', 'option3']
        result = get_user_input_with_verification("Choose an option:", options=options)
        self.assertEqual(result, 'option1')

    @patch('builtins.input', side_effect=['invalid', 'option2'])
    def test_with_options_invalid_then_valid(self, mock_input):
        options = ['option1', 'option2', 'option3']
        result = get_user_input_with_verification("Choose an option:", options=options)
        self.assertEqual(result, 'option2')
        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', side_effect=['-1', '0', '5'])
    def test_with_verification_method(self, mock_input):
        # Test with verify_positive_integer method
        result = get_user_input_with_verification(
            "Enter a positive integer:",
            verification_method=verify_positive_integer,
            attempts=3
        )
        self.assertEqual(result, '5')
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['invalid', 'still invalid', 'nope'])
    def test_with_verification_method_max_attempts(self, mock_input):
        with self.assertRaises(MaxAttemptsExceededError):
            get_user_input_with_verification(
                "Enter a positive integer:",
                verification_method=verify_positive_integer,
                attempts=3
            )
        self.assertEqual(mock_input.call_count, 3)


class TestVerifyUserInput(unittest.TestCase):
    """Test cases for verify_user_input function."""

    def test_verify_user_input_with_options_valid(self):
        options = ['option1', 'option2', 'option3']
        result = verify_user_input('option2', options=options)
        self.assertTrue(result)

    def test_verify_user_input_with_options_invalid(self):
        options = ['option1', 'option2', 'option3']
        with self.assertRaises(InvalidInputError) as context:
            verify_user_input('invalid_option', options=options)
        self.assertIn("Invalid option: 'invalid_option'", str(context.exception))

    def test_verify_user_input_with_method_valid(self):
        result = verify_user_input('10', verification_method=verify_positive_integer)
        self.assertTrue(result)

    def test_verify_user_input_with_method_invalid(self):
        with self.assertRaises(InvalidInputError) as context:
            verify_user_input('-5', verification_method=verify_positive_integer)
        self.assertIn("Invalid input: '-5'", str(context.exception))

    def test_verify_user_input_with_no_validation(self):
        # No options or verification method provided; any input is valid
        result = verify_user_input('any_input')
        self.assertTrue(result)


class TestVerifyPositiveInteger(unittest.TestCase):
    """Test cases for verify_positive_integer function."""

    def test_valid_positive_integers(self):
        self.assertTrue(verify_positive_integer('1'))
        self.assertTrue(verify_positive_integer('100'))
        self.assertTrue(verify_positive_integer('99999'))

    def test_zero_and_negative_numbers(self):
        self.assertFalse(verify_positive_integer('0'))
        self.assertFalse(verify_positive_integer('-1'))
        self.assertFalse(verify_positive_integer('-100'))

    def test_non_integer_inputs(self):
        self.assertFalse(verify_positive_integer('abc'))
        self.assertFalse(verify_positive_integer('1.5'))
        self.assertFalse(verify_positive_integer(''))

    def test_whitespace_and_special_characters(self):
        self.assertFalse(verify_positive_integer(' '))
        self.assertFalse(verify_positive_integer('@#$'))


if __name__ == '__main__':
    unittest.main()
