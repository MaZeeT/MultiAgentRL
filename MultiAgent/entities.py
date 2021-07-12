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

    def update_stats(self):
        self.x_min, self.y_min, self.x_max, self.y_max = self.get_stats()

    def get_raw_set(self):
        return self.entity_set

    def get_entity_by_position(self, x, y):
        for entity in self.entity_set:
            if entity.x == x and entity.y == y:
                return entity
        return None

    def get_nearby_entities(self, agent, agent_range=1):
        subset = []
        x, y = agent.x, agent.y
        # since range() is excluding the stop arg, +1 is added to include the stop arg
        for y_position in range(y - agent_range, y + agent_range + 1):
            for x_position in range(x - agent_range, x + agent_range + 1):
                entity = self.get_entity_by_position(x_position, y_position)
                if entity is not None:
                    subset.append(entity)
        return subset

    def append(self, entity):
        self.entity_set.append(entity)
        self.update_stats()

    def is_occupied(self, position):
        for entity in self.entity_set:
            if entity.x == position[0] and entity.y == position[1]:
                return True
        return False

    def count_goals(self, only_activated=True):
        count = 0
        for entity in self.entity_set:
            if isinstance(entity, Goal):
                if only_activated:
                    if entity.activated:
                        count += 1
                else:
                    count += 1
        return count

    def interact_with_surroundings(self, agent):
        has_interacted = False
        subset = self.get_nearby_entities(agent)
        for entity in subset:
            if isinstance(entity, InteractiveEntity):
                response = entity.activate(agent.group_id)
                if response is True:
                    has_interacted = True
        return has_interacted

    def get_empty_array(self):
        #todo this should be refactored and tested
        field = [[EmptySpace(i, j) for i in range(self.x_max + 1)] for j in range(self.y_max + 1)]
        return field

    def get_array(self):
        # todo this should be refactored and tested
        field = self.get_empty_array()
        for entity in self.entity_set:
            x, y = entity.x, entity.y
            field[x][y] = entity
        return field


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
