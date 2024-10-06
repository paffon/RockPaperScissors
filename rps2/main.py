from rps2.exceptions import FailedGameException
from rps2.game import Game
from rps2.player import HumanPlayer, ComputerPlayer
from rps2.rps_logic import RPSLogic


def main():
    rps_logic = RPSLogic()
    human = HumanPlayer(rps_logic=rps_logic)
    computer = ComputerPlayer(rps_logic=rps_logic)
    try:
        game = Game(human, computer, rps_logic)
        game.play_game()
    except FailedGameException as e:
        print(f'Sorry, but the game could not complete: "{e}" The game ends now.')


if __name__ == '__main__':
    main()