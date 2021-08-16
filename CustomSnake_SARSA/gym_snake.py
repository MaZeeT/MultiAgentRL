import gym
import numpy as np
import pygame
import entity
import utility
import gui
import config
import sys


class GymSnake(gym.Env):
    def __init__(self):
        pygame.init()
        self.grid = utility.grid()
        self.steps = 0
        self.start_pos = [((self.grid.width / 2), (self.grid.height / 2))]
        self.snake = entity.Snake(self.grid)
        self.food = entity.Food(self.grid)
        self.score = 1
        self.clock = pygame.time.Clock()
        self.player_controlled = False

        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(
            low=0, high=3, shape=(1, config.grid_width, config.grid_height), dtype=np.uint8)
        # 1 in shape is the dimension at each position in the array, if it was a picture it would be 3 for RGB,
        # but 1 here for the int marking if it is empty, food, snake-head or tail
        self.state = self.get_state()

    def step(self, action):
        # action = utility.decode_action(action) # todo fix awefull movement encoding to int from tuple
        self.steps += 1
        # self.clock.tick(10)
        control_action = self.control_keys()
        if self.player_controlled:
            action = control_action
        if action is not None:
            self.snake.turn(action)

        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.score += 1
            self.food.randomize_position()

        # the purpose of the vars below are to help see were the observation, reward, done, info consist off.
        observation = self.game_array()
        reward = self.score
        done = self.snake.self_bite
        info = {}
        return observation, reward, done, info

    def reset(self):
        self.game_array()
        self.snake = entity.Snake(self.grid)
        self.food = entity.Food(self.grid)
        self.score = 1
        self.steps = 0

        observation = self.game_array()
        return observation

    def render(self, mode='human'):
        user_interface = None
        if mode == "human":
            if user_interface is None:
                user_interface = gui.Draw(self.grid)

            user_interface.step(self.snake, self.food, self.score)
            pygame.display.update()

    def get_state(self):
        return self.snake.positions, self.snake.direction, self.food.position

    def game_array(self):
        board = np.zeros(shape=[config.grid_width, config.grid_height])
        board = self.game_array_add_snake(board, self.snake)
        board = self.game_array_add_head(board, self.snake)
        board = self.game_array_add_food(board, self.food)
        # self.print_board(board)
        return board

    def game_array_add_head(self, board, snake):
        head = snake.positions[0]
        x = int(head[0])
        y = int(head[1])
        board[x, y] = 1
        return board

    def game_array_add_snake(self, board, snake):
        for bodypart in snake.positions:
            x = int(bodypart[0])
            y = int(bodypart[1])
            board[x, y] = 2
        return board

    def game_array_add_food(self, board, food):
        x = food.position[0]
        y = food.position[1]
        board[x, y] = 3
        return board

    def print_board(self, board):
        print("------------------------------------")
        print(board)
        print("------------------------------------")

    def control_keys(self):
        movement_keys = {
            pygame.K_UP: config.move_up,
            pygame.K_DOWN: config.move_down,
            pygame.K_LEFT: config.move_left,
            pygame.K_RIGHT: config.move_right,
            pygame.K_w: config.move_up,
            pygame.K_s: config.move_down,
            pygame.K_a: config.move_left,
            pygame.K_d: config.move_right,
        }
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # print(self.observation_space) #todo remove
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.reset()
                else:
                    try:
                        self.player_controlled = True
                        return movement_keys[event.key]
                    except KeyError:
                        print("ERROR")
