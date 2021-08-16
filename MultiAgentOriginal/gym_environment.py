import gym
import numpy as np
import case
import logic
from ui import UserInterface


class GymEnvironment(gym.Env):
    def __init__(self):
        self.agents, self.entity_set = case.get_case_two()
        width = self.entity_set.x_max - self.entity_set.x_min
        height = self.entity_set.y_max - self.entity_set.y_min
        lowest_id, highest_id = self.entity_set.get_lowest_and_highest_id()
        num_actions = len(self.options)
        self.num_of_agents = len(self.agents)
        self.action_space = gym.spaces.Discrete(num_actions)
        self.observation_space = gym.spaces.Box(
            low=lowest_id, high=highest_id, shape=(1, width, height), dtype=np.uint8)

    options = {
        0: "up",
        1: "left",
        2: "down",
        3: "right",
        4: "action",
    }

    total_reward = 0

    def step(self, actions):
        for i in range(self.num_of_agents):
            action = self.options[actions[i]]
            if action == "action":
                self.entity_set.interact_with_surroundings(self.agents[i])
            else:
                logic.move_agent_in_list(self.entity_set, self.agents[i], action)
        observation = self.entity_set
        reward = 0
        done = self.check_if_done(self.entity_set)
        info = {}
        return observation, reward, done, info

    def reset(self):
        self.agents, self.entity_set = case.get_case_two()
        observation = self.entity_set
        return observation

    def render(self, mode='human'):
        gui = UserInterface()
        gui.render_field(self.entity_set)

    def check_if_done(self, entity_set):
        return entity_set.count_goals(only_activated=True) == entity_set.count_goals(only_activated=False)
