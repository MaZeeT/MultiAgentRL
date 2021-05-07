import gym


class SnakeEnv(gym.Env):
    def __init__(self):
        print("Env initialized")

    def step(self, action):
        print("Step Success!")

    def reset(self):
        print("resetting")

    def render(self, mode='human'):
        print("rendering")
