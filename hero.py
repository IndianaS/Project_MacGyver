
class Hero:
    def __init__(self):
        self.backpack = 0
        self.labyrinth = None
        self.position = None
        self.list_item = []

    def move(self, direction):
        # la nouvelle position correspond a la position + une direction
        new_position = self.position + direction
        # si la nouvelle position a un passage on change la position par un nouvelle position
        if new_position in self.labyrinth.list_passage:
            self.position = new_position  # position = nouvelle position
            self.win()

    def loot_item(self):
        if self.position in self.list_item:
            self.backpack += 1

    def win(self):
        if self.position == self.labyrinth.finish:
            if self.backpack == 3:
                print('Win!!!!!')
            else:
                print('Game over!!')
