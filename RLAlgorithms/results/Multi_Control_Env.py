import os
import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

import gym
import multi_control

from RLAlgorithms.agents.actor_critic_agents.A2C import A2C
from RLAlgorithms.agents.DQN_agents.Dueling_DDQN import Dueling_DDQN
from RLAlgorithms.agents.actor_critic_agents.SAC_Discrete import SAC_Discrete
from RLAlgorithms.agents.actor_critic_agents.A3C import A3C
from RLAlgorithms.agents.policy_gradient_agents.PPO import PPO
from RLAlgorithms.agents.Trainer import Trainer
from RLAlgorithms.utilities.data_structures.Config import Config
from RLAlgorithms.agents.DQN_agents.DDQN import DDQN
from RLAlgorithms.agents.DQN_agents.DDQN_With_Prioritised_Experience_Replay import \
    DDQN_With_Prioritised_Experience_Replay
from RLAlgorithms.agents.DQN_agents.DQN import DQN
from RLAlgorithms.agents.DQN_agents.DQN_With_Fixed_Q_Targets import DQN_With_Fixed_Q_Targets

config = Config()
config.seed = 1
config.environment = gym.make("multi_control-v0")
config.num_episodes_to_run = 250
config.file_to_save_data_results = "e:/Github/Deep-Reinforcement-Learning-Algorithms-with-PyTorch/results/data_and_graphs/multi_control_Results_Data.pkl"
config.file_to_save_results_graph = "e:/Github/Deep-Reinforcement-Learning-Algorithms-with-PyTorch/results/data_and_graphs/multi_control_Results_Graph.png"
config.show_solution_score = False
config.visualise_individual_results = False
config.visualise_overall_agent_results = True
config.standard_deviation_results = 1.0
config.runs_per_agent = 1
config.use_GPU = False
config.overwrite_existing_results_file = False
config.randomise_random_seed = True
config.save_model = False

config.hyperparameters = {
    "Actor_Critic_Agents": {

        "learning_rate": 0.005,
        "linear_hidden_units": [20, 10],
        "final_layer_activation": ["SOFTMAX", None],
        "gradient_clipping_norm": 5.0,
        "discount_rate": 0.99,
        "epsilon_decay_rate_denominator": 1.0,
        "normalise_rewards": True,
        "exploration_worker_difference": 2.0,
        "clip_rewards": False,

        "Actor": {
            "learning_rate": 0.0003,
            "linear_hidden_units": [64, 64],
            "final_layer_activation": "Softmax",
            "batch_norm": False,
            "tau": 0.005,
            "gradient_clipping_norm": 5,
            "initialiser": "Xavier"
        },

        "Critic": {
            "learning_rate": 0.0003,
            "linear_hidden_units": [64, 64],
            "final_layer_activation": None,
            "batch_norm": False,
            "buffer_size": 1000000,
            "tau": 0.005,
            "gradient_clipping_norm": 5,
            "initialiser": "Xavier"
        },

        "min_steps_before_learning": 10,
        "batch_size": 1,
        "discount_rate": 0.99,
        "mu": 0.0,  # for O-H noise
        "theta": 0.15,  # for O-H noise
        "sigma": 0.25,  # for O-H noise
        "action_noise_std": 0.2,  # for TD3
        "action_noise_clipping_range": 0.5,  # for TD3
        "update_every_n_steps": 1,
        "learning_updates_per_learning_session": 1,
        "automatically_tune_entropy_hyperparameter": True,
        "entropy_term_weight": None,
        "add_extra_noise": False,
        "do_evaluation_iterations": True
    }
}

if __name__ == "__main__":
    AGENTS = [SAC_Discrete]
    trainer = Trainer(config, AGENTS)
    trainer.run_games_for_agents()
