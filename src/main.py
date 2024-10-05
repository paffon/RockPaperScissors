from typing import List

# Import modules and classes used for game logic
from src.weapons.comparison import compare_weapons
from src.weapons.weapons import Weapon
from src.misc.errors import TerminationException
from src.player.player import Player
from src.strategies.random_strategy import StrategyRandom
from src.strategies.user_input_strategy import StrategyUserInput
from src.misc.utils import stringify_list_of_strings


def main():
    """
    Main entry point for the Rock-Paper-Scissors game.
    Initializes the game, handles user input for number of games,
    and manages the overall game flow (playing rounds and displaying results).
    """
    print("Welcome to the Rock-Paper-Scissors game!")

    # Initialize two players: human (with user input strategy) and computer (with random strategy)
    human = Player(name="Human", strategy=StrategyUserInput(), initial_score=0)
    computer = Player(name="Computer", strategy=StrategyRandom(), initial_score=0)

    # Get the number of games to play from the user, with input validation
    try:
        n_games = get_number_of_games()
    except TerminationException as e:
        # Handle invalid input and abort the game
        print(e)
        print('The game will abort due to invalid user input. Goodbye!')
        return

    # Play the specified number of games
    play_n_games(human, computer, n_games)

    # Display final scores after all games are completed
    display_final_scores([human, computer])


def get_number_of_games(attempts: int = 3) -> int:
    """
    Prompt the user for the number of games with input validation.
    The user has a limited number of tries to input a valid number.

    :param attempts: Number of attempts allowed for input. Default is 3.
    :return: The number of games if a valid input is given.
    :raises ValueError: If the user fails to provide valid input within the allowed tries.
    """
    while attempts:
        try:
            n_games = int(input("\nHow many games would you like to play? "))
            if n_games > 0:
                return n_games  # Return valid input
        except ValueError:
            print("Invalid input (must be a positive integer).")

        attempts -= 1

        if attempts >= 1:
            print(f"Remaining attempts: {attempts}")

    # Raise an error if user exhausts all attempts
    raise TerminationException("Too many invalid attempts.")


def play_n_games(p1: Player, p2: Player, n_games: int) -> None:
    """
    Play the specified number of games between two players.

    :param p1: First player
    :param p2: Second player
    :param n_games: Number of rounds to play
    """
    for i in range(n_games):
        print(f'\n------------\n\nRound {i + 1} / {n_games}\n')

        # Each player selects a weapon (may raise TerminationException if too many invalid inputs)
        try:
            weapon_1: Weapon = p1.pick_weapon()
            weapon_2: Weapon = p2.pick_weapon()
        except TerminationException as e:
            # Handle case where too many invalid choices are made
            print(e)
            print('The game will end now.')
            break

        # Announce each player's weapon choice
        print(f'{p1} picked {weapon_1}, {p2} picked {weapon_2}')

        # Compare the two weapons and determine the round's result
        result = compare_weapons(weapon_1, weapon_2)
        handle_round_result(p1, p2, result)

        if i < n_games - 1:
            # Display updated scores between rounds (except after the final round)
            print(stringify_scores([p1, p2]))


def handle_round_result(p1: Player, p2: Player, result) -> None:
    """
    Process and display the result of a round, updating player scores accordingly.

    :param p1: First player
    :param p2: Second player
    :param result: Result object containing the outcome of the round
    """
    if result.outcome == 0:
        print("It's a tie!")
    elif result.outcome == 1:
        print(f"{p1} wins!")
        p1.score += 1
    else:
        print(f"{p2} wins!")
        p2.score += 1


def display_final_scores(players: List[Player]) -> None:
    """
    Display the final scores of all players at the end of the game.

    :param players: List of Players
    """
    print("\n------------\n\nFinal Scores:")
    print(stringify_scores(players))  # Show final scores
    print('Thanks for playing, goodbye!')


def stringify_scores(players: List[Player]) -> str:
    """
    Convert player scores into a formatted string for display.

    :param players: List of players whose scores will be shown
    :return: Formatted string of player names and their scores
    """
    scores_strings_list: List[str] = [f'{player.name}: {player.score}' for player in players]
    return stringify_list_of_strings(scores_strings_list, ', ')


# Entry point of the program
if __name__ == "__main__":
    main()
