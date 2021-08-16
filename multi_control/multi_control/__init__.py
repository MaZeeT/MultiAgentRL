from gym.envs.registration import register

register(
    id='multi_control-v0',
    entry_point='multi_control.envs:GymEnvironment',
)
