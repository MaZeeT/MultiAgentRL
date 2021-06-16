from entities import *
import gym


class BaseCase(gym.Env):
    act = {
        0: "up",
        1: "down",
        2: "left",
        3: "right",
        4: "action_one",
        5: "action_two",
    }
    agents = []
    interactables = []

    def step(self, action):
        for a in action:
            if a <= 3:
                print("move")
            else:
                print("do action")

    def reset(self):
        pass

    def render(self, mode='human'):
        self.print_field()

    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.entities = []

    def edge_walls(self):
        top_y = 0
        bottom_y = self.height - 1
        left_x = 0
        right_x = self.width - 1

        # fill top
        for x in range(left_x, right_x + 1):
            self.entities.append(Wall(x, top_y))

        # fill bottom
        for x in range(left_x, right_x + 1):
            self.entities.append(Wall(x, bottom_y))

        # fill left side
        for y in range(top_y + 1, bottom_y):
            self.entities.append(Wall(left_x, y))

        # fill right side
        for y in range(top_y + 1, bottom_y):
            self.entities.append(Wall(right_x, y))

    def grid_print(self, array):
        for x in array:  # outer loop
            for i in x:  # inner loop
                print(i, end=" ")  # print the elements
            print()

    def print_field(self):
        field = [[0 for i in range(self.height)] for j in range(self.width)]

        for entity in self.entities:
            field[entity.x][entity.y] = entity.id

        self.grid_print(field)

    def print_entities(self):
        for entity in self.entities:
            print(str(entity.x) + " " + str(entity.y))
        print("-------")


class BasicTestCase(BaseCase):
    def __init__(self):
        x = 13
        y = 7
        super().__init__(x, y)
        self.edge_walls()
        self.add_agents()
        self.add_gates()
        self.add_goal()

    def add_agents(self):
        a = Agent(2, 3)
        b = Agent(6, 3)

        self.entities.append(a)
        self.entities.append(b)

        self.agents.append(a)
        self.agents.append(b)

    def add_gates(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                for i in range(1, 5):
                    g_a = Gate(4, i, entity)
                    g_b = Gate(8, i, entity)

                    self.entities.append(g_a)
                    self.entities.append(g_b)

                    self.interactables.append(g_a)
                    self.interactables.append(g_b)

    def add_goal(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                self.entities.append(Goal(10, 2, entity))
                self.entities.append(Goal(10, 4, entity))


class CaseLinearPath(BaseCase):
    def __init__(self):
        x = 13
        y = 17
        super().__init__(x, y)
        self.edge_walls()
        self.add_walls()
        self.add_agents()
        self.add_gates()
        self.add_goal()

    def add_walls(self):
        for i in range(1, 11):
            self.entities.append(Wall(6, i))

    def add_agents(self):
        self.entities.append(Agent(2, 2))
        self.entities.append(Agent(4, 2))
        self.entities.append(Agent(3, 4))

        self.entities.append(Agent(3, 8))

    def add_gates(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                self.entities.append(Gate(1, 6, entity))
                self.entities.append(Gate(2, 6, entity))
                self.entities.append(Gate(3, 6, entity))
                self.entities.append(Gate(4, 6, entity))
                self.entities.append(Gate(5, 6, entity))

                self.entities.append(Gate(1, 10, entity))
                self.entities.append(Gate(2, 10, entity))
                self.entities.append(Gate(3, 10, entity))
                self.entities.append(Gate(4, 10, entity))
                self.entities.append(Gate(5, 10, entity))

                self.entities.append(Gate(6, 11, entity))
                self.entities.append(Gate(6, 12, entity))
                self.entities.append(Gate(6, 13, entity))
                self.entities.append(Gate(6, 14, entity))
                self.entities.append(Gate(6, 15, entity))

                self.entities.append(Gate(7, 10, entity))
                self.entities.append(Gate(8, 10, entity))
                self.entities.append(Gate(9, 10, entity))
                self.entities.append(Gate(10, 10, entity))
                self.entities.append(Gate(11, 10, entity))

                self.entities.append(Gate(7,  4, entity))
                self.entities.append(Gate(8,  4, entity))
                self.entities.append(Gate(9,  4, entity))
                self.entities.append(Gate(10, 4, entity))
                self.entities.append(Gate(11, 4, entity))

    def add_goal(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                self.entities.append(Goal(9, 7, entity))
                self.entities.append(Goal(10, 14, entity))

class HoldTheDoorCase(BaseCase):
    def __init__(self):
        x = 22
        y = 17
        super().__init__(x, y)
        self.edge_walls()
        self.add_walls()
        self.add_agents()
        self.add_gates()
        self.add_door()
        self.add_goal()

    def add_walls(self):
        for i in range(6, 21):
            self.entities.append(Wall(i, 6))
            self.entities.append(Wall(i, 11))

    def add_agents(self):
        self.entities.append(Agent(2, 3))
        self.entities.append(Agent(4, 2))

        self.entities.append(Agent(7, 2))
        self.entities.append(Agent(9, 4))
        self.entities.append(Agent(11, 3))

    def add_gates(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                self.entities.append(Gate(17, 12, entity))
                self.entities.append(Gate(17, 13, entity))
                self.entities.append(Gate(17, 14, entity))
                self.entities.append(Gate(17, 15, entity))

    def add_door(self):
        self.entities.append(Door(9, 10, "down"))
        self.entities.append(Door(9, 11, "down"))
        self.entities.append(Door(9, 12, "down"))
        self.entities.append(Door(9, 13, "down"))
        self.entities.append(Door(9, 14, "down"))
        self.entities.append(Door(9, 15, "down"))

        self.entities.append(Door(12, 12, "up"))
        self.entities.append(Door(12, 11, "up"))
        self.entities.append(Door(12, 10, "up"))
        self.entities.append(Door(12, 9, "up"))
        self.entities.append(Door(12, 8, "up"))
        self.entities.append(Door(12, 7, "up"))

        self.entities.append(Door(15, 10, "down"))
        self.entities.append(Door(15, 11, "down"))
        self.entities.append(Door(15, 12, "down"))
        self.entities.append(Door(15, 13, "down"))
        self.entities.append(Door(15, 14, "down"))
        self.entities.append(Door(15, 15, "down"))

    def add_goal(self):
        for entity in self.entities:
            if isinstance(entity, Agent):
                self.entities.append(Goal(17, 3, entity))
                self.entities.append(Goal(19, 2, entity))

                self.entities.append(Goal(19, 9, entity))
                self.entities.append(Goal(19, 14, entity))


case = BasicTestCase()
case.print_field()
