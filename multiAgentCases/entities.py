class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MovablePosition(Position):
    d = {
        "up": (1, 1),
        "down": (0, 0),
        "left": (0, 0),
        "right": (0, 0),
    }

    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, direction):
        x, y = self.d[direction]
        self.x += x
        self.y += y


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = 0  # an id for the specific type of entity

class Gate(Entity):
    def __init__(self, x, y, agent):
        super().__init__(x, y)
        self.id = 3
        self.agent_id = agent.id

class Goal(Entity):
    def __init__(self, x, y, agent):
        super().__init__(x, y)
        self.id = 4
        self.agent_id = agent.id

class Wall(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 1
        self.color = "black"


class Door(Entity):
    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.direction = direction
        self.id = 5
        self.color = "red-blue"


class Agent(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 2
        self.color = "green"
