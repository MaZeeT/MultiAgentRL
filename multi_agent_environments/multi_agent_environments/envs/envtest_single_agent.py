# the purpose of this module is to make a test environment containing a single agent
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class SingleAgentTest(BaseEnv):
    def __init__(self):
        super().__init__()

    def get_field(self):
        agents = [entities.Agent(2, 1)]
        entity_set = entities.EntitySet([
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Wall(0, 3),
            entities.Wall(1, 0), entities.Goal(1, 2), entities.Wall(1, 3),
            entities.Wall(2, 0), agents[0], entities.Wall(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
        ])
        return agents, entity_set
