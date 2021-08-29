# the purpose of this module is to make a test environment containing two agents
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class TwoAgentTest(BaseEnv):
    def __init__(self):
        super().__init__()

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
