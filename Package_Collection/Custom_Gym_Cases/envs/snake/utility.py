# The purpose of this module is to provide utility as easy access to the configuration from the config file.
import random
import config

move_options = {
    0: config.move_up,
    1: config.move_down,
    2: config.move_left,
    3: config.move_right,
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
        self.width = config.grid_width
        self.height = config.grid_height
        self.color = config.grid_colors
        self.tile_size = (config.window_width / self.width, config.window_height / self.height)
