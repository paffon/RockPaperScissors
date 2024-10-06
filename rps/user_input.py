"""
This module provides functions for handling and verifying user input in the Rock-Paper-Scissors
 game.

It includes:
- `get_user_input_with_verification`: Prompts the user for input, verifies the input based on
 provided options or a custom verification method, and enforces a maximum number of attempts.
- `verify_user_input`: Validates the user's input against a list of valid options or a custom
 verification function.
- `verify_positive_integer`: A specific verification method that checks if the input is a positive
 integer.

The module raises the following exceptions:
- `InvalidInputError`: Raised when the user's input does not match the expected options or fails
 verification.
- `MaxAttemptsExceededError`: Raised when the user exceeds the maximum allowed number of attempts
 to provide valid input.

These functions are designed to provide robust user input handling and validation for various
 game-related interactions.
"""

from rps.exceptions import InvalidInputError, MaxAttemptsExceededError


def get_user_input_with_verification(message: str, options: list = None,
                                     verification_method: callable = None,
                                     attempts: int = 3) -> str:
    """
    Prompts the user for input and verifies it based on provided options or a verification method.

    If both `options` and `verification_method` are not provided, any input will be accepted.
    If `options` are provided, the input must match one of the options.
    If a `verification_method` is provided, the input must pass the verification method.

    :param message: The prompt message to show to the user.
    :param options: A list of valid options to verify user input against.
    :param verification_method: A callable that verifies the user input.
    :param attempts: Number of attempts the user has to provide valid input.
    :return: The user's valid input.
    :raises MaxAttemptsExceededError: If the user fails to provide valid input within the allowed
     number of attempts.
    """
    attempts_left_warning: str = ''  # Warning message indicating remaining attempts

    # Loop through the allowed attempts
    while attempts:
        user_input = input(attempts_left_warning + message)  # Display prompt and get user input

        try:
            # Verify user input based on provided options or a custom verification method
            verify_user_input(user_input, options, verification_method)
            return user_input  # Return the valid input if no exception was raised
        except InvalidInputError as error:
            # Print the error message and let the user try again
            print(error)

        # Decrease attempts and update the warning message
        attempts -= 1
        attempts_left_warning = f'{attempts} attempt{"s" if attempts > 1 else ""} left. '

    # If all attempts are exhausted, raise a MaxAttemptsExceededError
    raise MaxAttemptsExceededError("Maximum attempts exceeded.")


def verify_user_input(user_input: str, options: list = None,
                      verification_method: callable = None) -> bool:
    """
    Verifies user input against provided options or a verification method.

    :param user_input: The user's input to verify.
    :param options: A list of valid options to check user input against.
    :param verification_method: A callable that verifies the input (e.g., a function that checks if
     input is an integer).
    :return: True if the input is valid.
    :raises InvalidInputError: If the input is not valid based on the options or verification
     method.
    """
    # Check if input is one of the provided options
    if options and user_input not in options:
        raise InvalidInputError(f"Invalid option: '{user_input}', "
                                f"must be one of {options}")

    # If a verification method is provided, check if the input passes it
    if verification_method and not verification_method(user_input):
        raise InvalidInputError(f"Invalid input: '{user_input}', "
                                f"failed to pass {verification_method.__name__}")

    return True  # Input is valid


def verify_positive_integer(user_input: str) -> bool:
    """
    Verifies that the user input is a positive integer.

    :param user_input: The input to verify.
    :return: True if the input is a positive integer, otherwise False.
    """
    try:
        # Convert input to integer and check if it's greater than 0
        value = int(user_input)
        return value > 0
    except ValueError:
        # If conversion fails, the input is not a valid integer
        return False
