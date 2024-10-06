from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.score = 0

    @abstractmethod
    def make_move(self):
        pass

class Human(Player):
    def make_move(self):
        return self.strategy.make_choice()

class Computer(Player):
    def make_move(self):
        return self.strategy.make_choice()
