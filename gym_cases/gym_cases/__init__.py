from gym.envs.registration import register

register(
    id="SnakeEnv-v0",
    entry_point="envs.gym_snake:GymSnake"
)
