from src.weapons.weapons import Weapon
from src.strategies.strategy import Strategy


class StrategyRandom(Strategy):
    """
    A strategy that randomly selects a weapon for the player.

    This class extends the abstract base class `Strategy` and uses a random selection
    mechanism to pick a weapon from the available options in the game.
    """

    def __init__(self):
        """
        Initialize the StrategyRandom object with the name 'Random'.
        The constructor calls the parent `Strategy` class's initializer, passing the strategy name.
        """
        super().__init__(name='Random')

    def pick_weapon(self) -> Weapon:
        """
        Randomly select and return a weapon for the player.

        This method utilizes the `weapons_creator` to randomly generate a weapon
        from the available options.

        :return: A randomly selected Weapon object.
        """
        return self.weapons_creator.random_weapon()
