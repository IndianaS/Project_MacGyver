import pygame
from pygame.locals import *

from event import Event
from guardian import Guardian
from hero import Hero
from interface import Interface
from item import Item
from labyrinth import Labyrinth, Position
from motion import Motion
from settings import *
from visual import Display

up = Motion(0, -1)
down = Motion(0, 1)
left = Motion(-1, 0)
right = Motion(1, 0)


# laby = Labyrinth()
# laby.read_level('level.txt')
# # laby.read_level('level_simple.txt')
# laby.add_item()

# mcgyver = Hero()
# laby.add_hero(mcgyver)
# garde = Guardian()
# laby.add_guardian(garde)

# # Position du gardien
# print('Position du gardien:', garde.position)

# # Déplacement du héro
# print('Position de départ du héro:', mcgyver.position)
# mcgyver.move(right)
# print('Positon du hero après déplacement:', mcgyver.position, '\n')

# # Ramasser les objets
# mcgyver.position = laby.syringe.position
# print('Objet:', mcgyver.position)
# mcgyver.loot_item()
# print(mcgyver.backpack)

# mcgyver.position = laby.ether.position
# print('Objet:', mcgyver.position)
# mcgyver.loot_item()
# print(mcgyver.backpack)

# mcgyver.position = laby.needle.position
# print('Objet:', mcgyver.position)
# mcgyver.loot_item()
# print(mcgyver.backpack)

# # Condition de victoire
# mcgyver.position = laby.finish
# mcgyver.win()
# print('\n'*4)

# Reset position
# mcgyver.position = laby.start

# # Test the game
# interface = Interface()
# interface.loop(mcgyver)

level_file = 'level.txt'

lvl = Labyrinth()
lvl.read_level(level_file)
lvl.add_item()
mcgyver = Hero()
lvl.add_hero(mcgyver)
garde = Guardian()
lvl.add_guardian(garde)


# Ouverture de la fenêtre Pygame
windows = pygame.display.set_mode((side_windows, side_windows))

# Chargement et collage du fond
background = pygame.image.load("pictures/background.jpg").convert()
wall = pygame.image.load("pictures/wall.png").convert()
tube = pygame.image.load("pictures/tube.png").convert_alpha()
windows.blit(background, (0, 0))

vue = Display(windows)
vue.display(lvl.list_wall, lvl.list_item)

# Window title
pygame.display.set_caption(window_title)

# Rafraîchissement de l'écran
pygame.display.update()

continuer = 1
while continuer:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():  # On parcours la liste de tous les événements recus
        if event.type == QUIT:  # Si un de ces événement est de type QUIT
            continuer = 0
