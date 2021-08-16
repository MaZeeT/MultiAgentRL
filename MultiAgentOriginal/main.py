import case
from ui import UserInterface
import gym_environment
from MultiAgentOriginal.ui import print_entity_set

agents, entity_set = case.get_case_two()
gui = UserInterface()

print("agent: " + str(agents))
print("Entity_set: \n")
print_entity_set(entity_set)

env = gym_environment.GymEnvironment()
counter = 0
isRunning = True
total_reward = 0
while isRunning:
    direc = []
    for agent in agents:
        direc.append(gui.get_direction())
    observation, reward, done, info = env.step(direc)
    total_reward += reward
    counter += 1
    print("Moves taken:" + str(counter))
    print_entity_set(observation)
    if done:
        isRunning = False
        print("finished")
        print("reward is :{}".format(total_reward))


