import abc


class EntitySet:
    def __init__(self, entity_set):
        self.entity_set = entity_set
        self.x_min, self.y_min, self.x_max, self.y_max = self.get_stats()

    def get_stats(self):
        x_min, y_min, x_max, y_max = 0, 0, 0, 0
        for entity in self.entity_set:
            if entity.x < x_min: x_min = entity.x
            if entity.x > x_max: x_max = entity.x
            if entity.y < y_min: y_min = entity.y
            if entity.y > y_max: y_max = entity.y
        return x_min, y_min, x_max, y_max

    def get_raw_set(self):
        return self.entity_set

    def get_entity_by_position(self, x, y):
        for entity in self.entity_set:
            if entity.x == x and entity.y == y:
                return entity
        return None

class Entity(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = 0  # an id for the specific type of entity

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)


class InteractiveEntity(Entity):
    activated = False

    @abc.abstractmethod
    def activate(self, actor):
        pass


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


class Goal(InteractiveEntity):
    def __init__(self, x, y, interactive_with_group_id=0):
        super().__init__(x, y)
        self.id = 5
        self.group_id = interactive_with_group_id

    def activate(self, actor):
        if actor == self.group_id:
            self.activated = True
        return self.activated
