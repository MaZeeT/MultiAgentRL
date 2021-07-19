import tensorflow
from tensorflow import keras
from tensorflow.keras import layers
import tf_agents

shape = (1, 1)
num_of_actions = 4



num_hidden = 128

inputs = layers.Input(batch_input_shape=shape)
flat = layers.Flatten()(inputs)
common = layers.Dense(num_hidden, activation="relu")(flat)
action = layers.Dense(num_of_actions, activation="softmax")(common)
critic = layers.Dense(1)(common)
model = keras.Model(inputs=inputs, outputs=[action, critic])
print(model)
actor_network, critic_network = model

sac_agent = tf_agents.agents.SacAgent(actor_network=actor_network, critic_network=critic_network)
sac_agent.initialize()

print(str(sac_agent))
