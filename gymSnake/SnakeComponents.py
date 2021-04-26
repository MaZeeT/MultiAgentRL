import pygame
import sys
import Entity
import Config
import Utility


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480


class Draw(object):
    def __init__(self, screen_size, grid_width, grid_height, grid_size):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size, 0, 32)
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
        r = pygame.Rect(self.cal_position(food.position), self.grid_size)
        pygame.draw.rect(self.surface, food.color, r)

    def draw_snake(self, snake):
        for p in snake.positions:
            r = pygame.Rect(self.cal_position((p[0], p[1])), self.grid_size)
            pygame.draw.rect(self.surface, snake.color, r)
            pygame.draw.rect(self.surface, (93, 216, 228), r, 1)

    def cal_position(self, position):
        x, y = position
        return x * self.grid_size[0], y * self.grid_size[1]

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
    def __init__(self, mode):
        self.grid = Utility.grid()
        self.mode = mode
        self.start_pos = [((self.grid.width / 2), (self.grid.height / 2))]
        self.snake = Entity.Snake(self.grid)
        self.food = Entity.Food(self.grid)
        self.score = 0
        self.clock = pygame.time.Clock()

    def step(self, action):
        self.clock.tick(10)
        if self.mode is "human":
            self.control_keys()
        else:
            self.snake.turn(action)
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
        self.snake = Entity.Snake(self.grid)
        self.food = Entity.Food(self.grid, (255, 0, 0))
        self.score = 0

    def render(self, mode='human'):
        draw = None
        if mode == "human":
            if draw is None:
                draw = Draw((SCREEN_WIDTH, SCREEN_HEIGHT), self.grid.width, self.grid.height, self.grid.size)
            draw.step(self.snake, self.food, self.score)
            pygame.display.update()

    def print_positions(self):
        snake_position = self.snake.positions[0]
        print("Snake position is x:{0} and y: {1}".format(snake_position[0], snake_position[1]))
        print("Food position is x:{0} and y: {1}".format(self.food.position[0], self.food.position[1]))
        print("Score is: {0}".format(self.score))

    def control_keys(self):
        movement_keys = {
            pygame.K_UP: Config.move_up,
            pygame.K_DOWN: Config.move_down,
            pygame.K_LEFT: Config.move_left,
            pygame.K_RIGHT: Config.move_right,
            pygame.K_w: Config.move_up,
            pygame.K_s: Config.move_down,
            pygame.K_a: Config.move_left,
            pygame.K_d: Config.move_right,
        }
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.reset()
                else:
                    try:
                        self.snake.turn(movement_keys[event.key])
                    except KeyError:
                        print("ERROR")


def main():
    pygame.init()
    game = Game("human")

    is_running = True
    while is_running:
        action = Utility.random_direction()
        game.step(action)


main()
