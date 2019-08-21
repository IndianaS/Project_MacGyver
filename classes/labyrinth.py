import random

from .item import Item
from .position import Position


class Labyrinth:
    def __init__(self):
        self.list_wall = []
        self.list_passage = []
        self.finish = None
        self.start = None

    def read_level(self, level_file):
        with open(level_file, 'r') as level:
            for n_line, line in enumerate(level):
                for n_char, char in enumerate(line):
                    if char == "w":
                        wall = Position(n_char, n_line)
                        self.list_wall.append(wall)
                    elif char == "0":
                        ground = Position(n_char, n_line)
                        self.list_passage.append(ground)
                    elif char == "f":
                        self.finish = Position(n_char, n_line)
                    elif char == "s":
                        self.start = Position(n_char, n_line)
            self.list_passage.append(self.finish)
            self.list_passage.append(self.start)

    def add_hero(self, hero):
        self.hero = hero
        self.hero.position = self.start
        self.hero.labyrinth = self
        self.hero.list_item = [
            self.syringe,
            self.tube,
            self.ether
        ]

    def add_item(self):
        self.get_random_position()
        # 'pop' attribut de liste qui remplace 0, 1, 2
        self.syringe = Item('syringe', self.random_position.pop(), "pictures/syringe.png")
        self.tube = Item('tube', self.random_position.pop(), "pictures/tube.png")
        self.ether = Item('ether', self.random_position.pop(), "pictures/ether.png")
        self.list_item = [self.syringe, self.tube, self.ether]

    def add_guardian(self, guardian):
        self.guardian = guardian
        self.guardian.position = self.finish

    def get_random_position(self):
        self.random_position = random.sample(self.list_passage[:-2], 3)
