import case
import ui
import gym_environment
from MultiAgentOriginal.ui import render_field

agents, entity_set = case.get_case_two()

print("agent: " + str(agents))
print("Entity_set: \n")
render_field(entity_set)

env = gym_environment.GymEnvironment()
counter = 0
isRunning = True
total_reward = 0
while isRunning:
    direc = []
    for agent in agents:
        direc.append(ui.get_direction())
    observation, reward, done, info = env.step(direc)
    total_reward += reward
    counter += 1
    print("Moves taken:" + str(counter))
    render_field(observation)
    if done:
        isRunning = False
        print("finished")
        print("reward is :{}".format(total_reward))
