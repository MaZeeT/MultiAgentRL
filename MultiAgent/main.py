import case
from ui import UserInterface
from MultiAgent.ui import print_entity_set

agent, entity_set = case.get_case()

print("agent: " + str(agent))
print("Entity_set: \n")
print_entity_set(entity_set)

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
