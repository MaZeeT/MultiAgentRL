import gym

from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from rl.agents import SARSAAgent
from rl.policy import EpsGreedyQPolicy

import random
import numpy as np


# Source
# https://medium.com/@abhishek.bn93/using-keras-reinforcement-learning-api-with-openai-gym-6c2a35036c83


class RandomAgent:
    def __init__(self, env):
        self.action_size = env.action_space.n

    def get_action(self, state):
        action = random.choice([0, 1])
        return action


env = gym.make("CartPole-v1")
states = env.observation_space.shape[0]
print("States", states)

actions = env.action_space
print("Actions", actions)

agent = RandomAgent(env)


def get_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(actions, activation="linear"))
    return model


model = get_model(env.observation_space.shape[0], env.action_space.n)
policy = EpsGreedyQPolicy()
sarsa = SARSAAgent(model=model, policy=policy, nb_actions=env.action_space.n)
sarsa.compile("adam", metrics=["mse"])
sarsa.fit(env, nb_steps=50000, visualize=False, verbose=1)
episodes = 10
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0
    while not done:
        env.render()
        action = agent.get_action(state)
        n_state, reward, done, info = env.step(action)
        score += reward
    print("episode {} score {}".format(episode, score))
