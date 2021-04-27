# The purpose of this module is to provide utility as easy access to the configuration from the config file.
import random
import Config


def random_direction():
    return random.choice([Config.move_up, Config.move_down, Config.move_left, Config.move_right])


def grid():
    return Grid()


class Grid(object):
    def __init__(self):
        self.width = Config.grid_width
        self.height = Config.grid_height
        self.size = (self.width, self.height)
