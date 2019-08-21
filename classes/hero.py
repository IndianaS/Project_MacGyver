
class Hero:
    def __init__(self):
        self.labyrinth = None
        self.position = None
        self.list_item = []
        self.backpack = 0
        self.picture = 'pictures/MacGyver.png'

    def move(self, direction):
        # la nouvelle position correspond a la position + une direction
        new_position = self.position + direction
        # si la nouvelle position a un passage on change la position par un nouvelle position
        if new_position in self.labyrinth.list_passage:
            self.position = new_position  # position = nouvelle position
            self.catch_item()
            self.display_win()

    def catch_item(self):
        for item in self.list_item:
            if self.position == item.position and item.looted != 1:
                print(f'Tu a un objet!! {item}')
                item.looted = 1
                item.picture = 'pictures/vide.png'
                self.backpack += 1

    def display_win(self):
        if self.position == self.labyrinth.finish:
            if self.backpack == 3:
                print('Win!!!!!')
            else:
                print('Game over!!')

    def __repr__(self):
        return self.position
