def print_entity_set(entity_set):
    for column in range(entity_set.max_x):
        for row in range(entity_set.max_y):
            pass



class UserInterface:
    def __init__(self):
        pass

    def render(self, state):
        pass

    def render_field(self, field):
        for row in field:
            print(row)

    def get_input(self):
        return input("Pick Direction, by wasd")

    def get_direction(self):
        d = {
            "w": "up",
            "a": "left",
            "s": "down",
            "d": "right",
        }
        return d[self.get_input()]


def render_field(field):
    for row in field:
        print(row)
    print("\n")
