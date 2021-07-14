import case
from ui import UserInterface
import gym_environment
from MultiAgent.ui import print_entity_set

agents, entity_set = case.get_case_two()
gui = UserInterface()

print("agent: " + str(agents))
print("Entity_set: \n")
print_entity_set(entity_set)

env = gym_environment.GymEnvironment()
counter = 0
isRunning = True
while isRunning:
    direction = gui.get_direction()
    observation, reward, done, info = env.step([direction])
    counter += 1
    print("Moves taken:" + str(counter))
    print_entity_set(observation)
    if done:
        isRunning = False
        print("finished")


