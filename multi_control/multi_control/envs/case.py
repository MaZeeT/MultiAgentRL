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

def get_case_two_single_agent():
    agents = [entities.Agent(2, 1, group_id=1)]
    entity_set = entities.EntitySet([
        entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Wall(0, 3),
        entities.Wall(1, 0), agents[0], entities.Goal(1, 2, interactive_with_group_id=1), entities.Wall(1, 3),
        entities.Wall(2, 0), entities.Wall(2, 3),
        entities.Wall(3, 0), entities.Wall(3, 3),
        entities.Wall(4, 0), agents[1], entities.Goal(4, 2, interactive_with_group_id=1), entities.Wall(4, 3),
        entities.Wall(5, 0), entities.Wall(5, 1), entities.Wall(5, 2), entities.Wall(5, 3),

    ])
    return agents, entity_set

