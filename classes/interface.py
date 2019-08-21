import os
import sys
from pygame import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE, QUIT

# from .event import Event
from .motion import down, left, right, up


class Interface:
    def loop(self, windows, pygame, display, hero, guardian):
        background = pygame.image.load("pictures/background.jpg").convert()
        picture = pygame.image.load(hero.picture).convert_alpha()
        state = True
        while state:
            # direction = Event().event_user()
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
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
                windows.blit(picture, (
                    hero.position.x * 30, hero.position.y * 30
                ))
                pygame.display.update()
