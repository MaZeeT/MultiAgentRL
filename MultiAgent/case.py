import entities


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
    print(str(x) + ", " + str(y))
    for j in range(0, y):
        for i in range(0, x):
            if field[i][j] == 0:
                field[i][j] = entities.EmptySpace(i, j)
            if field[i][j] == 1:
                field[i][j] = entities.Wall(i, j)
    return field
