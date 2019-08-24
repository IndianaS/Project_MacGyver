from classes.settings import *

from .labyrinth import Position


class Hero:
    def __init__(self):
        self.labyrinth = None
        self.position = None
        self.list_item = []
        self.backpack = 0
        self.picture = HERO_IMG

    def move(self, direction):
        '''Check if the new positon is in pass list to allow the move'''
        new_position = self.position + direction
        if new_position in self.labyrinth.list_passage:
            self.position = new_position
            self.catch_item()
            

    def catch_item(self):
        '''Gives the possibility to pick up the object then the stock in backpack'''
        for item in self.list_item:
            if self.position == item.position and item.looted != 1:
                print(f'Tu a un objet!! {item}')
                item.looted = 1
                x = self.backpack
                item.position = Position(x, 15)
                self.backpack += 1

    def win_condition(self):
        '''Victory condition depending on the content of the backpack and the position'''
        if self.position == self.labyrinth.finish:
            if self.backpack == 3:
                return 1
            else:
                return 0

    def __repr__(self):
        return self.position
