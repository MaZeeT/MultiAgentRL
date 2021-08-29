import gym
import numpy as np

from . import entities
from multi_agent_environments.envs.base_env import BaseEnv


class GymSimpleDoor(BaseEnv):
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
