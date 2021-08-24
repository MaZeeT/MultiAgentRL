import gym
import numpy as np

from . import case
from . import entities

class BaseEnv(gym.Env):
    options = {
        0: "up",
        1: "left",
        2: "down",
        3: "right",
        4: "action",
    }
    def __init__(self):
        pass

    def step(self, actions):
            for i in range(self.num_of_agents):
                action = self.options[actions[i]]
                if action == "action":
                    self.entity_set.interact_with_surroundings(self.agents[i])
                else:
                    move_agent_in_list(self.entity_set, self.agents[i], action)
            self.entity_set.step()

            observation = self.entity_set.get_int_array()
            reward = self.calculate_reward()
            done = self.check_if_done()
            info = {}
            return observation, reward, done, info

    def render(self, mode='human'):
        for row in self.entity_set.get_int_array():
            print(row)
        print("\n")

    def calculate_reward(self):
        state_reward = self.entity_set.count_goals(only_activated=True)
        result = state_reward - self.last_state_reward
        self.last_state_reward = self.entity_set.count_goals(only_activated=True)
        return result * self.reward_modifier

    def check_if_done(self):
        return self.entity_set.count_goals(only_activated=True) == self.entity_set.count_goals(only_activated=False)


def move_agent_in_list(entity_set, agent, direction):
    print(f"direction is: {direction}")
    if direction is None: return False
    new_position = agent.check_next_move(direction)
    if not entity_set.is_occupied(new_position):
        agent.move(direction)
        return True
    else:
        return False
