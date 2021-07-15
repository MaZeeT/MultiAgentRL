import gym
import gym_environment
# from tensorflow import keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
# from keras.layers import Dense, Flatten
# from keras.models import Sequential
# from keras.optimizers import Adam

import random
import numpy as np

env = gym_environment.GymEnvironment()
states = env.observation_space.shape
print("States", states)

actions = env.action_space
print("Actions", actions)


def get_model(states, actions):
    shape = (1, 6, 4)
    model = Sequential()
    model.add(Flatten(input_shape=shape, batch_size=1))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(actions, activation="linear"))
    return model


model = get_model(env.observation_space.shape[0], env.action_space.n)

from rl.agents import SARSAAgent
from rl.policy import EpsGreedyQPolicy

policy = EpsGreedyQPolicy()
# sarsa = SARSAAgent(model, nb_actions=env.action_space.n, policy=policy)
sarsa = SARSAAgent(model=model, policy=policy, nb_actions=env.action_space.n)
sarsa.compile("adam", metrics=["mse"])
what_to_do = sarsa.predict()
sarsa.fit(env, nb_steps=50000, visualize=False, verbose=1)
# episodes = 10
# for episode in range(1, episodes + 1):
#    agents, state = env.reset()
#    done = False
#    score = 0
#    while not done:
#        env.render()
#        action = sarsa.forward(state)
#        n_state, reward, done, info = env.step(action)
#        score += reward
#    print("episode {} score {}".format(episode, score))
#
