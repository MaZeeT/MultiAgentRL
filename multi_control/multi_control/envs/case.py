from . import entities


def get_case():
    agents = [entities.Agent(2, 1)]
    entity_set = entities.EntitySet([
        entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Wall(0, 3),
        entities.Wall(1, 0), entities.Goal(1, 2), entities.Wall(1, 3),
        entities.Wall(2, 0), agents[0], entities.Wall(2, 3),
        entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
    ])
    return agents, entity_set


def get_case_two():
    agents = [entities.Agent(2, 1, group_id=1), entities.Agent(4, 1, group_id=2)]
    entity_set = entities.EntitySet([
        entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Wall(0, 3),
        entities.Wall(1, 0), agents[0], entities.Goal(1, 2, interactive_with_group_id=2), entities.Wall(1, 3),
        entities.Wall(2, 0), entities.Wall(2, 3),
        entities.Wall(3, 0), entities.Wall(3, 3),
        entities.Wall(4, 0), agents[1], entities.Goal(4, 2, interactive_with_group_id=1), entities.Wall(4, 3),
        entities.Wall(5, 0), entities.Wall(5, 1), entities.Wall(5, 2), entities.Wall(5, 3),

    ])
    return agents, entity_set


def get_basic_cooperation():
    agents = [entities.Agent(3, 3, group_id=1), entities.Agent(3, 9, group_id=2)]
    goals = [entities.Goal(2, 15, interactive_with_group_id=1), entities.Goal(4, 15, interactive_with_group_id=2)]

    removableWallsPositions = [(1,6), (2,6), (3,6), (4,6), (5,6)]
    rWalls = entities.ParentRemovableWall(removableWallsPositions, interactive_with_group_id=2)

    interactiveWallPositions = [(1,12), (2,12), (3,12), (4,12), (5,12)]
    iWalls = entities.ParentRemovableWall(interactiveWallPositions, interactive_with_group_id=2)

    set = add_outer_walls(x=6, y=18)
    set += agents + goals + rWalls.children + iWalls.children

    entity_set = entities.EntitySet(set)
    return agents, entity_set


def add_outer_walls(x, y):
    wall_set = []
    print(f"x:{x}, y:{y}")
    for xi in range(x):
        wall_set.append(entities.Wall(xi, 0))
        wall_set.append(entities.Wall(xi, y))

    for yi in range(y - 1):
        # start from [1:-1] since the x-loop already coveres the corners
        wall_set.append(entities.Wall(0, yi))
        wall_set.append(entities.Wall(x, yi))

    return wall_set
