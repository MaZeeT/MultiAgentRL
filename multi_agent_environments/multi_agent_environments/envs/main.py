# the purpose of this file is to test run the environment with human control.
# should not be packaged into the Gym-package since a reinforcement algorithm doesn't have any use for it.
from multi_agent_environments.envs import envtest_two_agent, env_basic_cooperation, envtest_single_agent, \
    env_linear_path, \
    env_hold_door, env_basic_door, env_hold_door_with_back_way
from multi_agent_environments.envs.human_input import get_direction

if __name__ == "__main__":
    # env = envtest_single_agent.SingleAgentTest()
    # env = envtest_two_agent.TwoAgentTest()
    env = env_basic_cooperation.BasicCooperation()
    # env = env_basic_door.BasicDoor()
    # env = env_linear_path.LinearPath()
    # env = env_hold_door.HoldDoor()
    # env = env_hold_door_with_back_way.HoldDoorWithBackWay()

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
