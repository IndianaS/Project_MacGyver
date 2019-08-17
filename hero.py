
class Hero:
    
    def __init__(self):
        self.backpack = 0
        self.passage = []
        self.position = None
        self.list_item = []
    
    def move(self, direction):
        new_position = self.position + direction #la nouvelle position correspond a la position + une direction
        if new_position in self.passage: # si la nouvelle position a un passage on change la position par un nouvelle position 
            self.position = new_position #position = nouvelle position 


    def loot_item(self):
        if self.position in self.list_item:
            self.backpack += 1
        

class Motion:
    def __init__(self, dx, dy): # donne un deplacement en direction x, direction y pour le deplacemnt du hero
        self.dx = dx
        self.dy = dy
    
    def __repr__(self):
        return f"Motion(x={self.dx}, y={self.dy})"

up = Motion(0, -1)
down = Motion(0, 1)
left = Motion(-1, 0)
right = Motion(1, 0)

