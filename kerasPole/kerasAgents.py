import random


class Random:
    def __init__(self, env):
        self.action_size = env.action_space.n

    def get_action(self, state):
        action = random.choice([0,1])
        return action
