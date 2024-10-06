from typing import Tuple

from rps2.asset_manager import AssetManager
from rps2.exceptions import FailedWeaponChoiceException, FailedGameException, MaxAttemptsExceededError
from rps2.user_input import get_user_input_with_verification, verify_positive_integer


class Game:
    def __init__(self, player1, player2, rps_logic):
        self.player1 = player1
        self.player2 = player2
        self.rps_logic = rps_logic

        try:
            self.num_rounds: int = int(get_user_input_with_verification(
                message='Enter the number of rounds: ',
                verification_method=verify_positive_integer
            ))
        except MaxAttemptsExceededError as e:
            raise FailedGameException('Invalid number of rounds.') from e

    def play_game(self):
        print(AssetManager().get_asset('game_title.txt'))

        for round_number in range(1, self.num_rounds + 1):
            print(f'\n---------\nRound {round_number} / {self.num_rounds}\n')
            self.play_one_round()

        print(f'Final score: {self.get_scores_as_str()}')


    def play_one_round(self):
        try:
            weapon1 = self.player1.choose()
            weapon2 = self.player2.choose()
        except FailedWeaponChoiceException as e:
            raise FailedGameException(f'Invalid weapon choice: ({e})') from e

        result: int = self.rps_logic.compare(weapon1, weapon2)

        weapon1_name: str = self.rps_logic.short_names_to_full_names[weapon1].capitalize()
        weapon2_name: str = self.rps_logic.short_names_to_full_names[weapon2].capitalize()

        self.summarize_round(result, weapon1_name, weapon2_name)

    def summarize_round(self, result, weapon1_name, weapon2_name):

        print(f'{self.player1.name} chose {weapon1_name}, {self.player2.name} chose {weapon2_name}.')

        if result == 0:
            print(f'Tie! Both players chose {weapon1_name}.')

        elif result == 1:
            self.player1.score += 1
            print(f'{weapon1_name} beats {weapon2_name}. {self.player1.name} wins!')

        else:
            self.player2.score += 1
            print(f'{weapon2_name} beats {weapon1_name}. {self.player2.name} wins!')

        print(self.get_scores_as_str())

    def get_scores_as_str(self):
        return f'{self.player1.name} {self.player1.score} - {self.player2.score} {self.player2.name}'