from simple_dqn_keras import Agent

import gym
import multi_agent_environments


def run():
    env = gym.make("basic_coop-v0")

    shape = env.observation_space.shape
    n_actions = env.action_space.n

    state = env.reset()
    agents = get_agents(2, n_actions, input_shape=shape)

    counter = 0
    done = False
    while not done:
        actions = choose_actions(agents=agents, state=state)
        observation, reward, done, info = env.step(actions)
        counter += 1
        print(str(actions))
        print(f"observation at step {counter}, is done: {done}: \n{observation}")

        # store the states and actions in the agents replay buffer
        for i in range(len(agents)):
            agents[i].remember(state=state, action=actions[i], new_state=observation, reward=reward, done=done)


def get_agents(agent_count, n_actions, input_shape, batch_size=64, learning_rate=0.01, discount_rate=0.99, epsilon=1):
    agents = []
    for i in range(agent_count):
        agents.append(Agent(alpha=learning_rate,
                            batch_size=batch_size,
                            epsilon=epsilon,
                            gamma=discount_rate,
                            input_dims=input_shape,
                            n_actions=n_actions)
                      )
    return agents


def choose_actions(agents, state):
    actions = []
    for agent in agents:
        actions.append(agent.choose_action(state))
    return actions


if __name__ == "__main__":
    run()
