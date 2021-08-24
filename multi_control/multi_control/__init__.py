from gym.envs.registration import register

register(
    id='multi_control-v0',
    entry_point='multi_control.envs:GymTwoAgentTest',
)

register(
    id='basic_coop-v0',
    entry_point='multi_control.envs:GymBasicCooperation',
)

register(
    id='single_agent-v0',
    entry_point='multi_control.envs:GymSingleAgentTest',
)

register(
    id='linear_path-v0',
    entry_point='multi_control.envs:GymLinearPath',
)