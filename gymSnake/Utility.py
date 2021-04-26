import random
import Config


# this modules provide utility as easy access to the configuration from the config file.
class Directions(object):
    def __init__(self):
        self.up = Config.move_up
        self.down = Config.move_down
        self.left = Config.move_left
        self.right = Config.move_right

    def random(self):
        return random.choice([self.up, self.down, self.left, self.right])


class Grid(object):
    def __init__(self):
        self.width = Config.grid_width
        self.height = Config.grid_height
        self.size = (self.width, self.height)
