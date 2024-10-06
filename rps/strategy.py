import random
from abc import ABC, abstractmethod
from typing import List

from rps.exceptions import MaxAttemptsExceededError, FailedWeaponChoiceException
from rps.rps_logic import RPSLogic
from user_input import get_user_input_with_verification


class Strategy(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, *args, **kwargs) -> str:
        pass

class RandomStrategy(Strategy):
    def __init__(self):
        super().__init__('Random')

    def execute(self, rps_logic: RPSLogic) -> str:
        return random.choice(rps_logic.options)

class UserInputStrategy(Strategy):
    def __init__(self):
        super().__init__('User Input')

    def execute(self, rps_logic: RPSLogic) -> str:
        sep: str = '\n\t'
        options_str = sep + sep.join(f'{short_name}- {full_name}' for short_name, full_name in rps_logic.short_names_to_full_names.items())
        try:
            return get_user_input_with_verification(f'Choose from {options_str}: ', options=rps_logic.options)
        except MaxAttemptsExceededError as e:
            raise FailedWeaponChoiceException(f'Invalid weapon choice by UserInput Strategy') from e
