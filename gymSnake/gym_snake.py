import gym
import pygame
import entity
import utility
import gui


class GymSnake(gym.Env):
    def __init__(self):
        pygame.init()
        self.grid = utility.grid()
        self.steps = 0
        self.start_pos = [((self.grid.width / 2), (self.grid.height / 2))]
        self.snake = entity.Snake(self.grid)
        self.food = entity.Food(self.grid)
        self.score = 0
        self.clock = pygame.time.Clock()

        self.action_space = gym.spaces.Discrete(4)
        self.observation_space  # todo figure this out... [Array of snake positions; direction of the snake; food position]
        # looks like it is the shape of the returned state... Is it velocity + angel + position that is return or something else like a picture in a 3color, height, width.
        self.state = self.get_state()

    def step(self, action):
        decoded_action = utility.decode_action(action)
        self.steps += 1
        self.clock.tick(10)
        self.snake.turn(decoded_action)
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.score += 1
            self.food.randomize_position()

        # the purpose of the vars below are to help see were the observation, reward, done, info consist off.
        observation = self.get_state()
        reward = self.score
        done = self.snake.self_bite
        info = {"Steps passed: {0}".format(self.steps)}
        return observation, reward, done, info

    def reset(self):
        self.snake = entity.Snake(self.grid)
        self.food = entity.Food(self.grid)
        self.score = 0
        self.steps = 0
        return self.get_state()

    def render(self, mode='human'):
        user_interface = None
        if mode == "human":
            if user_interface is None:
                user_interface = gui.Draw(self.grid)

            user_interface.step(self.snake, self.food, self.score)
            pygame.display.update()

    def get_state(self):
        return self.snake.positions, self.snake.direction, self.food.position
