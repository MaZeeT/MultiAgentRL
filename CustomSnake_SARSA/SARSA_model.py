# Source: https://medium.com/@abhishek.bn93/using-keras-reinforcement-learning-api-with-openai-gym-6c2a35036c83
import os

from tensorflow import uint32
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.python.keras import Input
import gym_snake
from rl.agents import SARSAAgent


env = gym_snake.GymSnake()
states = env.observation_space.shape
actions = env.action_space.n

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

load_model(sarsa)
print("loaded model of 18.000.000 steps")
train_model(sarsa, steps=2000000, render=True)
save_model(sarsa)
print("saved model of 20.000.000 steps")

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
