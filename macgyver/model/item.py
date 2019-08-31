

class Item:
    def __init__(self, name, position, picture):
        '''Responsible for objects recoverable by the player'''
        self.position = position
        self.picture = picture
        self.name = name
        self.looted = None

    def __repr__(self):
        return self.name
