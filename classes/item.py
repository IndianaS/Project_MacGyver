

class Item:
    def __init__(self, name, position, picture):
        self.position = position
        self.picture = picture
        self.name = name
        self.looted = None

    def __repr__(self):
        return self.name
