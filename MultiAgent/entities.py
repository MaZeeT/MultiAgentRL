class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = 0  # an id for the specific type of entity

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)


class Agent(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 2

    def move(self, direction):
        d = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
        }
        step = d[direction]
        self.x += step[0]
        self.y += step[1]


class EmptySpace(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 0


class Wall(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 1
