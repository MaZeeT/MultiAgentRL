from gym.envs.registration import register

register(
    id='multi_agent_environments-v0',
    entry_point='multi_agent_environments.envs:GymTwoAgentTest',
)

register(
    id='basic_coop-v0',
    entry_point='multi_agent_environments.envs:GymBasicCooperation',
)

register(
    id='single_agent-v0',
    entry_point='multi_agent_environments.envs:GymSingleAgentTest',
)

register(
    id='linear_path-v0',
    entry_point='multi_agent_environments.envs:GymLinearPath',
)

register(
    id='doors-v0',
    entry_point='multi_agent_environments.envs:GymDoors',
)

register(
    id='simple_door-v0',
    entry_point='multi_agent_environments.envs:GymSimpleDoor',
)
