"""
This module defines various strategies for selecting a weapon in the Rock-Paper-Scissors game.

Each strategy implements the `execute` method to return a chosen weapon based on the specific
 strategy's logic.
"""

import random
from abc import ABC, abstractmethod

from rps.exceptions import MaxAttemptsExceededError, FailedWeaponChoiceException
from rps.rps_logic import RPSLogic
from rps.user_input import get_user_input_with_verification


class Strategy(ABC):
    """
    Abstract base class representing a strategy for selecting a weapon in the Rock-Paper-Scissors
     game.

    Attributes:
        name (str): The name of the strategy.
    """

    def __init__(self, strategy_name: str):
        """
        Initializes a strategy with a given name.

        :param strategy_name: The name of the strategy.
        """
        self.name = strategy_name

    @abstractmethod
    def execute(self, game_logic: RPSLogic) -> str:
        """
        Abstract method to execute the strategy. Must be implemented by all subclasses.

        :return: The chosen weapon as a string.
        """


class RandomStrategy(Strategy):
    """
    A strategy that selects a weapon randomly.
    """

    def __init__(self):
        """
        Initializes a RandomStrategy with the name 'Random'.
        """
        super().__init__('Random')

    def execute(self, game_logic: RPSLogic) -> str:
        """
        Randomly selects a weapon using the options available in RPSLogic.

        :param game_logic: The game logic containing weapon options.
        :return: The randomly chosen weapon as a string.
        """
        # Use Python's random.choice to select a weapon from available options
        return random.choice(game_logic.options)


class UserInputStrategy(Strategy):
    """
    A strategy that allows the user to choose a weapon via input.
    """

    def __init__(self):
        """
        Initializes a UserInputStrategy with the name 'User Input'.
        """
        super().__init__('User Input')

    def execute(self, game_logic: RPSLogic) -> str:
        """
        Prompts the user to select a weapon from the available options in RPSLogic.

        :param game_logic: The game logic containing weapon options and names.
        :return: The user's chosen weapon as a string.
        :raises FailedWeaponChoiceException: If the user fails to provide a valid input after
         multiple attempts.
        """
        # Formatting the weapon options for user display
        separator: str = '\n\t'
        formatted_options = separator + separator.join(
            f'{short_name}- {full_name}'
            for short_name, full_name in game_logic.short_names_to_full_names.items()
        )

        try:
            # Prompt the user to choose a weapon, with input verification for valid choices
            user_prompt = f'Choose from the following options: {formatted_options}\n'
            return get_user_input_with_verification(
                message=user_prompt, options=game_logic.options)

        except MaxAttemptsExceededError as error:
            # Raise a specific exception if the user exceeds allowed attempts for valid input
            raise FailedWeaponChoiceException(
                'Invalid weapon choice by UserInput Strategy'
            ) from error
