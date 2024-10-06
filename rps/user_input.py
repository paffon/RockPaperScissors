from rps.exceptions import InvalidInputError, MaxAttemptsExceededError


def get_user_input_with_verification(message: str, options: list = None,
                                     verification_method: callable = None,
                                     attempts: int = 3) -> str:
    """
    if both options and verification_method are not provided, any input will be accepted.
    if options are provided, the input must be one of the options.
    if verification_method is provided, the input must pass the verification_method.
    """

    while attempts:
        user_input = input(message)
        try:
            verify_user_input(user_input, options, verification_method)
            return user_input
        except InvalidInputError as e:
            print(e)

        attempts -= 1
        print(f'You have {attempts} attempt{"s" if attempts > 1 else ""}')

    raise MaxAttemptsExceededError("Maximum attempts exceeded.")


def verify_user_input(user_input: str, options: list = None, verification_method: callable = None) -> bool:
    if options and user_input not in options:
        raise InvalidInputError(f"Invalid option: {user_input}, must be one of {options}")

    if verification_method and not verification_method(user_input):
        raise InvalidInputError(f"Invalid input: {user_input}, failed to pass {verification_method.__name__}")

    return True

def verify_positive_integer(user_input: str) -> bool:
    try:
        value = int(user_input)
        return value > 0
    except ValueError:
        return False
