from abc import ABC, abstractmethod

from rps2.exceptions import MaxAttemptsExceededError, FailedWeaponChoiceException
from rps2.rps_logic import RPSLogic
from rps2.strategy import Strategy, UserInputStrategy, RandomStrategy
from rps2.user_input import get_user_input_with_verification, verify_positive_integer


class Player(ABC):
    def __init__(self, name: str, strategy: Strategy, rps_logic: RPSLogic):
        self.name = name
        self.strategy = strategy
        self.rps_logic = rps_logic  # necessary to implement strategies
        self.score = 0

    def choose(self, *args, **kwargs) -> str:
        return self.strategy.execute(self.rps_logic)


class HumanPlayer(Player):
    def __init__(self, rps_logic: RPSLogic):
        super().__init__('Human', UserInputStrategy(), rps_logic)


class ComputerPlayer(Player):
    def __init__(self, rps_logic: RPSLogic):
        super().__init__('Computer', RandomStrategy(), rps_logic)