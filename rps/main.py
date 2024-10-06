from strategies import UserInputStrategy, RandomStrategy
from players import Human, Computer
from rps_logic import RPSLogic
from game import Game
from assets_manager import AssetManager
from exceptions import MaxAttemptsExceededError

def main():
    # Initialize RPSLogic
    rps_logic = RPSLogic('../data/short_names.json', '../data/relationship.csv')

    # Get the weapons and short names
    weapons = rps_logic.weapons
    short_names = rps_logic.short_names

    # Initialize strategies
    user_strategy =
    computer_strategy =

    # Create players
    human = Human("You", UserInputStrategy(weapons, short_names))
    computer = Computer("Computer", RandomStrategy(weapons))

    # Display game title
    asset_manager = AssetManager('../assets')
    game_title = asset_manager.get_asset('game_title.txt')
    if game_title:
        print(game_title)
    else:
        print("Let's play Rock Paper Scissors!")

    # Get number of rounds from user
    attempts_left = 3
    while attempts_left > 0:
        num_rounds_input = input("Enter the number of rounds you want to play: ")
        if num_rounds_input.isdigit() and int(num_rounds_input) > 0:
            num_rounds = int(num_rounds_input)
            break
        else:
            attempts_left -= 1
            print(f"Invalid input. You have {attempts_left} attempts left.")
    else:
        print("Maximum attempts exceeded.")
        return

    # Create and play game
    game = Game(num_rounds, human, computer, rps_logic)
    game.play()

if __name__ == "__main__":
    main()
