import gym
import agents

import time


def sleep(sleepTime):
    time.sleep(sleepTime)


# config
env_name = "CartPole-v1"
runtime = 200

# making the environment
environment = gym.make(env_name)
print("Observation space:", environment.observation_space)
print("Action space:", environment.action_space)

# make environment
agent = agents.Smart(environment)
state = environment.reset()

for _ in range(200):
    action = agent.get_action(state)
    state, reward, done, info = environment.step(action)
    environment.render()
    if done == True:
        print("Is done")
        # sleep(5)
        # environment.close()
        # break

print("Closed")
