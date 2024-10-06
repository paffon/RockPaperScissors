import json
import os
import pandas as pd

from tests.input_files_verification.verify_input_files import validate_input

import numpy as np


class RPSLogic:
    def __init__(self):

        short_names_path = os.path.join('..', 'data', 'short_names.json')
        relationship_path = os.path.join('..', 'data', 'relationship.csv')

        # Load weapon names from the JSON file
        with open(short_names_path, 'r') as f:
            self.names_tuples = json.load(f)

        # Load weapon relationships from the CSV file into a DataFrame
        self.relationship = pd.read_csv(relationship_path, index_col=0)

        # Validate the loaded data to ensure correctness
        validate_input(self.names_tuples, self.relationship)

        # Create a dictionary mapping short names to full names for convenience
        self.short_names_to_full_names = {short: full for short, full in self.names_tuples}
        self.options = [short for short, full in self.names_tuples]

    def compare(self, weapon1: str, weapon2: str) -> int:
        """
        0 tie, 1 first weapon wins, 2 second weapon wins
        :param weapon1:
        :param weapon2:
        :return:
        """
        return self.relationship.loc[weapon1, weapon2]

    def random(self) -> str:
        return np.random.choice(self.options)
