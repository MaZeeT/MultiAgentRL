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
    d = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    def __init__(self, x, y, group_id=0):
        super().__init__(x, y)
        self.id = 2
        self.group_id = group_id

    def check_next_move(self, direction):
        step = self.d[direction]
        return self.x + step[0], self.y + step[1]

    def move(self, direction):
        step = self.d[direction]
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


class Goal(Entity):
    def __init__(self, x, y, target=0):
        super().__init__(x, y)
        self.activated = False
        self.target = target

    def activate(self, actor):
        if actor == self.target:
            self.activated = True
        return self.activated
