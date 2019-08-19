

class Motion:
    # donne un deplacement en direction x, direction y pour le deplacemnt du hero
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"Motion(x={self.dx}, y={self.dy})"
