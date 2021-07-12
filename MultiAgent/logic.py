import entities

d = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


def interact_with_surroundings(agent, entity_set):
    has_interacted = False
    subset = get_nearby_entities(agent, entity_set)
    for entity in subset:
        if isinstance(entity, entities.InteractiveEntity):
            response = entity.activate(agent.group_id)
            if response is True:
                has_interacted = True
    return has_interacted


def get_nearby_entities(agent, entity_set):
    agent_range = 1
    subset = []
    x, y = agent.x, agent.y
    # since range() is excluding the stop arg, +1 is added to include the stop arg
    for y_position in range(y - agent_range, y + agent_range + 1):
        for x_position in range(x - agent_range, x + agent_range + 1):
            entity = get_entity_by_position(x_position, y_position, entity_set)
            if entity is not None:
                subset.append(entity)
    return subset


def get_entity_by_position(x, y, entity_set):
    for entity in entity_set:
        if entity.x == x and entity.y == y:
            return entity
    return None


def move_agent_in_list(entity_set, agent, direction):
    new_position = agent.check_next_move(direction)
    if not is_occupied(entity_set, new_position):
        agent.move(direction)
        return True
    else:
        return False


def is_occupied(entity_set, position):
    for entity in entity_set:
        if entity.x == position[0] and entity.y == position[1]:
            return True
    return False


def count_activated_entities(entity_set):
    count = 0
    for entity in entity_set:
        if isinstance(entity, entities.InteractiveEntity):
            if entity.activated is True:
                count += 1
    return count


def move_agent(field, agent, direction):
    # array based
    valid_move = is_move_valid(field, agent, direction)
    print("pre-position, x:" + str(agent.x) + ", y:" + str(agent.y) + ", Valid move:" + str(
        valid_move))
    if valid_move:
        i, j = d[direction]
        x, y = agent.x, agent.y
        agent.x = x + i
        agent.y = y + j
        field[x][y] = entities.EmptySpace(x, y)
        field[x + i][y + j] = agent
    print("post-position, x:" + str(agent.x) + ", y:" + str(agent.y))
    return field, agent


def is_move_valid(field, agent, direction):
    i, j = d[direction]
    x, y = agent.x, agent.y
    return field[x + i][y + j].id == 0
