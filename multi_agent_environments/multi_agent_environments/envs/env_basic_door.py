# the purpose of this module is to implement the environment designed with the name of Basic Door
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class BasicDoor(BaseEnv):
    def __init__(self):
        super().__init__()

    def get_field(self):
        agents, goals, walls, doors = [], [], [], []

        # group 1
        agents += [entities.Agent(2, 2, group_id=1, id=3)]
        goals += [entities.Goal(7, 2, interactive_with_group_id=1)]

        # group 2
        agents += [entities.Agent(2, 6, group_id=2, id=2)]
        goals += [entities.Goal(7, 6, interactive_with_group_id=2)]

        for i in range(4, 9):
            walls.append(entities.Wall(i, 4))

        doorPos = [(5, 3)]
        for i in range(5, 8):
            doorPos.append((5, i))
        door = entities.DoorButtom(doorPos, interactive_with_group_id=1)
        doors += [door] + door.children

        set = self.add_outer_walls(x=9, y=8)
        set += agents + goals + walls + doors

        entity_set = entities.EntitySet(set)
        return agents, entity_set
