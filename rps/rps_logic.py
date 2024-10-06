"""
This module defines the RPSLogic class, which encapsulates the logic for determining the outcome of
a Rock-Paper-Scissors-like game.

It provides the following functionality:
- Loading and validating weapon names and their relationships from external JSON and CSV files.
- Storing the relationships between weapons in a DataFrame, which is used to compare weapons.
- Mapping short weapon names (e.g., 'r') to full names (e.g., 'Rock').
- Comparing two weapons to determine the winner.

External dependencies include:
- Pandas for managing weapon relationships in a DataFrame.
- JSON for loading weapon names from an external configuration file.
- ConfigurationError for handling invalid input data.
- validate_config_files_input for ensuring the correctness of the loaded files.
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
        short_names_path = os.path.join('data', 'short_names.json')
        relationship_path = os.path.join('data', 'relationship.csv')

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
