import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

#import MultiAgent.gym_environment
import gym_environment


os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


class Agent:
    gamma = 0.99  # Discount factor for past rewards
    max_steps_per_episode = 100000
    eps = np.finfo(np.float32).eps.item()  # Smallest number such that 1.0 + eps != 1.0
    file_path = "./"
    file_dir = os.path.dirname(file_path)
    should_render = True

    actor_losses = None
    critic_losses = None

    action_probs_history = []
    critic_value_history = []
    rewards_history = []

    def __init__(self,
                 num_actions,
                 input_shape,
                 optimize_function=keras.optimizers.Adam(learning_rate=0.001),
                 loss_function=keras.losses.Huber()
                 ):
        self.input_shape = input_shape
        self.num_actions = num_actions
        self.optimizer = optimize_function
        self.loss = loss_function

        self.model = self.nn_model()

    def nn_model(self):
        num_hidden = 128

        inputs = layers.Input(batch_input_shape=self.input_shape)
        flat = layers.Flatten()(inputs)
        common = layers.Dense(num_hidden, activation="relu")(flat)
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
        action_probs, critic_value = self.model(state)
        self.critic_value_history.append(critic_value[0, 0])
        return action_probs

    def step(self, state):
        if self.should_render is True:
            env.render()
        state = tf.convert_to_tensor(state)
        state = tf.expand_dims(state, 0)

        action_probs = self.predictions(state)

        action = self.sample_action(action_probs)
        return env.step(action)

    def run_episode(self, state):
        episode_reward = 0

        with tf.GradientTape() as tape:
            for timestep in range(1, self.max_steps_per_episode):
                # Apply the sampled action in our environment
                state, reward, done, _ = self.step(state)
                self.rewards_history.append(reward)
                episode_reward += reward
                if done is True:
                    break

            # Calculate expected value from rewards
            expected_reward = agent.cal_expected_reward()
            # Normalize
            norm_expected_reward = agent.normalize(expected_reward)
            # Calculating loss values to update our network
            agent.cal_loss_values(norm_expected_reward)
            # Backpropagation
            agent.backpropagation(tape)

            # Clear the loss and reward history
            agent.clear_history()

        return episode_reward

    def backpropagation(self, tape):
        # Backpropagation
        loss_value = sum(self.actor_losses) + sum(self.critic_losses)
        grads = tape.gradient(loss_value, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

    def normalize(self, values):
        # Normalize
        values = np.array(values)
        values = (values - np.mean(values)) / (np.std(values) + self.eps)
        return values.tolist()

    def cal_loss_values(self, returns):
        history = zip(self.action_probs_history, self.critic_value_history, returns)
        self.actor_losses = []
        self.critic_losses = []
        for log_prob, value, ret in history:
            # At this point in history, the critic estimated that we would get a
            # total reward = `value` in the future. We took an action with log probability
            # of `log_prob` and ended up recieving a total reward = `ret`.
            # The actor must be updated so that it predicts an action that leads to
            # high rewards (compared to critic's estimate) with high probability.
            diff = ret - value
            self.actor_losses.append(-log_prob * diff)  # actor loss

            # The critic must be updated so that it predicts a better estimate of
            # the future rewards.
            self.critic_losses.append(
                self.loss(tf.expand_dims(value, 0), tf.expand_dims(ret, 0))
            )

    def cal_expected_reward(self):
        # Calculate expected value from rewards
        expected_reward = []
        discounted_sum = 0
        for r in self.rewards_history[::-1]:
            discounted_sum = r + self.gamma * discounted_sum
            expected_reward.insert(0, discounted_sum)
        return expected_reward

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
env = gym_environment.GymEnvironment()
num_actions = env.action_space.n
input_shapes = env.observation_space.shape
print(num_actions)
print(input_shapes)


optimizer = keras.optimizers.Adam(learning_rate=0.001)
loss = keras.losses.Huber()
agent = Agent(num_actions, input_shapes, optimizer, loss)

# agent.load_model()

running_reward = 0
episode_count = 0

isRunning = True
while isRunning:  # Run until solved
    state = env.reset()
    episode_reward = 0
    episode_reward += agent.run_episode(state)

    # Update running reward to check condition for solving
    running_reward = 0.05 * episode_reward + (1 - 0.05) * running_reward

    # Log details
    episode_count += 1
    if episode_count % 10 == 0:
        template = "running reward: {:.2f} at episode {}"
        print(template.format(running_reward, episode_count))

    # if running_reward > 190:  # Condition to consider the task solved
    #     agent.save_model()
    #     agent.should_render = True
#
    # if running_reward > 195:  # Condition to consider the task solved
    #     print("Solved at episode {}!".format(episode_count))
    #     agent.save_model()
    #     isRunning = False
#