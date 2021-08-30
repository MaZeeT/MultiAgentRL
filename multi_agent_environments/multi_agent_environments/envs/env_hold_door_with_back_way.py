# the purpose of this module is to implement the environment designed with the name of Hold The Door With A Back Way
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class HoldDoorWithBackWay(BaseEnv):
    def __init__(self):
        super().__init__()

    def get_field(self):
        agents, goals, walls, eWalls, doors = [], [], [], [], []

        # group 1
        agents += [entities.Agent(2, 3, group_id=1, id=3), entities.Agent(4, 2, group_id=1, id=3)]
        goals += [entities.Goal(17, 3, interactive_with_group_id=1), entities.Goal(19, 2, interactive_with_group_id=1)]

        # group 2
        agents += [entities.Agent(2, 2, group_id=2, id=2), entities.Agent(3, 4, group_id=2, id=2),
                   entities.Agent(4, 2, group_id=2, id=2)]
        goals += [entities.Goal(19, 9, interactive_with_group_id=2), entities.Goal(19, 14, interactive_with_group_id=2)]

        for i in range(6, 21):
            walls.append(entities.Wall(i, 6))
            walls.append(entities.Wall(i, 11))

        explodingWallPositions = []
        for i in range(12, 16):
            explodingWallPositions.append((17, i))
        eWalls += entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        explodingWallPositions = []
        for i in range(7, 11):
            explodingWallPositions.append((21, i))
        eWalls += entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        explodingWallPositions = []
        for i in range(12, 16):
            explodingWallPositions.append((21, i))
        eWalls += entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        explodingWallPositions = []
        for i in range(22, 25):
            explodingWallPositions.append((i, 6))
        eWalls += entities.ExplodingWall(explodingWallPositions, interactive_with_group_id=2).children

        doorPos = [(9, 10)]
        for i in range(12, 16):
            doorPos.append((9, i))
        door = entities.DoorButton(doorPos, interactive_with_group_id=1)
        doors += [door] + door.children

        doorPos = [(15, 10)]
        for i in range(12, 16):
            doorPos.append((15, i))
        door = entities.DoorButton(doorPos, interactive_with_group_id=1)
        doors += [door] + door.children

        doorPos = [(12, 12)]
        for i in range(7, 11):
            doorPos.append((12, i))
        door = entities.DoorButton(doorPos, interactive_with_group_id=1)
        doors += [door] + door.children

        set = self.add_outer_walls(x=25, y=16)
        set += agents + goals + walls + eWalls + doors

        entity_set = entities.EntitySet(set)
        return agents, entity_set
