# The purpose of this module is to provide the human interface for the snake game.
import pygame
import Config


class Draw(object):
    def __init__(self, grid):
        self.screen_size = (Config.window_width, Config.window_height)
        self.screen = pygame.display.set_mode(self.screen_size, 0, 32)
        self.grid = grid
        self.font = pygame.font.SysFont("monospace", 32)
        self.surface = pygame.Surface(self.screen.get_size()).convert()

    def draw_grid(self):
        for y in range(0, int(self.grid.height)):
            for x in range(0, int(self.grid.width)):
                color = self.grid.color[(x + y) % 2]  # alternating colors by (x + y) % 2
                r = pygame.Rect((x * self.grid.tile_size[0], y * self.grid.tile_size[1]), self.grid.tile_size)
                pygame.draw.rect(self.surface, color, r)

    def draw_food(self, food):
        r = pygame.Rect(self.cal_position(food.position), self.grid.tile_size)
        pygame.draw.rect(self.surface, food.color, r)

    def draw_snake(self, snake):
        for p in snake.positions:
            r = pygame.Rect(self.cal_position((p[0], p[1])), self.grid.tile_size)
            pygame.draw.rect(self.surface, snake.color, r)
            pygame.draw.rect(self.surface, (93, 216, 228), r, 1)

    def cal_position(self, position):
        x, y = position
        return x * self.grid.tile_size[0], y * self.grid.tile_size[1]

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
