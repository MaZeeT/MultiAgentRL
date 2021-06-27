import entities
from multiAgentCases import test_cases

case = test_cases.CaseLinearPath()
agent = entities.Agent(x=3, y=3)

print("x:{}, y:{}".format(agent.x, agent.y))
agent.move("down")
agent.move("right")
print("x:{}, y:{}".format(agent.x, agent.y))
