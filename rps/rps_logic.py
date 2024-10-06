import csv
import json
from enum import Enum

class RPSLogic:
    def __init__(self, short_names_file, relationships_file):
        self.short_names_file = short_names_file
        self.relationships_file = relationships_file
        self.weapons = []
        self.short_names = {}
        self.relationships = {}
        self.weapon_enum = None
        self.load_weapons()
        self.load_relationships()
        self.create_weapon_enum()

    def load_weapons(self):
        with open(self.short_names_file, 'r') as f:
            data = json.load(f)
            self.short_names = {item[0]: item[1] for item in data}
            self.weapons = list(set(self.short_names.values()))

    def load_relationships(self):
        with open(self.relationships_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)[1:]  # Skip index column
            for row in reader:
                weapon = row[0]
                results = row[1:]
                self.relationships[weapon] = dict(zip(header, results))

    def create_weapon_enum(self):
        self.weapon_enum = Enum('Weapon', {name: name for name in self.weapons})

    def determine_winner(self, weapon1_name, weapon2_name):
        if weapon1_name not in self.relationships or weapon2_name not in self.relationships[weapon1_name]:
            raise ValueError("Invalid weapons for determining winner.")
        result = self.relationships[weapon1_name][weapon2_name]
        if result == '0':
            return 'tie'
        elif result == '1':
            return 'win'
        elif result == '2':
            return 'lose'
        else:
            raise ValueError("Invalid result in relationships")

    def get_weapon_enum(self):
        return self.weapon_enum
