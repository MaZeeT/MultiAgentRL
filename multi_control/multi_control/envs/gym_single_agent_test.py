import gym
import numpy as np

from . import case, entities
from multi_control.envs.base_env import BaseEnv
import gym
import numpy as np

from . import case
from . import entities


class GymSingleAgentTest(gym.Env):
    options = {
        0: "up",
        1: "left",
        2: "down",
        3: "right",
        4: "action",
    }

    def __init__(self):
        self.agents, self.entity_set = case.get_case()
        self.agents = self.agents[0]
        width = self.entity_set.x_max - self.entity_set.x_min
        height = self.entity_set.y_max - self.entity_set.y_min
        lowest_id, highest_id = self.entity_set.get_lowest_and_highest_id()
        num_actions = len(self.options)
        self.num_of_agents = 1
        self.last_state_reward = 0
        self.reward_modifier = 10
        self.action_space = gym.spaces.Discrete(num_actions)

        # self.observation_space = gym.spaces.Box(low=lowest_id, high=highest_id, shape=(width + 1, height + 1), dtype=np.uint8)
        self.observation_space = gym.spaces.Box(np.array([0, 0]), np.array([width, height]), dtype=np.uint8)

    def step(self, action):
        if action == "action":
            self.entity_set.interact_with_surroundings(self.agents)
        else:
            move_agent_in_list(self.entity_set, self.agents, action)

        observation = self.entity_set.get_int_array()
        reward = self.calculate_reward()
        done = self.check_if_done()
        info = {}
        return observation, reward, done, info

    def render(self, mode='human'):
        for row in self.entity_set.get_int_array():
            print(row)
        print("\n")

    def calculate_reward(self):
        state_reward = self.entity_set.count_goals(only_activated=True)
        result = state_reward - self.last_state_reward
        self.last_state_reward = self.entity_set.count_goals(only_activated=True)
        return result * self.reward_modifier

    def check_if_done(self):
        return self.entity_set.count_goals(only_activated=True) == self.entity_set.count_goals(only_activated=False)

    def reset(self):
        self.agents, self.entity_set = case.get_basic_cooperation()
        self.last_state_reward = 0
        observation = self.entity_set.get_int_array()
        return observation


def move_agent_in_list(entity_set, agent, direction):
    print(f"direction is: {direction}")
    if direction is None: return False
    new_position = agent.check_next_move(direction)
    if not entity_set.is_occupied(new_position):
        agent.move(direction)
        return True
    else:
        return False
