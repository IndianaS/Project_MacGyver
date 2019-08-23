import pygame
from pygame.locals import *

from classes import *
from classes.settings import *

up = Motion(0, -1)
down = Motion(0, 1)
left = Motion(-1, 0)
right = Motion(1, 0)


def __main__():
    lvl = Labyrinth()
    lvl.read_level(LEVEL_FILE)
    lvl.add_item()
    mcgyver = Hero()
    lvl.add_hero(mcgyver)
    garde = Guardian()
    lvl.add_guardian(garde)

    # Opening the pygame window
    windows = pygame.display.set_mode((windows_width, windows_height))

    # Loading and gluing the background
    background = pygame.image.load(BACKGROUND_IMG).convert()
    windows.blit(background, (0, 0))

    vue = Display(pygame, windows, lvl.list_wall, lvl.list_item, mcgyver)
    vue.display()
    vue.display_guardian(garde)
    vue.display_hero(mcgyver)

    interface = Interface()

    # Window title
    pygame.display.set_caption(window_title)

    # Refresh the screen
    pygame.display.update()

    # Game loop speed limit
    pygame.time.Clock().tick(30)
    interface.loop(windows, pygame, vue, mcgyver, garde)


if __name__ == "__main__":
    __main__()
