import case
from ui import UserInterface
import logic
from MultiAgent.ui import print_entity_set

agent, entity_set = case.get_case()
gui = UserInterface()


def step(action):
    logic.move_agent_in_list(entity_set, agent, action)
    print_entity_set(entity_set)


def check_winning_condition(entity_set):
    return entity_set.count_goals(only_activated=True) == entity_set.count_goals(only_activated=False)


print("agent: " + str(agent))
print("Entity_set: \n")
print_entity_set(entity_set)

counter = 0
isRunning = True
while isRunning:
    direction = gui.get_direction()
    if direction == "exit": isRunning = False
    step(direction)
    counter += 1
    is_done = check_winning_condition(entity_set)
    if is_done:
        isRunning = False
        print(str(counter))

# print("this is the main")
# c = case.AgentMovementCase()
# ui = UserInterface()
#
# ui.render_field(c.field)
#
# print("call entity_field")
# field = case.entity_field(c.field)
# print(field)
# ui.render_field(field)
# test = field[1][1]
# print(type(test))
# print("end of main")
