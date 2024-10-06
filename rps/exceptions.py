class InvalidInputError(Exception):
    """Raised when the user input is invalid."""
    pass

class MaxAttemptsExceededError(Exception):
    """Raised when the user exceeds the maximum number of input attempts."""
    pass
