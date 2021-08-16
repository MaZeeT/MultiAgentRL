def print_entity_set(entity_set):
    #for column in range(entity_set.max_y):
    #    for row in range(entity_set.max_x):
    #        pass
    render_field(entity_set)


class UserInterface:
    def __init__(self):
        pass

    def render(self, state):
        pass

    def render_field(self, field):
        for row in field.get_array():
            print(row)

    def get_input(self):
        return input("Pick Direction, by wasd")

    def get_direction(self):
        d = {
            "w": 0,  # up
            "a": 1,  # left
            "s": 2,  # down
            "d": 3,  # right
            " ": 4,  # action
        }
        return d[self.get_input()]


def render_field(field):
    for row in field.get_array():
        print(row)
    print("\n")
