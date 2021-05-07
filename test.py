import envs
import gym

env = gym.make("SnakeEnv-v0")
env.step()
env.reset()
env.render()
