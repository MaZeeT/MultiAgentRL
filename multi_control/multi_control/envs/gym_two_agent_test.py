import gym
import numpy as np

from . import entities
from multi_control.envs.base_env import BaseEnv


class GymTwoAgentTest(BaseEnv):
    def __init__(self):
        self.agents, self.entity_set = self.get_field()
        width = self.entity_set.x_max - self.entity_set.x_min
        height = self.entity_set.y_max - self.entity_set.y_min
        lowest_id, highest_id = self.entity_set.get_lowest_and_highest_id()
        num_actions = len(self.options)
        self.num_of_agents = len(self.agents)
        self.last_state_reward = 0
        self.reward_modifier = 10
        self.action_space = gym.spaces.Discrete(num_actions)

        # self.observation_space = gym.spaces.Box(low=lowest_id, high=highest_id, shape=(1, width+1, height+1), dtype=np.uint8)
        self.observation_space = gym.spaces.Box(np.array([0, 0]), np.array([width, height]), dtype=np.uint8)

    def get_field(self):
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
