# Purpose of this file is to test run the environment with human control.
# Should not be packaged into the Gym-package since a reinforcement algorithm doesn't have any use for it.
from multi_control.envs import case
from multi_control.envs import gym_environment
from multi_control.envs.human_input import get_direction

env = gym_environment.GymEnvironment()
state = env.reset()
agents = env.agents

print("agent: " + str(agents))
print("Entity_set: \n")
env.render()

counter = 0
isRunning = True
total_reward = 0
while isRunning:
    direc = []
    for agent in agents:
        direc.append(get_direction())
    observation, reward, done, info = env.step(direc)
    total_reward += reward
    counter += 1
    print("Moves taken:" + str(counter))
    env.render()
    if done:
        isRunning = False
        print("finished")
        print("reward is :{}".format(total_reward))
