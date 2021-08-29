# the purpose of this file is to get an input from a human when testing the environment.
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
