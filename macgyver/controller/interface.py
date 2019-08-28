import sys

from pygame import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT

from macgyver.model.motion import down, left, right, up
from macgyver.settings import BACKGROUND_IMG


class Interface:

    '''Class that gives the possibility of moving the hero'''

    def loop(self, windows, pygame, display, hero, guardian):
        background = pygame.image.load(BACKGROUND_IMG).convert()
        state = True
        while state:
            for event in pygame.event.get():
                if event.type == QUIT \
                        or event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        hero.move(right)
                    if event.key == K_LEFT:
                        hero.move(left)
                    if event.key == K_UP:
                        hero.move(up)
                    if event.key == K_DOWN:
                        hero.move(down)

                windows.blit(background, (0, 0))
                display.display()
                display.display_guardian(guardian)
                display.display_hero(hero)
                display.display_result()
                pygame.display.update()
