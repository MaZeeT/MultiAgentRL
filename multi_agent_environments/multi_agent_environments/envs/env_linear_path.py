# the purpose of this module is to implement the environment designed with the name of Linear Path
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class LinearPath(BaseEnv):
    def __init__(self):
        super().__init__()

    def get_field(self):
        agents = [entities.Agent(3, 8, group_id=1, id=3)]
        agents += [entities.Agent(2, 2, group_id=2, id=2), entities.Agent(3, 4, group_id=2, id=2),
                   entities.Agent(4, 2, group_id=2, id=2)]

        goals = [entities.Goal(9, 7, interactive_with_group_id=1), entities.Goal(10, 14, interactive_with_group_id=1)]

        walls = []
        for i in range(1, 11):
            walls.append(entities.Wall(6, i))

        removableWallsPositions = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]
        rWalls = entities.ParentRemovableWall(removableWallsPositions, interactive_with_group_id=1).children

        removableWallsPositionsTwo = [(6, 11), (6, 12), (6, 13), (6, 14), (6, 15)]
        rWalls += entities.ParentRemovableWall(removableWallsPositionsTwo, interactive_with_group_id=1).children

        explodingWallPositions = []
        for i in range(1, 6):
            explodingWallPositions.append((i, 10))
        eWalls = entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        explodingWallPositions = []
        for i in range(7, 12):
            explodingWallPositions.append((i, 10))
        eWalls += entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        explodingWallPositions = []
        for i in range(7, 12):
            explodingWallPositions.append((i, 4))
        eWalls += entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        set = self.add_outer_walls(x=12, y=16)
        set += agents + goals + walls + rWalls + eWalls

        entity_set = entities.EntitySet(set)
        return agents, entity_set
