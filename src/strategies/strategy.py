from abc import ABC, abstractmethod

from src.weapons.weapons import WeaponsCreator, Weapon

"""
Why we import ABC:

- We use `ABC` (Abstract Base Class) to make sure `Strategy` can't be instantiated directly.
  This ensures that it's only used as a base for other specific strategies like random or user
  input.
- The `abstractmethod` decorator forces any class that inherits from `Strategy` to implement the 
  `pick_weapon` method. This keeps all strategies consistent while allowing each one to have its 
  own way of picking a weapon.
- If someone tries to create a `Strategy` object directly without defining `pick_weapon`, they'll 
  get a `TypeError`, preventing incomplete strategy implementations.
"""


class Strategy(ABC):
    """
    Abstract base class for defining a game strategy.

    A strategy determines how a player selects a weapon during a game.
    Concrete subclasses must implement the `pick_weapon` method, which is responsible
    for deciding which weapon to select.

    :param name: The name of the strategy.
    """

    def __init__(self, name: str):
        """
        Initialize the Strategy object with a name and a WeaponsCreator instance.

        :param name: The name of the strategy (e.g., 'Random', 'UserInput').
        """
        self.name = name
        self.weapons_creator = WeaponsCreator()  # Initialize WeaponsCreator to generate weapons

    @abstractmethod
    def pick_weapon(self) -> Weapon:
        """
        Abstract method to select a weapon for the player.

        This method must be implemented by any subclass of Strategy to define
        how a weapon is selected (e.g., randomly, via user input, etc.).

        :return: A Weapon object selected by the strategy.
        """
        pass
