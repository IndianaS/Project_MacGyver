from labyrinth import Labyrinth, Position
from hero import Hero, Motion
from item import Item
from guardian import Guardian

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

print(garde.position)

# Position de départ
print('Départ:', mcgyver.position)
mcgyver.position = laby.syringe.position

# Ramasser les objets
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