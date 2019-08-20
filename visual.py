import pygame
from pygame.locals import *

from guardian import Guardian
from hero import Hero
from labyrinth import Labyrinth

pygame.init()


class Display:
    def __init__(self, windows):
        self.windows = windows

    def display(self, list_wall, list_item):
        for position in list_wall:
            coordinate = (position.x * 30, position.y * 30)
            wall = picture = pygame.image.load('pictures/wall.png').convert()
            self.windows.blit(wall, coordinate)

        for item in list_item:
            coordinate = (item.position.x * 30, item.position.y * 30)
            picture = pygame.image.load(item.picture).convert_alpha()
            self.windows.blit(picture, coordinate)
