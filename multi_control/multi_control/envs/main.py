# Purpose of this file is to test run the environment with human control.
# Should not be packaged into the Gym-package since a reinforcement algorithm doesn't have any use for it.
from multi_control.envs import case, gym_two_agent_test, gym_basic_cooperation
from multi_control.envs.human_input import get_direction

if __name__ == "__main__":
    #env = gym_two_agent_test.GymTwoAgentTest()
    env = gym_basic_cooperation.GymBasicCooperation()
    state = env.reset()
    agents = env.agents

    print("Entity_set:")
    env.render()

    move_counter = 0
    isRunning = True
    total_reward = 0
    while isRunning:
        actions = []
        for agent in agents:
            actions.append(get_direction())

        observation, reward, done, info = env.step(actions)
        total_reward += reward
        move_counter += 1
        print("Moves taken:" + str(move_counter))
        env.render()

        if done:
            isRunning = False
            print("finished")
            print("reward is :{}".format(total_reward))
