import random
from abc import ABC, abstractmethod
from exceptions import MaxAttemptsExceededError

class Strategy(ABC):
    @abstractmethod
    def make_choice(self):
        pass

class UserInputStrategy(Strategy):
    def __init__(self, weapons, short_names):
        self.weapons = weapons  # List of weapon names
        self.short_names = short_names  # Dict mapping short names to full names

    def make_choice(self):
        attempts_left = 3
        while attempts_left > 0:
            user_input = input(f"Choose your weapon ({'/'.join(self.short_names.keys())}): ").lower()
            if user_input in self.short_names:
                weapon_name = self.short_names[user_input]
                return weapon_name
            else:
                attempts_left -= 1
                print(f"Invalid input. You have {attempts_left} attempts left.")
        raise MaxAttemptsExceededError("Maximum attempts exceeded.")

class RandomStrategy(Strategy):
    def __init__(self, weapons):
        self.weapons = weapons

    def make_choice(self):
        return random.choice(self.weapons)
