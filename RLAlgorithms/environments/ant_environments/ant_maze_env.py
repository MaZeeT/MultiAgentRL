

# NOTE THIS CODE IS TAKEN FROM https://github.com/tensorflow/models/tree/master/research/efficient-hrl/environments
# and is not my code.



from RLAlgorithms.environments.ant_environments.maze_env import MazeEnv
from RLAlgorithms.environments.ant_environments.ant import AntEnv


class AntMazeEnv(MazeEnv):
    MODEL_CLASS = AntEnv
