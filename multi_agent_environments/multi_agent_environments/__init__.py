# the purpose of this module is to register the environments to the Gym toolkit for function gym.make("env_name")
from gym.envs.registration import register

register(
    id='single_agent-v0',
    entry_point='multi_agent_environments.envs:SingleAgentTest',
)

register(
    id='two_agent-v0',
    entry_point='multi_agent_environments.envs:TwoAgentTest',
)

register(
    id='basic_coop-v0',
    entry_point='multi_agent_environments.envs:BasicCooperation',
)

register(
    id='basic_door-v0',
    entry_point='multi_agent_environments.envs:BasicDoor',
)

register(
    id='linear_path-v0',
    entry_point='multi_agent_environments.envs:LinearPath',
)

register(
    id='hold_door-v0',
    entry_point='multi_agent_environments.envs:HoldDoor',
)

register(
    id='hold_door_Backway-v0',
    entry_point='multi_agent_environments.envs:HoldDoorWithBackWay',
)
