from rps.asset_manager import AssetManager
from rps.exceptions import FailedWeaponChoiceException, FailedGameException, MaxAttemptsExceededError
from rps.user_input import get_user_input_with_verification, verify_positive_integer


class Game:
    """
    Represents a Rock-Paper-Scissors game between two players. The game can be played for a specified
    number of rounds, and the winner is determined by comparing players' weapon choices in each round.

    Attributes:
        player1: The first player in the game, which must have a 'choose' method for weapon selection and 'name', 'score' attributes.
        player2: The second player in the game, similar to player1 in structure.
        rps_logic: Logic that determines the winner based on weapon choices, including a comparison method and weapon names.
        num_rounds (int): The number of rounds to be played, provided by the user.
    """

    def __init__(self, player1, player2, rps_logic):
        """
        Initializes the Game with two players and the logic for comparing Rock-Paper-Scissors choices.
        Asks the user to input the number of rounds, verified by a method.

        :param player1: First player object.
        :param player2: Second player object.
        :param rps_logic: The logic used to compare the players' weapon choices.
        :raises FailedGameException: If the user fails to provide a valid number of rounds.
        """
        self.player1 = player1
        self.player2 = player2
        self.rps_logic = rps_logic

        try:
            # Asking user for the number of rounds to play, with input verification
            self.num_rounds: int = int(get_user_input_with_verification(
                message='Enter the number of rounds: ',
                verification_method=verify_positive_integer
            ))
        except MaxAttemptsExceededError as e:
            # Raise an error if the user fails to provide valid input after multiple attempts
            raise FailedGameException('Invalid number of rounds.') from e

    def play_game(self):
        """
        Starts and manages the overall game for the specified number of rounds.
        Prints the game title asset and iterates over rounds, calling the method to play each round.
        """
        # Displaying the game title from the assets (external text file)
        print(AssetManager().get_asset('game_title.txt'))

        # Looping through the number of rounds and playing each one
        for round_number in range(1, self.num_rounds + 1):
            print(f'\n---------\nRound {round_number} / {self.num_rounds}\n')
            self.play_one_round()

        # Print final scores after all rounds are completed
        print(f'Final score: {self.get_scores_as_str()}')

    def play_one_round(self):
        """
        Plays a single round of the game where each player selects a weapon.
        The round result is calculated and summarized.

        :raises FailedGameException: If any player makes an invalid weapon choice.
        """
        try:
            # Each player chooses their weapon (the 'choose' method is implemented in player objects)
            weapon1 = self.player1.choose()
            weapon2 = self.player2.choose()
        except FailedWeaponChoiceException as e:
            # Raise an error if either player's weapon choice is invalid
            raise FailedGameException(f'Invalid weapon choice: ({e})') from e

        # Use rps_logic to determine the result: 0 for tie, 1 if player1 wins, -1 if player2 wins
        result: int = self.rps_logic.compare(weapon1, weapon2)

        # Convert the weapon's short name (e.g., 'r', 'p', 's') to a full name ('Rock', 'Paper', 'Scissors')
        weapon1_name: str = self.rps_logic.short_names_to_full_names[weapon1].capitalize()
        weapon2_name: str = self.rps_logic.short_names_to_full_names[weapon2].capitalize()

        # Summarize the round and display results
        self.summarize_round(result, weapon1_name, weapon2_name)

    def summarize_round(self, result: int, weapon1_name: str, weapon2_name: str):
        """
        Summarizes the result of a single round and updates players' scores.

        :param result: The result of the round comparison (0 for tie, 1 if player1 wins, -1 if player2 wins).
        :param weapon1_name: Full name of player1's chosen weapon.
        :param weapon2_name: Full name of player2's chosen weapon.
        """
        # Displaying the chosen weapons for both players
        print(f'{self.player1.name} chose {weapon1_name}, {self.player2.name} chose {weapon2_name}.')

        if result == 0:
            # If the result is a tie, announce it
            print(f'Tie! Both players chose {weapon1_name}.')

        elif result == 1:
            # If player1 wins, increment their score and announce the victory
            self.player1.score += 1
            print(f'{weapon1_name} beats {weapon2_name}. {self.player1.name} wins!')

        else:
            # If player2 wins, increment their score and announce the victory
            self.player2.score += 1
            print(f'{weapon2_name} beats {weapon1_name}. {self.player2.name} wins!')

        # Display the updated scores after the round
        print(self.get_scores_as_str())

    def get_scores_as_str(self) -> str:
        """
        Returns the current scores of both players as a formatted string.

        :return: A string representing the current score in the format "player1_name score1 - score2 player2_name".
        """
        # Formatting and returning the current scores as a string
        return f'{self.player1.name} {self.player1.score} - {self.player2.score} {self.player2.name}'
