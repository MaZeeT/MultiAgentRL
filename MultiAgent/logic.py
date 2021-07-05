import entities

d = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


def move_agent(field, agent, direction):
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
