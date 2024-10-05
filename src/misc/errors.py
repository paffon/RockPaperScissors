class TerminationException(Exception):
    """
    Custom exception raised when the user input is invalid or terminates the process.

    :param message: Explanation of the error.
    """
    def __init__(self, message: str):
        super().__init__(message)
