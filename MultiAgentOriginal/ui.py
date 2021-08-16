
class UserInterface:
    def __init__(self):
        pass

    def get_direction(self):
        return get_direction()


def get_direction():
    d = {
        "w": 0,  # up
        "a": 1,  # left
        "s": 2,  # down
        "d": 3,  # right
        " ": 4,  # action
    }
    return d[get_input()]


def get_input():
    return input("Pick Direction, by wasd")


def render_field(field):
    for row in field.get_array():
        print(row)
    print("\n")
