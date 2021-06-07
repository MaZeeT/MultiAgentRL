import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


class Agent:

    gamma = 0.99  # Discount factor for past rewards
    max_steps_per_episode = 10000
    eps = np.finfo(np.float32).eps.item()  # Smallest number such that 1.0 + eps != 1.0
    num_inputs = 4
    num_actions = 2
    file_path = "./"
    file_dir = os.path.dirname(file_path)
    should_render = False

    action_probs_history = []
    critic_value_history = []
    rewards_history = []

    def __init__(self):
        self.model = self.nn_model()

    def nn_model(self):
        num_hidden = 128

        inputs = layers.Input(shape=(self.num_inputs,))
        common = layers.Dense(num_hidden, activation="relu")(inputs)
        action = layers.Dense(self.num_actions, activation="softmax")(common)
        critic = layers.Dense(1)(common)

        return keras.Model(inputs=inputs, outputs=[action, critic])

    def sample_action(self, action_probabilities):
        # Sample action from action probability distribution
        action_sample = np.random.choice(self.num_actions, p=np.squeeze(action_probabilities))
        self.action_probs_history.append(tf.math.log(action_probabilities[0, action_sample]))
        return action_sample

    def predictions(self, state):
        # Predict action probabilities and estimated future rewards
        # from environment state
        action_probs, critic_value = agent.model(state)
        self.critic_value_history.append(critic_value[0, 0])
        return action_probs, critic_value

    def run_episode(self, state):
        episode_reward = 0
        for timestep in range(1, self.max_steps_per_episode):
            if self.should_render is True:
                env.render()  # Adding this line would show the attempts
            # of the agent in a pop up window.

            state = tf.convert_to_tensor(state)
            state = tf.expand_dims(state, 0)

            action_probs, critic_value = agent.predictions(state)

            action = agent.sample_action(action_probs)

            # Apply the sampled action in our environment
            state, reward, done, _ = env.step(action)
            self.rewards_history.append(reward)
            episode_reward += reward

            if done is True:
                break
        return episode_reward

    def backpropagation(self, optimizer):
        # Backpropagation
        loss_value = sum(actor_losses) + sum(critic_losses)
        grads = tape.gradient(loss_value, agent.model.trainable_variables)
        optimizer.apply_gradients(zip(grads, agent.model.trainable_variables))

    def clear_history(self):
        self.action_probs_history.clear()
        self.critic_value_history.clear()
        self.rewards_history.clear()

    def save_model(self):
        self.model.save_weights(self.file_dir, overwrite=True)
        print("Saved model")

    def load_model(self):
        self.model.load_weights(self.file_dir)
        print("Loaded model")
        return agent


# Configuration parameters for the whole setup
seed = 42
env = gym.make("CartPole-v0")  # Create the environment
env.seed(seed)
agent = Agent()

agent.load_model()

optimizer = keras.optimizers.Adam(learning_rate=0.01)
huber_loss = keras.losses.Huber()

running_reward = 0
episode_count = 0

isRunning = True
while isRunning:  # Run until solved
    state = env.reset()
    episode_reward = 0
    with tf.GradientTape() as tape:
        episode_reward += agent.run_episode(state)

        # Update running reward to check condition for solving
        running_reward = 0.05 * episode_reward + (1 - 0.05) * running_reward

        # Calculate expected value from rewards
        # - At each timestep what was the total reward received after that timestep
        # - Rewards in the past are discounted by multiplying them with gamma
        # - These are the labels for our critic
        returns = []
        discounted_sum = 0
        for r in agent.rewards_history[::-1]:
            discounted_sum = r + agent.gamma * discounted_sum
            returns.insert(0, discounted_sum)

        # Normalize
        returns = np.array(returns)
        returns = (returns - np.mean(returns)) / (np.std(returns) + agent.eps)
        returns = returns.tolist()

        # Calculating loss values to update our network
        history = zip(agent.action_probs_history, agent.critic_value_history, returns)
        actor_losses = []
        critic_losses = []
        for log_prob, value, ret in history:
            # At this point in history, the critic estimated that we would get a
            # total reward = `value` in the future. We took an action with log probability
            # of `log_prob` and ended up recieving a total reward = `ret`.
            # The actor must be updated so that it predicts an action that leads to
            # high rewards (compared to critic's estimate) with high probability.
            diff = ret - value
            actor_losses.append(-log_prob * diff)  # actor loss

            # The critic must be updated so that it predicts a better estimate of
            # the future rewards.
            critic_losses.append(
                huber_loss(tf.expand_dims(value, 0), tf.expand_dims(ret, 0))
            )

        # Backpropagation
        agent.backpropagation(optimizer)

        # Clear the loss and reward history
        agent.clear_history()

    # Log details
    episode_count += 1
    if episode_count % 10 == 0:
        template = "running reward: {:.2f} at episode {}"
        print(template.format(running_reward, episode_count))

    if running_reward > 190:  # Condition to consider the task solved
        agent.save_model()
        agent.should_render = True

    if running_reward > 195:  # Condition to consider the task solved
        print("Solved at episode {}!".format(episode_count))
        agent.save_model()
        isRunning = False
