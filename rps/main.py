"""
This module serves as the main entry point for the Rock-Paper-Scissors game application.

It provides the following functionality:
- Initializes game logic and assets.
- Creates human and computer players.
- Manages the game flow by instantiating the Game class and starting the game.
- Handles any game failures through exception handling.

External dependencies include:
- AssetManager: For retrieving game assets like titles.
- Game: For managing rounds and gameplay.
- HumanPlayer, ComputerPlayer: Representing the human and computer players in the game.
- RPSLogic: For comparing player choices and determining the winner.
- FailedGameException: Handles game-related failures during execution.
"""

from rps.asset_manager import AssetManager
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
    # Initialize Rock-Paper-Scissors logic (comparison rules, weapon names, etc.).
    # May raise Configuration error. No need to catch, as it is assumed to be deployed with proper
    # configuration
    rps_logic = RPSLogic()

    # Displaying the game title from the assets (external text file)
    print(AssetManager().get_asset('game_title.txt'))

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
