from src.strategies.strategy import Strategy
from src.weapons.weapons import Weapon


class Player:
    """
    Represents a player in the game, with a name, strategy, and score.

    The Player class interacts with different game strategies to pick a weapon
    and keeps track of the player's score during the game.

    :param name: The name of the player.
    :param strategy: The strategy that the player uses to pick a weapon.
    :param initial_score: The starting score of the player. Default is 0.
    """

    def __init__(self, name: str, strategy: Strategy, initial_score: int = 0):
        """
        Initialize a Player object with a given name, strategy, and an optional initial score.

        :param name: The name of the player.
        :param strategy: The strategy instance the player uses to make decisions (e.g., random
         or user input).
        :param initial_score: The initial score for the player. Defaults to 0.
        """
        self.name = name
        self.strategy = strategy
        self.score = initial_score

    def pick_weapon(self) -> Weapon:
        """
        Use the player's strategy to select a weapon for the round.

        :return: The weapon chosen by the player's strategy.
        """
        element: Weapon = self.strategy.pick_weapon()
        return element

    def __repr__(self) -> str:
        """
        Provide a string representation of the player, which is the player's name.

        :return: The player's name as a string.
        """
        return self.name
