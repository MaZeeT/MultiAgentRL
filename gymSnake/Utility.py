# The purpose of this module is to provide utility as easy access to the configuration from the config file.
import random
import Config

move_options = {
    0: Config.move_up,
    1: Config.move_down,
    2: Config.move_left,
    3: Config.move_right,
}


def random_direction():
    rand = random.randint(0, 3)
    return move_options[rand]


def decode_action(action):
    movement = move_options[action]
    return movement


def grid():
    return Grid()


class Grid(object):
    def __init__(self):
        self.width = Config.grid_width
        self.height = Config.grid_height
        self.size = (self.width, self.height)
