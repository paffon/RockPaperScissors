from tests.input_files_verification.verify_input_files import validate_input
import pandas as pd
import json
import os

import numpy as np


class Weapon:
    """
    A class representing a weapon in the game, with rules for how it compares to other weapons.

    Attributes:
        relationship (pd.DataFrame): A DataFrame representing the relationships between weapons,
                                     which is used to determine whether one weapon is stronger
                                      or weaker than another.
        short_name (str): A short identifier for the weapon (e.g., "R" for "Rock").
        full_name (str): The full name of the weapon (e.g., "Rock").
    """

    def __init__(self, relationship: pd.DataFrame, short_name: str = None, full_name: str = None):
        """
        Initialize a Weapon object with a relationship DataFrame and optional short and full names.

        :param relationship: A DataFrame that defines the relationships between weapons (who beats
         whom).
        :param short_name: The short name (identifier) of the weapon.
        :param full_name: The full name of the weapon.
        """
        self.relationship = relationship
        self.short_name: str = short_name  # The short name of the weapon
        self.full_name: str = full_name  # The full name of the weapon

    def __repr__(self) -> str:
        """
        Return a string representation of the weapon, which is the full name.

        :return: The full name of the weapon.
        """
        return self.full_name

    def __eq__(self, other) -> bool:
        """
        Check if two weapons are equal based on their short names.

        :param other: The other weapon to compare with.
        :return: True if the short names of both weapons are equal, False otherwise.
        """
        return self.short_name == other.short_name

    def __lt__(self, other) -> bool:
        """
        Compare if this weapon is weaker than another weapon based on the relationship DataFrame.

        :param other: The other weapon to compare with.
        :return: True if this weapon is weaker, False otherwise.
        """
        return self.relationship.loc[self.short_name, other.short_name] == 2

    def __gt__(self, other) -> bool:
        """
        Compare if this weapon is stronger than another weapon based on the relationship DataFrame.

        :param other: The other weapon to compare with.
        :return: True if this weapon is stronger, False otherwise.
        """
        return self.relationship.loc[self.short_name, other.short_name] == 1


class WeaponsCreator:
    """
    A class responsible for creating Weapon objects and managing weapon-related data.

    Attributes:
        names_tuples (list): A list of tuples containing the short and full names of the weapons.
        relationship (pd.DataFrame): A DataFrame representing the relationships between weapons.
    """

    def __init__(self):
        """
        Initialize the WeaponsCreator, loading the weapon names and their relationships from files.
        """
        data_dir: str = '../data/'

        # Paths to the JSON file with weapon names and the CSV file with weapon relationships
        short_names_path = os.path.join(data_dir, 'short_names.json')
        relationship_path = os.path.join(data_dir, 'relationship.csv')

        # Load weapon names from the JSON file
        with open(short_names_path, 'r') as f:
            self.names_tuples = json.load(f)

        # Load weapon relationships from the CSV file into a DataFrame
        self.relationship = pd.read_csv(relationship_path, index_col=0)

        # Validate the loaded data to ensure correctness
        validate_input(self.names_tuples, self.relationship)

    def create_weapon(self, name: str) -> Weapon:
        """
        Create and return a Weapon object based on a given name (either short or full name).

        :param name: The short or full name of the weapon to create.
        :return: A Weapon object if a match is found; otherwise, None.
        """
        for short_name, full_name in self.names_tuples:
            if name in [short_name, full_name]:
                return Weapon(self.relationship, short_name=short_name, full_name=full_name)

    def random_weapon(self) -> Weapon:
        """
        Select a weapon randomly from the list of available weapons and return it.

        :return: A randomly selected Weapon object.
        """
        random_index: int = np.random.randint(len(self.names_tuples))
        short_name, full_name = self.names_tuples[random_index]
        return Weapon(self.relationship, short_name=short_name, full_name=full_name)
