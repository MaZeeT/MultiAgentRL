# The purpose of this module is to define the different entities in the snake game.
import random


class Food(object):
    def __init__(self, grid, color=(223, 163, 49)):
        self.grid = grid
        self.color = color
        self.position = None
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, self.grid.width - 1),
            random.randint(0, self.grid.height - 1),
        )


class Snake(object):
    def __init__(self, grid, direction=(1, 0)):
        self.grid = grid
        self.length = 1
        self.positions = [((grid.width / 2), (grid.height / 2))]
        self.direction = direction
        self.color = (17, 24, 47)
        self.self_bite = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        move_x, move_y = self.direction
        head_x, head_y = self.get_head_position()

        new_position = (
            (head_x + move_x) % self.grid.width,  # modulus (%) keeps snake on the grid
            (head_y + move_y) % self.grid.height,
        )

        if len(self.positions) > 2 and new_position in self.positions[2:]:
            self.self_bite = True
        else:
            self.positions.insert(0, new_position)
            if len(self.positions) > self.length:
                self.positions.pop()
