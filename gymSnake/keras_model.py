import os

import gym
from tensorflow.python.keras import Input

import gym_snake
from rl.agents import SARSAAgent
from tensorflow import keras, uint32
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.optimizers import Adam

import random
import numpy as np

# Source
# https://medium.com/@abhishek.bn93/using-keras-reinforcement-learning-api-with-openai-gym-6c2a35036c83


env = gym_snake.GymSnake()
states = env.observation_space.shape
actions = env.action_space.n

print(env.observation_space)
print(env.observation_space.shape)

file_path = "./"
file_dir = os.path.dirname(file_path)


def save_model(agent):
    agent.save_weights(file_dir, overwrite=True)


def load_model(agent):
    agent.load_weights(file_dir)
    return agent


def get_model(shape, actions):
    model = Sequential()
    model.add(Input(shape=shape, batch_size=1, dtype=uint32))
    # model.add(keras.layers.Input(shape=shape))
    model.add(Flatten())
    model.add(Dense(96, activation="relu"))
    model.add(Dense(48, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(actions, activation="linear"))
    return model


def train_model(agent, steps=10000, render=False):
    agent.fit(env, nb_steps=steps, visualize=render, verbose=1, log_interval=steps)
    return sarsa



model = get_model(states, actions)
print(states)
model.summary()


sarsa = SARSAAgent(model, actions)
sarsa.compile("adam", metrics=["mse"])
#train_model(sarsa, steps=50000)
#save_model(sarsa)
load_model(sarsa)
train_model(sarsa, steps=2000, render=True)


# episodes = 1
# for episode in range(1, episodes + 1):
#     observation = env.reset()
#     done = False
#     score = 0
#     while not done:
#         env.render()
#         action = sarsa.forward(observation)
#         observation, reward, done, info = env.step(action)
#         score += reward
#     print("episode {} score {}".format(episode, score))
#