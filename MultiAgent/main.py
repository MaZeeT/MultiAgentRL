import case
from ui import UserInterface

print("this is the main")
c = case.AgentMovementCase()
ui = UserInterface()

ui.render_field(c.field)

print("call entity_field")
field = case.entity_field(c.field)
print(field)
ui.render_field(field)
test = field[1][1]
print(type(test))
print("end of main")

