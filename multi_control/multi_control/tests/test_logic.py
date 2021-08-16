from unittest import TestCase
from unittest.mock import patch

from multi_control.envs import entities, base_env


class TestObjectLogic(TestCase):

    def test_move_agent_not_occupied(self):
        entity_set = entities.EntitySet([
            entities.Wall(0, 0),
            entities.Wall(0, 2),
        ])
        agent = entities.Agent(0, 1)
        entity_set.append(agent)
        result = base_env.move_agent_in_list(entity_set, agent, "left")
        self.assertTrue(result)
        self.assertEqual(agent.x, -1)
        self.assertEqual(agent.y, 1)

    def test_move_agent_occupied(self):
        entity_set = entities.EntitySet([
            entities.Wall(0, 0),
            entities.Wall(0, 2),
        ])
        agent = entities.Agent(0, 1)
        entity_set.append(agent)
        result = base_env.move_agent_in_list(entity_set, agent, "down")
        self.assertFalse(result)
        self.assertEqual(agent.x, 0)
        self.assertEqual(agent.y, 1)
