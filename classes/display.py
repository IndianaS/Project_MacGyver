from pygame.locals import *

from .guardian import Guardian
from .hero import Hero
from .labyrinth import Labyrinth


class Display:
    '''Description de la classe'''

    def __init__(self, pygame, windows, list_wall, list_item):
        self.windows = windows
        self.pygame = pygame
        self.list_wall = list_wall
        self.list_item = list_item

    def display(self):
        for position in self.list_wall:
            coordinate = (position.x * 30, position.y * 30)
            wall = self.pygame.image.load('pictures/wall.png').convert()
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
    
    def display_backpack(self, hero):
        pass
