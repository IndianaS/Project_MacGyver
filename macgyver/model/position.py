

class Position:
    def __init__(self, pos_x, pos_y):
        self.y = pos_y
        self.x = pos_x

    def __eq__(self, position):
        '''Determine the equality between positions'''
        return self.x == position.x and self.y == position.y

    def __add__(self, motion):
        '''Add displacement motion to self position'''
        return Position(self.x + motion.dx, self.y + motion.dy)

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"
