from abc import ABC, abstractmethod

from rps.exceptions import MaxAttemptsExceededError, FailedWeaponChoiceException
from rps.rps_logic import RPSLogic
from rps.strategy import Strategy, UserInputStrategy, RandomStrategy
from rps.user_input import get_user_input_with_verification, verify_positive_integer


class Player(ABC):
    """
    Abstract base class representing a player in the Rock-Paper-Scissors game.

    Attributes:
        name (str): The player's name.
        strategy (Strategy): The strategy that dictates how the player will choose a weapon.
        rps_logic (RPSLogic): The game's logic for weapon comparisons and rules.
        score (int): The player's current score, initialized to 0.
    """

    def __init__(self, name: str, strategy: Strategy, rps_logic: RPSLogic):
        """
        Initializes a Player with a name, strategy for choosing weapons, and game logic.

        :param name: The player's name.
        :param strategy: The strategy for selecting weapons (e.g., random, user input).
        :param rps_logic: The game logic used to determine weapon rules and outcomes.
        """
        self.name = name
        self.strategy = strategy
        self.rps_logic = rps_logic  # Game logic is required for strategy execution
        self.score = 0  # Initialize the player's score to 0

    def choose(self, *args, **kwargs) -> str:
        """
        Selects a weapon based on the player's strategy.

        :return: The chosen weapon (e.g., 'rock', 'paper', 'scissors').
        """
        return self.strategy.execute(self.rps_logic)


class HumanPlayer(Player):
    """
    Represents a human player in the Rock-Paper-Scissors game.
    The human player chooses their weapon through user input.
    """

    def __init__(self, rps_logic: RPSLogic):
        """
        Initializes a HumanPlayer with a name of 'Human' and a UserInputStrategy.

        :param rps_logic: The game logic used for weapon comparison and rules.
        """
        # The UserInputStrategy prompts the human player to select a weapon
        super().__init__('Human', UserInputStrategy(), rps_logic)


class ComputerPlayer(Player):
    """
    Represents a computer player in the Rock-Paper-Scissors game.
    The computer player chooses its weapon randomly.
    """

    def __init__(self, rps_logic: RPSLogic):
        """
        Initializes a ComputerPlayer with a name of 'Computer' and a RandomStrategy.

        :param rps_logic: The game logic used for weapon comparison and rules.
        """
        # The RandomStrategy allows the computer to select a weapon randomly
        super().__init__('Computer', RandomStrategy(), rps_logic)
