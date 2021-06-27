d = {
    "up": (1, 0),
    "down": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = 0  # an id for the specific type of entity

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)


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
    door_parts = []

    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.direction = direction
        self.id = 5
        self.color = "red-blue"

    def generate_parts(self, x, y, direction):
        pass

    def open_door(self):
        for part in self.door_parts:
            pass

    def close_door(self):
        for part in self.door_parts:
            pass

    class DoorPart(Entity):
        def __init__(self, x, y):
            super().__init__(x, y)


class Agent(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = 2
        self.color = "green"

    def move(self, direction):
        x, y = d[direction]
        self.x += x
        self.y += y
