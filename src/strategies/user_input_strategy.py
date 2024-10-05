from typing import Tuple, List

from src.weapons.weapons import Weapon
from src.misc.errors import TerminationException
from src.strategies.strategy import Strategy
from src.misc.utils import stringify_list_of_strings


def get_user_choice(options: List[Tuple[str, str]], tries: int = 3) -> str:
    """
    Prompt the user to choose from a list of options, with a limited number of attempts.

    The function displays the available options in a formatted string and validates
    the user's input. If the user selects a valid option, it returns the corresponding value.
    The user has a limited number of tries to provide valid input.

    :param options: A list of tuples where each tuple contains a shorthand option and its
     description.
    :param tries: The maximum number of attempts the user has to provide a valid choice. Default is
     3.
    :return: The description of the chosen option if valid.
    :raises ValueError: If the user fails to provide a valid input within the allowed number of
     attempts.
    """
    # Format options as a string like "(A) Rock or (B) Paper or (C) Scissors"
    options_str = stringify_list_of_strings(
        strings=[f'({tup[0]}) {tup[1]}' for tup in options],
        connector=' or ')

    # Create a dictionary to map shorthand options (e.g., 'A') to their descriptions (e.g., 'Rock')
    options_dict = {tup[0]: tup[1] for tup in options}

    while tries:
        # Prompt the user to choose from the options
        choice: str = input(f"Choose from {options_str}: ")
        if choice in options_dict:
            # Return the description of the chosen option if valid
            return options_dict[choice]

        if tries == 1:
            break

        # Decrement the number of tries and display an error message
        tries -= 1
        print(f"{choice} is invalid. Valid options are {list(options_dict.keys())}. "
              f"You have {tries} {'tries' if tries > 1 else 'try'} left.")

    # Raise a ValueError if all attempts are used up without a valid choice
    raise ValueError(f"Invalid user choice.")


class StrategyUserInput(Strategy):
    """
    A strategy that allows the player to select their weapon via user input.

    This strategy prompts the user to choose a weapon from the available options,
    validates the choice, and then returns the corresponding weapon.
    """

    def __init__(self):
        """
        Initialize the StrategyUserInput object with the name 'User Input'.
        """
        super().__init__(name='User Input')

    def pick_weapon(self) -> Weapon:
        """
        Prompt the user to pick a weapon from the available options.

        The method asks the user to choose a weapon and validates their input.
        If an invalid choice is made multiple times, a TerminationException is raised.

        :return: The Weapon object corresponding to the user's choice.
        :raises TerminationException: If the user fails to provide valid input.
        """
        options: List[Tuple[str, str]] = self.weapons_creator.names_tuples

        try:
            # Get the user's weapon choice with validation
            choice: str = get_user_choice(options=options, tries=3)
        except ValueError as e:
            # Raise a TerminationException if the user fails to choose correctly
            raise TerminationException("Invalid user choice.") from e

        # Create and return the Weapon object based on the user's choice
        return self.weapons_creator.create_weapon(choice)
