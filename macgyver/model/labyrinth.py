import random

from macgyver.settings import ETHER_IMG, SYRINGE_IMG, TUBE_IMG

from .item import Item
from .position import Position


class Labyrinth:
    '''Class that uses lists to store the file.txt'''

    def __init__(self):
        self.list_wall = []
        self.list_passage = []
        self.finish = None
        self.start = None

    def read_level(self, level_file):
        '''
        Read text file line by line and
        create Position object for each character
        '''
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
        '''Adds the hero on the labyrinth'''
        self.hero = hero
        self.hero.position = self.start
        self.hero.labyrinth = self
        self.hero.list_item = [
            self.syringe,
            self.tube,
            self.ether
        ]

    def add_item(self):
        '''Adds objects to the labyrinth'''
        self.get_random_position()
        self.syringe = Item('syringe', self.random_position.pop(), SYRINGE_IMG)
        self.tube = Item('tube', self.random_position.pop(), TUBE_IMG)
        self.ether = Item('ether', self.random_position.pop(), ETHER_IMG)
        self.list_item = [self.syringe, self.tube, self.ether]

    def add_guardian(self, guardian):
        '''Adds the guardian on the labyrinth'''
        self.guardian = guardian
        self.guardian.position = self.finish

    def get_random_position(self):
        '''Selects three passages in the pass list'''
        self.random_position = random.sample(self.list_passage[:-2], 3)
