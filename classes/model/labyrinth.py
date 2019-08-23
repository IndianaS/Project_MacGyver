import random

from classes.settings import ETHER_IMG, SYRINGE_IMG, TUBE_IMG

from .item import Item
from .position import Position


class Labyrinth:
    
    '''Class that uses liste for reading the txt file '''
    
    def __init__(self):
        self.list_wall = []
        self.list_passage = []
        self.finish = None
        self.start = None

    '''Methode that reads the txt file by line, and gives a number to each line and character'''
    
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

    '''Method that adds the hero on the labyrinth'''
    
    def add_hero(self, hero):
        self.hero = hero
        self.hero.position = self.start
        self.hero.labyrinth = self
        self.hero.list_item = [
            self.syringe,
            self.tube,
            self.ether
        ]

    '''Method that adds objects to the labyrinth'''
    
    def add_item(self):
        self.get_random_position()
        self.syringe = Item('syringe', self.random_position.pop(), SYRINGE_IMG)
        self.tube = Item('tube', self.random_position.pop(), TUBE_IMG)
        self.ether = Item('ether', self.random_position.pop(), ETHER_IMG)
        self.list_item = [self.syringe, self.tube, self.ether]

    '''Method that adds the guardian on the labyrinth'''
    
    def add_guardian(self, guardian):
        self.guardian = guardian
        self.guardian.position = self.finish

    '''Method that selects three passages in the pass list'''
    
    def get_random_position(self):
        self.random_position = random.sample(self.list_passage[:-2], 3)
