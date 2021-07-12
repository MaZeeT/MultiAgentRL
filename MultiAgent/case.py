import entities


def get_case():
    agent = entities.Agent(2, 1)
    entity_set = [
        entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Wall(0, 3),
        entities.Wall(1, 0),                      entities.Goal(1, 2), entities.Wall(1, 3),
        entities.Wall(2, 0), agent,                                    entities.Wall(2, 3),
        entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
    ]
    return agent, entity_set


class Case:
    def __init__(self):
        self.field = [[0 for i in range(5)] for j in range(5)]


class ArrayCase:
    field = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]


class AgentMovementCase:
    field = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]


def entity_field(field):
    x = len(field[0])
    y = len(field)
    for j in range(0, y):
        for i in range(0, x):
            if field[i][j] == 0:
                field[i][j] = entities.EmptySpace(i, j)
            if field[i][j] == 1:
                field[i][j] = entities.Wall(i, j)
    return field
