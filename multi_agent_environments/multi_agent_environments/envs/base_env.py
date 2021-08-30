# the purpose of this module is to implement all common functions and data the different environment designs need.
import gym
import numpy as np

from . import entities


class BaseEnv(gym.Env):
    options = {
        0: "up",
        1: "left",
        2: "down",
        3: "right",
        4: "action",
    }

    def __init__(self):
        self.agents, self.entity_set = self.get_field()
        width = self.entity_set.x_max - self.entity_set.x_min
        height = self.entity_set.y_max - self.entity_set.y_min
        lowest_id, highest_id = self.entity_set.get_lowest_and_highest_id()
        num_actions = len(self.options)
        self.num_of_agents = len(self.agents)
        self.action_space = gym.spaces.Discrete(num_actions)

        # self.observation_space = gym.spaces.Box(low=lowest_id, high=highest_id, shape=(width + 1, height + 1), dtype=np.uint8)
        self.observation_space = gym.spaces.Box(np.array([0, 0]), np.array([width, height]), dtype=np.uint8)

        self.last_state_reward = 0
        self.reward_modifier = 10

    def step(self, actions):
        for i in range(self.num_of_agents):
            action = self.options[actions[i]]
            if action == "action":
                self.entity_set.interact_with_surroundings(self.agents[i])
            else:
                self.move_agent(self.agents[i], action)
        self.entity_set.step()

        observation = self.entity_set.get_int_array()
        reward = self.calculate_reward()
        done = self.check_if_done()
        info = {}
        return observation, reward, done, info

    def render(self, mode='human'):
        for row in self.entity_set.get_int_array():
            print(row)
        print("\n")

    def reset(self):
        self.agents, self.entity_set = self.get_field()
        self.last_state_reward = 0
        observation = self.entity_set.get_int_array()
        return observation

    def calculate_reward(self):
        state_reward = self.entity_set.count_goals(only_activated=True)
        result = state_reward - self.last_state_reward
        self.last_state_reward = self.entity_set.count_goals(only_activated=True)
        return result * self.reward_modifier

    def check_if_done(self):
        return self.entity_set.count_goals(only_activated=True) == self.entity_set.count_goals(only_activated=False)

    # helper function to add walls to the field
    def add_outer_walls(self, x, y):
        wall_set = []
        wall_set.append(entities.Wall(x, y))  # add last corner since range(x) exclude the last number in the range.

        for xi in range(x):
            wall_set.append(entities.Wall(xi, 0))
            wall_set.append(entities.Wall(xi, y))

        for yi in range(y):
            # start from [1:-1] since the x-loop already coveres the corners
            wall_set.append(entities.Wall(0, yi))
            wall_set.append(entities.Wall(x, yi))

        return wall_set

    def move_agent(self, agent, direction):
        if direction is None: return False
        new_position = agent.check_next_move(direction)
        if not self.entity_set.is_occupied(new_position):
            agent.move(direction)
            return True
        else:
            return False
