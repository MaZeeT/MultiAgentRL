import random


class Smart:
    def __init__(self, env):
        self.action_size = env.action_space.n

    def get_action(self, state):
        pole_angle = state[2]
        action = 0 if pole_angle < 0 else 1
        return action


class Random:
    def __init__(self, env):
        self.action_size = env.action_space.n

    def get_action(self, state):
        action = random.choice(range(self.action_size))

        return action
