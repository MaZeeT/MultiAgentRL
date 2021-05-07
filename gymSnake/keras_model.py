import gym
import gym_snake
import random

from tensorflow import keras
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

def get_model(shape, actions):
    model = Sequential()
    model.add(keras.layers.Input(shape=shape))
    model.add(Flatten())
    model.add(Dense(24, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(actions, activation="linear"))
    return model


model = get_model(states, actions)
model.summary()

from rl.agents import SARSAAgent


sarsa = SARSAAgent(model, actions)
sarsa.compile("adam", metrics=["mse"])
sarsa.fit(env, nb_steps=50000, visualize=False, verbose=1)
episodes = 10
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0
    while not done:
        env.render()
        action = random.randint(0, 4)
        n_state, reward, done, info = env.step(action)
        score += reward
    print("episode {} score {}".format(episode, score))