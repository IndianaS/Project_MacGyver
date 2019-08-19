import random
from item import Item

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
                        self.list_passage.append(self.finish)
                    if char == "s":
                        self.start = Position(n_char, n_line)
                        self.list_passage.append(self.start)
        
    def add_hero(self, hero):
        self.hero = hero
        self.hero.position = self.start
        self.hero.labyrinth = self
        self.hero.list_item = [self.syringe.position, self.needle.position, self.ether.position]
    
    def add_item(self):
        self.get_random_position()
        self.syringe = Item(self.random_position[0])
        self.needle = Item(self.random_position[1])
        self.ether = Item(self.random_position[2])
    
    def add_guardian(self, guardian):
        self.guardian = guardian
        self.guardian.position = self.finish
         
    
    def get_random_position(self):
        self.random_position = random.sample(self.list_passage, 3)
            


class Position:

    def __init__(self, pos_x, pos_y):
        self.y = pos_y
        self.x = pos_x
    
    def __eq__(self, position):
        return self.x == position.x and self.y == position.y

    def __add__(self, motion):
        return Position(self.x + motion.dx, self.y + motion.dy)

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"


