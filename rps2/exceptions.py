class InvalidInputError(Exception):
    """Raised when the user input is invalid."""
    pass

class MaxAttemptsExceededError(Exception):
    """Raised when the user exceeds the maximum number of input attempts."""
    pass

class FailedWeaponChoiceException(Exception):
    """Raised when the user fails to choose a valid weapon."""
    pass

class FailedGameException(Exception):
    """Raised when the game fails to complete successfully."""
    pass