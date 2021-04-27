import gym
import pygame
import Entity
import Utility
import GUI


class GymSnake(gym.Env):
    def __init__(self):
        pygame.init()
        self.grid = Utility.grid()
        self.steps = 0
        self.start_pos = [((self.grid.width / 2), (self.grid.height / 2))]
        self.snake = Entity.Snake(self.grid)
        self.food = Entity.Food(self.grid)
        self.score = 0
        self.clock = pygame.time.Clock()

        self.action_space = gym.spaces.Discrete(4)
        self.observation_space # todo figure this out
        self.state = self.get_state()

    def step(self, action):
        decoded_action = Utility.decode_action(action)
        self.steps += 1
        self.clock.tick(10)
        self.snake.turn(decoded_action)
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.score += 1
            self.food.randomize_position()

        reward = self.score
        done = self.snake.self_bite
        info = {"Steps passed: {0}".format(self.steps)}
        return self.get_state(), reward, done, info

    def reset(self):
        self.snake = Entity.Snake(self.grid)
        self.food = Entity.Food(self.grid)
        self.score = 0
        self.steps = 0
        return self.get_state()

    def render(self, mode='human'):
        draw = None
        if mode == "human":
            if draw is None:
                draw = GUI.Draw(self.grid)
            draw.step(self.snake, self.food, self.score)
            pygame.display.update()

    def get_state(self):
        return self.snake.positions, self.snake.direction, self.food.position
