"""
This module defines custom exception classes used for handling various error conditions
in a game or configuration system.

The exceptions include:
- ConfigurationError: Raised when there is an issue with the system configuration.
- InvalidInputError: Raised when user input is considered invalid.
- MaxAttemptsExceededError: Raised when a user exceeds the maximum allowed input attempts.
- FailedWeaponChoiceException: Raised when the user fails to make a valid weapon choice.
- FailedGameException: Raised when the game encounters an error and cannot complete successfully.

These exceptions are used to handle specific failure cases and ensure more informative error
 handling throughout the application.
"""


class ConfigurationError(Exception):
    """Raised when the configuration is invalid."""

class InvalidInputError(Exception):
    """Raised when the user input is invalid."""

class MaxAttemptsExceededError(Exception):
    """Raised when the user exceeds the maximum number of input attempts."""

class FailedWeaponChoiceException(Exception):
    """Raised when the user fails to choose a valid weapon."""

class FailedGameException(Exception):
    """Raised when the game fails to complete successfully."""
