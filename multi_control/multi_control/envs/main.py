# Purpose of this file is to test run the environment with human control.
# Should not be packaged into the Gym-package since a reinforcement algorithm doesn't have any use for it.
from multi_control.envs import gym_two_agent_test, gym_basic_cooperation, gym_single_agent_test, gym_linear_path, \
    gym_doors, gym_simple_door
from multi_control.envs.human_input import get_direction

if __name__ == "__main__":
    # env = gym_two_agent_test.GymTwoAgentTest()
    # env = gym_basic_cooperation.GymBasicCooperation()
    # env = gym_linear_path.GymLinearPath()
    # env = gym_single_agent_test.GymSingleAgentTest()
    # env = gym_doors.GymDoors()
    env = gym_simple_door.GymSimpleDoor()

    state = env.reset()
    agents = env.agents

    move_counter = 0
    isRunning = True
    total_reward = 0
    while isRunning:
        env.render()
        actions = []
        for agent in agents:
            actions.append(get_direction())

        observation, reward, done, info = env.step(actions)
        total_reward += reward
        move_counter += 1
        print("Moves taken:" + str(move_counter))

        if done:
            print("finished")
            print("reward is :{}".format(total_reward))
            move_counter = 0
            total_reward = 0
            env.reset()
            # isRunning = False
