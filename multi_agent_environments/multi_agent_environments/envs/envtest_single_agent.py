import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class SingleAgentTest(BaseEnv):
    def __init__(self):
        self.agents, self.entity_set = self.get_field()
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

    def get_field(self):
        agents = [entities.Agent(2, 1)]
        entity_set = entities.EntitySet([
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Wall(0, 3),
            entities.Wall(1, 0), entities.Goal(1, 2), entities.Wall(1, 3),
            entities.Wall(2, 0), agents[0], entities.Wall(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
        ])
        return agents, entity_set
