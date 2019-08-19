import os
from motion import up, down, right, left
from event import Event

class Interface:
    def loop(self, hero):
        state = True
        while state:
            direction = Event().event_user()
            if direction == 'q':
                state = False
            if direction == 'd':
                os.system('cls')
                hero.move(right)
                print(hero.position)
            if direction == 'g':
                os.system('cls')
                hero.move(left)
                print(hero.position)
            if direction == 'h':
                os.system('cls')
                hero.move(up)
                print(hero.position)
            if direction == 'b':
                os.system('cls')
                hero.move(down)
                print(hero.position)
