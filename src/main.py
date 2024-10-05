import random
from typing import Tuple

print("Let's play Rock-Paper-Scissors")

def get_stronger_weaker(object_1: str, object_2: str) -> Tuple[str, str]:
    return {
        'r': {'p': ('paper', 'rock'), 's': ('rock', 'scissors')},
        'p': {'r': ('rock', 'paper'), 's': ('scissors', 'paper')},
        's': {'r': ('rock', 'scissors'), 'p': ('paper', 'scissors')}
    }[object_1][object_2]

score_1, score_2 = 0, 0

while True:
    # User
    choice_1: str = input("Enter a choice ([r]ock, [p]aper, [s]cissors): ")

    # Computer
    choice_2: str = random.choice(["r", "p", "s"])

    print(f"You chose {choice_1}, computer chose {choice_2}")

    # Dictionary from choice_1 -> choice_2 -> outcome
    # 0 = tie, 1 = player_1 wins, 2 = player_2 wins

    states = {
        'r': {'r': 0, 'p': 2, 's': 1},
        'p': {'r': 1, 'p': 0, 's': 2},
        's': {'r': 2, 'p': 1, 's': 0}
    }

    outcome: int = states[choice_1][choice_2]

    if outcome == 0:
        print("It's a tie!")
        continue

    stronger_object, weaker_object = get_stronger_weaker(choice_1, choice_2)
    print(f'{stronger_object} beats {weaker_object}')

    if outcome == 1:
        score_1 += 1
        winner = "Player"
    else:
        score_2 += 1
        winner = "Computer"

    print(f"{winner} wins!")
    print(f"Score: (Player) {score_1} - {score_2} (Computer)")
