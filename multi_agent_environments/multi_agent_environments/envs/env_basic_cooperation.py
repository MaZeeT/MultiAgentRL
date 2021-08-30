# the purpose of this module is to implement the environment designed with the name of Basic Cooperation
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class BasicCooperation(BaseEnv):
    def __init__(self):
        super().__init__()

    def get_field(self):
        agents, goals, rWalls = [], [], []

        agents += [entities.Agent(3, 3, group_id=1, id=3), entities.Agent(3, 9, group_id=2, id=2)]
        goals += [entities.Goal(2, 15, interactive_with_group_id=1), entities.Goal(4, 15, interactive_with_group_id=2)]

        removableWallsPositions = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]
        rWalls += entities.ParentRemovableWall(removableWallsPositions, interactive_with_group_id=2).children

        removableWallsPositions = [(1, 12), (2, 12), (3, 12), (4, 12), (5, 12)]
        rWalls += entities.ParentRemovableWall(removableWallsPositions, interactive_with_group_id=2).children

        set = self.add_outer_walls(x=6, y=18)
        set += agents + goals + rWalls

        entity_set = entities.EntitySet(set)
        return agents, entity_set
