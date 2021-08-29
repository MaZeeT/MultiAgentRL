# the purpose of this module is to implement the environment designed with the name of Basic Cooperation
import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class BasicCooperation(BaseEnv):
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
        agents = [entities.Agent(3, 3, group_id=1, id=3), entities.Agent(3, 9, group_id=2, id=2)]
        goals = [entities.Goal(2, 15, interactive_with_group_id=1), entities.Goal(4, 15, interactive_with_group_id=2)]

        removableWallsPositions = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]
        rWalls = entities.ParentRemovableWall(removableWallsPositions, interactive_with_group_id=2)

        interactiveWallPositions = [(1, 12), (2, 12), (3, 12), (4, 12), (5, 12)]
        iWalls = entities.ParentRemovableWall(interactiveWallPositions, interactive_with_group_id=2)

        set = self.add_outer_walls(x=6, y=18)
        set += agents + goals + rWalls.children + iWalls.children

        entity_set = entities.EntitySet(set)
        return agents, entity_set
