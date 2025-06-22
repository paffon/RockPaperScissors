"""
This module defines the RPSLogic class, which encapsulates the logic for determining the outcome of
a Rock-Paper-Scissors-like game.
"""

import json
import os
import pandas as pd

from rps.exceptions import ConfigurationError
from rps.verify_input_files import (
    validate_config_files_input)


class RPSLogic:
    """
    Represents the logic for a Rock-Paper-Scissors-like game, including the loading
    of weapon names and their relationships (which weapons beat others).

    Attributes:
        names_tuples (list): A list of tuples with short names and full names of weapons.
        relationship (pd.DataFrame): A DataFrame representing the relationships between weapons
         (who wins against whom).
        short_names_to_full_names (dict): A dictionary mapping short weapon names to full names.
        options (list): A list of all available weapon short names.
    """

    def __init__(self):
        """
        Initializes RPSLogic by loading weapon names and relationships from external files.
        """
        # Paths to the input files for weapon names and their relationships
        # Resolve paths relative to this file so the module works regardless of
        # the current working directory
        base_dir = os.path.dirname(__file__)
        short_names_path = os.path.join(base_dir, '..', 'data', 'short_names.json')
        relationship_path = os.path.join(base_dir, '..', 'data', 'relationship.csv')

        # Load weapon names from the JSON file
        with open(short_names_path, 'r', encoding='utf-8') as f:
            self.names_tuples = json.load(f)

        # Load weapon relationships from the CSV file into a DataFrame
        self.relationship = pd.read_csv(relationship_path, index_col=0)

        # Validate the loaded data to ensure correctness
        try:
            validate_config_files_input(self.names_tuples, self.relationship)
        except AssertionError as e:
            raise ConfigurationError(f"Invalid input data: {e}") from e

        # Create a dictionary mapping short names (e.g., 'r') to full names (e.g., 'Rock')
        self.short_names_to_full_names = {short: full for short, full in self.names_tuples}

        # List of all weapon short names for easy reference
        self.options = [short for short, full in self.names_tuples]

    def compare(self, weapon1: str, weapon2: str) -> int:
        """
        Compares two weapons and determines the outcome.

        :param weapon1: The first weapon (short name).
        :param weapon2: The second weapon (short name).
        :return: 0 if it's a tie, 1 if the first weapon wins, and 2 if the second weapon wins.
        """
        # Lookup in the relationship DataFrame to determine the result
        return self.relationship.loc[weapon1, weapon2]
