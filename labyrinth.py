import random
from item import Item
from position import Position


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
                    if char == "0":
                        ground = Position(n_char, n_line)
                        self.list_passage.append(ground)
                    if char == "f":
                        self.finish = Position(n_char, n_line)
                    if char == "s":
                        self.start = Position(n_char, n_line)
            self.list_passage.append(self.finish)
            self.list_passage.append(self.start)

    def add_hero(self, hero):
        self.hero = hero
        self.hero.position = self.start
        self.hero.labyrinth = self
        self.hero.list_item = [
            self.syringe.position,
            self.needle.position,
            self.ether.position
        ]

    def add_item(self):
        self.get_random_position()
        self.syringe = Item(self.random_position.pop())#'pop' attribut de liste qui remplace 0, 1, 2 
        self.needle = Item(self.random_position.pop())
        self.ether = Item(self.random_position.pop())

    def add_guardian(self, guardian):
        self.guardian = guardian
        self.guardian.position = self.finish

    def get_random_position(self):
        self.random_position = random.sample(self.list_passage[:-2], 3)
