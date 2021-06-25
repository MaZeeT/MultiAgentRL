import case
from ui import ui

print("this is the main")
c = case.AgentMovementCase()
gui = ui()

gui.render_field(c.field)

print("call entity_field")
field = case.entity_field(c.field)
print(field)
gui.render_field(field)
test = field[1][1]
print(type(test))
print("end of main")

