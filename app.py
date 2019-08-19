from labyrinth import Labyrinth, Position
from motion import Motion
from item import Item
from guardian import Guardian
from hero import Hero

up = Motion(0, -1)
down = Motion(0, 1)
left = Motion(-1, 0)
right = Motion(1, 0)


laby = Labyrinth()
laby.read_level('level.txt')
laby.add_item()

mcgyver = Hero()
laby.add_hero(mcgyver)
garde = Guardian()
laby.add_guardian(garde)

# Position du gardien
print('Position du gardien:', garde.position)

# Déplacement du héro
print('Position de départ du héro:', mcgyver.position)
mcgyver.move(right)
print('Positon du hero après déplacement:', mcgyver.position, '\n')

# Ramasser les objets
mcgyver.position = laby.syringe.position
print('Objet:', mcgyver.position)
mcgyver.loot_item()
print(mcgyver.backpack)

mcgyver.position = laby.ether.position
print('Objet:', mcgyver.position)
mcgyver.loot_item()
print(mcgyver.backpack)

mcgyver.position = laby.needle.position
print('Objet:', mcgyver.position)
mcgyver.loot_item()
print(mcgyver.backpack)

# Condition de victoire
mcgyver.position = laby.finish
mcgyver.win()