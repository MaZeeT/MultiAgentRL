import gym
import numpy as np

import case
import entities


class GymEnvironment(gym.Env):
    def __init__(self):
        self.agents, self.entity_set = case.get_case_two()
        width = self.entity_set.x_max - self.entity_set.x_min
        height = self.entity_set.y_max - self.entity_set.y_min
        lowest_id, highest_id = self.entity_set.get_lowest_and_highest_id()
        num_actions = len(self.options)
        self.num_of_agents = len(self.agents)
        self.action_space = gym.spaces.Discrete(num_actions)

        # action_space: Float and Box are used to simulate an continuous action space
        # at index 0 the movement of the x-axis
        # at index 1 the movement of the y-axis
        # at index 2 the activation of an action
        #self.action_space = gym.spaces.Box(low=np.array([-1.0, -1.0, 0.0]), high=np.array([1.0, 1.0, 1.0]), dtype=np.float16)
        self.observation_space = gym.spaces.Box(
            low=lowest_id, high=highest_id, shape=(width+1, height+1), dtype=np.uint8)


    options = {
        0: "up",
        1: "left",
        2: "down",
        3: "right",
        4: "action",
    }

    total_reward = 0

    def step(self, actions):
        if isinstance(actions[0], int):
            for i in range(self.num_of_agents):
                action = self.options[actions[i]]
                if action == "action":
                    self.entity_set.interact_with_surroundings(self.agents[i])
                else:
                    move_agent_in_list(self.entity_set, self.agents[i], action)
        else:
            for i in range(self.num_of_agents):
                action = actions[i]
                x = action[0]
                y = action[1]
                act = action[2]
                if act > 0.5:
                    self.entity_set.interact_with_surroundings(self.agents[i])
                else:
                    movement = None
                    if x > 0.33: movement = "left"
                    if x < -0.33: movement = "right"
                    if y > 0.33: movement = "down"
                    if y < -0.33: movement = "up"
                    move_agent_in_list(self.entity_set, self.agents[i], movement)
                print(f"x:{x}, y:{y}, act:{act}")

        observation = self.entity_set.get_int_array()
        reward = 0
        done = self.check_if_done()
        info = {}
        return observation, reward, done, info

    def reset(self):
        self.agents, self.entity_set = case.get_case_two()
        observation = self.entity_set.get_int_array()
        return observation

    def render(self, mode='human'):
        for row in self.entity_set.get_array():
            print(row)
        print("\n")

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


def count_activated_entities(entity_set):
    count = 0
    for entity in entity_set.get_raw_set():
        if isinstance(entity, entities.InteractiveEntity):
            if entity.activated is True:
                count += 1
    return count