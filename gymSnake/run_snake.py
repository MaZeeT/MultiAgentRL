import gym_snake
import utility


def main():
    game = gym_snake.GymSnake()
    mode = "human"
    is_running = True
    while is_running:
        action = utility.random_direction()
        print(action)
        game.step(action)
        game.render(mode)


main()
