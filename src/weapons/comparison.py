from dataclasses import dataclass

from src.weapons.weapons import Weapon


@dataclass
class ComparisonData:
    """
    Data class to hold the result of a weapon comparison.

    Attributes:
        outcome (int): The result of the comparison.
                       0 for a tie,
                       1 for Player 1 (weapon_1) wins,
                       2 for Player 2 (weapon_2) wins.
        stronger (Weapon): The weapon that is stronger in the comparison.
        weaker (Weapon): The weapon that is weaker in the comparison.
    """
    outcome: int  # The result of the comparison: 0 (tie), 1 (weapon_1 wins), 2 (weapon_2 wins)
    stronger: Weapon  # The stronger weapon in the comparison
    weaker: Weapon  # The weaker weapon in the comparison


def compare_weapons(weapon_1: Weapon, weapon_2: Weapon) -> ComparisonData:
    """
    Compare two weapons and determine the outcome.

    This function compares two weapons and returns a `ComparisonResult` object
    that contains the outcome of the comparison and identifies the stronger and weaker weapons.

    :param weapon_1: The first weapon (usually Player 1's weapon).
    :param weapon_2: The second weapon (usually Player 2's weapon).
    :return: A `ComparisonResult` object that includes the outcome, stronger, and weaker weapons.
    """
    # If both weapons are the same, it's a tie
    if weapon_1 == weapon_2:
        return ComparisonData(outcome=0, stronger=weapon_1, weaker=weapon_2)

    # If weapon_1 is stronger than weapon_2, Player 1 wins
    elif weapon_1 > weapon_2:
        return ComparisonData(outcome=1, stronger=weapon_1, weaker=weapon_2)

    # Otherwise, Player 2 wins
    return ComparisonData(outcome=2, stronger=weapon_2, weaker=weapon_1)
