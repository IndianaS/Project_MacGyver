from pygame.locals import *

from classes.model.guardian import Guardian
from classes.model.hero import Hero
from classes.model.labyrinth import Labyrinth
from classes.settings import *

class Display:
    '''Description de la classe'''

    def __init__(self, pygame, windows, list_wall, list_item, hero):
        self.windows = windows
        self.pygame = pygame
        self.list_wall = list_wall
        self.list_item = list_item
        self.win = self.pygame.image.load(WIN_IMG).convert_alpha()
        self.lose = self.pygame.image.load(LOSE_IMG).convert_alpha()
        self.hero = hero

    def display(self):
        for position in self.list_wall:
            coordinate = (position.x * 30, position.y * 30)
            wall = self.pygame.image.load(WALL_IMG).convert()
            self.windows.blit(wall, coordinate)

        for item in self.list_item:
            coordinate = (item.position.x * 30, item.position.y * 30)
            picture = self.pygame.image.load(item.picture).convert_alpha()
            self.windows.blit(picture, coordinate)

    def display_guardian(self, guardian):
        coordinate = (guardian.position.x * 30, guardian.position.y * 30)
        picture = self.pygame.image.load(guardian.picture).convert_alpha()
        self.windows.blit(picture, coordinate)

    def display_hero(self, hero):
        coordinate = (hero.position.x * 30, hero.position.y * 30)
        picture = self.pygame.image.load(hero.picture).convert_alpha()
        self.windows.blit(picture, coordinate)

    def display_result(self):
        if self.hero.win_condition() == 1:
            self.windows.blit(self.win, (0, 0))
        elif self.hero.win_condition() == 0:
            self.windows.blit(self.lose, (0, 0))
