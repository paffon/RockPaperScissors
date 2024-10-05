from dataclasses import dataclass

from tests.input_files_verification.verify_input_files import validate_input
import pandas as pd
import json
from typing import Tuple
import os

class Element:
    def __init__(self, short_name: str, full_name: str) -> None:
        self.short_name: str = short_name  #The short name of the element
        self.full_name: str = full_name # The name of the element

    def __repr__(self):
        return self.full_name

    def __eq__(self, other):
        return self.short_name == other.short_name


@dataclass
class ComparisonResult:
    outcome: int  # The result of the comparison, 1 (tie), 1 (player 1 wins), 2 (player 2 wins)
    stronger: Element  # The stronger object in the comparison
    weaker: Element  # The weaker object in the comparison


class Relationship:
    def __init__(self):
        data_dir: str = '../data/'

        short_names_path = os.path.join(data_dir, 'short_names.json')
        relationship_path =  os.path.join(data_dir, 'relationship.csv')

        with open(short_names_path, 'r') as f:
            self.short_names = json.load(f)

        self.relationship = pd.read_csv(relationship_path, index_col=0)


        validate_input(self.short_names, self.relationship)

        # Since a 1-to-1 relationship is asserted, the dictionaries will have the same length
        self.shorts_to_names = {tup[0]: tup[1] for tup in self.short_names}
        self.names_to_shorts = {tup[1]: tup[0] for tup in self.short_names}

    def get_element(self, name: str) -> Element:
        """
        Create an element object from short or full name.
        :param name: either short name or full name of the element object
        :return: Complete Element object
        """
        if name in self.names_to_shorts:
            return Element(short_name=self.names_to_shorts[name], full_name=name)

        return Element(short_name=name, full_name=self.shorts_to_names[name])

    def compare(self, element_1: Element, element_2: Element) -> ComparisonResult:
        if element_1 == element_2:
            return ComparisonResult(outcome=0, stronger=element_1, weaker=element_2)

        outcome = self.relationship.loc[element_1.short_name, element_2.short_name]
        if outcome == 1:
            return ComparisonResult(outcome=1, stronger=element_1, weaker=element_2)

        return ComparisonResult(outcome=2, stronger=element_2, weaker=element_1)


relationship = Relationship()
r = relationship.get_element('rock')
p = relationship.get_element('p')
s = relationship.get_element('scissors')

pass