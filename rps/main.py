from rps.exceptions import FailedGameException
from rps.game import Game
from rps.player import HumanPlayer, ComputerPlayer
from rps.rps_logic import RPSLogic


def main():
    """
    Main entry point for the Rock-Paper-Scissors game.
    Initializes the game logic, creates players (human and computer),
    and starts the game. Catches and handles any game failure exceptions.
    """
    # Initialize Rock-Paper-Scissors logic (comparison rules, weapon names, etc.)
    rps_logic = RPSLogic()

    # Create a human player and a computer player, passing the game logic to both
    human = HumanPlayer(rps_logic=rps_logic)
    computer = ComputerPlayer(rps_logic=rps_logic)

    try:
        # Initialize the game with the two players and the game logic
        game = Game(human, computer, rps_logic)

        # Start the game
        game.play_game()

    except FailedGameException as e:
        # Handle any game-related errors, such as invalid inputs or issues during gameplay
        print(f'The game could not complete and will now end: {e}')


if __name__ == '__main__':
    # If this script is executed directly, start the game by calling the main function
    main()
