import tensorflow as tf

from tf_agents.agents.dqn import dqn_agent
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import sequential
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.specs import tensor_spec
from tf_agents.utils import common


class MyAgentDQN:

    def __init__(self, env, learning_rate=1e-3):
        self.env = env
        self.learning_rate = learning_rate
        self.fc_layer_params = (100, 50)
        self.action_tensor_spec = tensor_spec.from_spec(self.env.action_spec())
        self.num_actions = self.action_tensor_spec.maximum - self.action_tensor_spec.minimum + 1
        self.train_env = tf_py_environment.TFPyEnvironment(env)

    # Define a helper function to create Dense layers configured with the right
    # activation and kernel initializer.
    def dense_layer(self, num_units):
        return tf.keras.layers.Dense(
            num_units,
            activation=tf.keras.activations.relu,
            kernel_initializer=tf.keras.initializers.VarianceScaling(
                scale=2.0, mode='fan_in', distribution='truncated_normal'))

    # QNetwork consists of a sequence of Dense layers followed by a dense layer
    # with `num_actions` units to generate one q_value per available action as
    # it's output.
    def get_q_net(self):
        dense_layers = [self.dense_layer(num_units) for num_units in self.fc_layer_params]
        q_values_layer = tf.keras.layers.Dense(
            self.num_actions,
            activation=None,
            kernel_initializer=tf.keras.initializers.RandomUniform(
                minval=-0.03, maxval=0.03),
            bias_initializer=tf.keras.initializers.Constant(-0.2))
        q_net = sequential.Sequential(dense_layers + [q_values_layer])
        return q_net

    def get_optimizer(self):
        optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
        return optimizer

    def get_train_step_counter(self):
        train_step_counter = tf.Variable(0)

    def get_agent(self):
        agent = dqn_agent.DqnAgent(
            self.env.time_step_spec(),
            self.env.action_space(),
            q_network=self.get_q_net(),
            optimizer=self.get_optimizer(),
            td_errors_loss_fn=common.element_wise_squared_loss,
            train_step_counter=self.get_train_step_counter())

        agent.initialize()
        return agent
