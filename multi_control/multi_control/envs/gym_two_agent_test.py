import gym
import numpy as np

from . import case, entities
from multi_control.envs.base_env import BaseEnv


class GymTwoAgentTest(BaseEnv):
    def __init__(self):
        self.agents, self.entity_set = case.get_case_two()
        width = self.entity_set.x_max - self.entity_set.x_min
        height = self.entity_set.y_max - self.entity_set.y_min
        lowest_id, highest_id = self.entity_set.get_lowest_and_highest_id()
        num_actions = len(self.options)
        self.num_of_agents = len(self.agents)
        self.last_state_reward = 0
        self.reward_modifier = 10
        self.action_space = gym.spaces.Discrete(num_actions)

        # action_space: Float and Box are used to simulate an continuous action space
        # at index 0 the movement of the x-axis
        # at index 1 the movement of the y-axis
        # at index 2 the activation of an action
        # self.action_space = gym.spaces.Box(low=np.array([-1.0, -1.0, 0.0]), high=np.array([1.0, 1.0, 1.0]), dtype=np.float16)
        self.observation_space = gym.spaces.Box(
            low=lowest_id, high=highest_id, shape=(width + 1, height + 1), dtype=np.uint8)

    def reset(self):
        self.agents, self.entity_set = case.get_case_two()
        self.last_state_reward = 0
        observation = self.entity_set.get_int_array()
        return observation
