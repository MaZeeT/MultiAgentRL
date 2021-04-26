import pygame
import sys
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = (20, 20)
GRID_WIDTH = SCREEN_HEIGHT / GRID_SIZE[0]
GRID_HEIGHT = SCREEN_WIDTH / GRID_SIZE[1]

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Food(object):
    def __init__(self, grid_width, grid_height, grid_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid_size = grid_size
        self.position = (0, 0)  # todo make default a random position instead of 0,0
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, int(self.grid_width - 1)) * self.grid_size[0],
            random.randint(0, int(self.grid_height - 1)) * self.grid_size[1]
        )


class Snake(object):
    def __init__(self, start_position):
        self.length = 1
        self.positions = start_position
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.score = 0
        self.time = 0
        self.self_bite = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE[0])) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE[1])) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.self_bite = True
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()


class Draw(object):
    def __init__(self, screen, grid_width, grid_height, grid_size):
        self.screen = screen
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid_size = grid_size
        self.grid_color = ((93, 216, 228), (93, 150, 228))
        self.font = pygame.font.SysFont("monospace", 32)
        self.surface = pygame.Surface(self.screen.get_size()).convert()

    def draw_grid(self):
        for y in range(0, int(self.grid_height)):
            for x in range(0, int(self.grid_width)):
                color = self.grid_color[(x + y) % 2]  # alternating colors by (x + y) % 2
                r = pygame.Rect((x * self.grid_size[0], y * self.grid_size[1]), self.grid_size)
                pygame.draw.rect(self.surface, color, r)

    def draw_food(self, food):
        r = pygame.Rect(food.position, self.grid_size)
        pygame.draw.rect(self.surface, food.color, r)

    def draw_snake(self, snake):
        for p in snake.positions:
            r = pygame.Rect((p[0], p[1]), self.grid_size)
            pygame.draw.rect(self.surface, snake.color, r)
            pygame.draw.rect(self.surface, (93, 216, 228), r, 1)

    def draw_score(self, score):
        score_text = self.font.render("Score {0}".format(score), True, (255, 0, 0))
        self.screen.blit(score_text, (5, 10))

    def draw_timer(self):
        timer_text = self.font.render("Time {0}".format(int(pygame.time.get_ticks() / 1000)), True, (255, 0, 0))
        self.screen.blit(timer_text, (5, 50))

    def step(self, snake, food, score):
        self.draw_grid()
        self.draw_snake(snake)
        self.draw_food(food)
        self.screen.blit(self.surface, (0, 0))
        self.draw_score(score)
        self.draw_timer()


class Game(object):
    def __init__(self, mode, draw):
        self.mode = mode
        self.draw = draw
        self.snake = Snake([((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))])
        self.food = Food(GRID_WIDTH, GRID_HEIGHT, GRID_SIZE)
        self.score = 0
        self.clock = pygame.time.Clock()

    def step(self):
        self.clock.tick(10)
        self.handle_keys()
        self.snake.move()
        if self.snake.self_bite:
            self.reset()

        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.score += 1
            self.food.randomize_position()
        self.print_positions()
        self.render(self.mode)

    def reset(self):
        self.snake = Snake([((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))])
        self.score = 0

    def render(self, mode='human'):
        if mode == "human":
            self.draw.step(self.snake, self.food, self.score)
            pygame.display.update()

    def print_positions(self):
        snake_position = self.snake.positions[0]
        print("Snake position is x:{0} and y: {1}".format(snake_position[0], snake_position[1]))
        print("Food position is x:{0} and y: {1}".format(self.food.position[0], self.food.position[1]))

    def handle_keys(self):
        movement_keys = {
            pygame.K_UP: UP,
            pygame.K_DOWN: DOWN,
            pygame.K_LEFT: LEFT,
            pygame.K_RIGHT: RIGHT,
            pygame.K_w: UP,
            pygame.K_s: DOWN,
            pygame.K_a: LEFT,
            pygame.K_d: RIGHT,
        }
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    try:
                        self.snake.turn(movement_keys[event.key])
                    except KeyError:
                        print("ERROR")


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    render = Draw(screen, GRID_WIDTH, GRID_HEIGHT, GRID_SIZE)
    game = Game("human", render)

    is_running = True
    while is_running:
        game.step()


main()
