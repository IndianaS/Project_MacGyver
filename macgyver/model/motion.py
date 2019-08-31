

class Motion:

    def __init__(self, dx, dy):
        '''Object responsible for a direction in x and y'''
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"Motion(x={self.dx}, y={self.dy})"


up = Motion(0, -1)
down = Motion(0, 1)
left = Motion(-1, 0)
right = Motion(1, 0)
