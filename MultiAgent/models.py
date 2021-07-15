import abc
import tensorflow
from tensorflow import keras
from keras.layers import Flatten, Dense, Input
from keras.models import Sequential

class Base(abc):
    def __init__(self, my_agent, environment):
        self.my_agent = my_agent
        self.environment = environment

    def model(self, shape, actions):
        #shape = (1, 6, 4)
        model = Sequential()
        model.add(Flatten(input_shape=shape, batch_size=1))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(24, activation="relu"))
        model.add(Dense(actions, activation="linear"))
        return model



    def predict(self):
        pass
        # prediction = None
        # return prediction


class ActorCritic(abc):
    def __init__(self, my_agent, environment):
        pass

    def actor_model(self):
        num_hidden = 128

        inputs = Input(batch_input_shape=self.input_shape)
        flat = Flatten()(inputs)
        common = Dense(num_hidden, activation="relu")(flat)
        action = Dense(self.num_actions, activation="softmax")(common)
        critic = Dense(1)(common)
        return keras.Model(inputs=inputs, outputs=[action, critic])

    def predict(self):
        pass
