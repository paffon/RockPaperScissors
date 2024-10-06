from assets_manager import AssetManager
from exceptions import MaxAttemptsExceededError

class Game:
    def __init__(self, num_rounds, player1, player2, rps_logic):
        self.num_rounds = num_rounds
        self.player1 = player1
        self.player2 = player2
        self.rps_logic = rps_logic

    def reset_game(self):
        self.player1.score = 0
        self.player2.score = 0

    def play(self):
        asset_manager = AssetManager('assets')
        for round_num in range(1, self.num_rounds + 1):
            print(f"\nRound {round_num}")
            try:
                move1 = self.player1.make_move()
                move2 = self.player2.make_move()
            except MaxAttemptsExceededError as e:
                print(e)
                return

            result = self.rps_logic.determine_winner(move1, move2)

            print(f"{self.player1.name} chose {move1}")
            move1_art = asset_manager.get_asset(f"{move1}.txt")
            if move1_art:
                print(move1_art)

            print(f"{self.player2.name} chose {move2}")
            move2_art = asset_manager.get_asset(f"{move2}.txt")
            if move2_art:
                print(move2_art)

            if result == 'win':
                print(f"{self.player1.name} wins this round!")
                self.player1.score += 1
            elif result == 'lose':
                print(f"{self.player2.name} wins this round!")
                self.player2.score += 1
            else:
                print("This round is a tie!")

            print(f"Scores => {self.player1.name}: {self.player1.score}, {self.player2.name}: {self.player2.score}")

        # After all rounds
        print("\nGame Over!")
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins the game!")
        elif self.player1.score < self.player2.score:
            print(f"{self.player2.name} wins the game!")
        else:
            print("The game is a tie!")
