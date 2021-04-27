# The purpose of this module is to implement the game logic of the snake game
import pygame
import sys
import Entity
import Config
import Utility
import GUI


class Game(object):
    def __init__(self, mode):
        pygame.init()
        self.grid = Utility.grid()
        self.mode = mode
        self.start_pos = [((self.grid.width / 2), (self.grid.height / 2))]
        self.snake = Entity.Snake(self.grid)
        self.food = Entity.Food(self.grid)
        self.score = 0
        self.clock = pygame.time.Clock()

    def step(self, action):
        self.clock.tick(10)

        if self.mode == "human":
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

        # self.print_positions()    # Helps to debug non-gui mode by outputting to the console

    def reset(self):
        self.snake = Entity.Snake(self.grid)
        self.food = Entity.Food(self.grid, (255, 0, 0))
        self.score = 0

    def render(self, mode='human'):
        draw = None
        if mode == "human":
            if draw is None:
                draw = GUI.Draw(self.grid)
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
    game = Game("human")
    mode = "human"
    is_running = True
    while is_running:
        action = Utility.random_direction()
        game.step(action)
        game.render(mode)


main()
