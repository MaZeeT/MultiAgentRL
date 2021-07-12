import entities

d = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


def move_agent_in_list(entity_set, agent, direction):
    new_position = agent.check_next_move(direction)
    if not entity_set.is_occupied(new_position):
        agent.move(direction)
        return True
    else:
        return False


def count_activated_entities(entity_set):
    count = 0
    for entity in entity_set.get_raw_set():
        if isinstance(entity, entities.InteractiveEntity):
            if entity.activated is True:
                count += 1
    return count

