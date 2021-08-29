import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class LinearPath(BaseEnv):
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

        # self.observation_space = gym.spaces.Box(low=lowest_id, high=highest_id, shape=(width + 1, height + 1), dtype=np.uint8)
        self.observation_space = gym.spaces.Box(np.array([0, 0]), np.array([width, height]), dtype=np.uint8)

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
