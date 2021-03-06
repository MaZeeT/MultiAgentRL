from unittest import TestCase

import entities
import logic

class TestObjectLogic(TestCase):
    def test_move_agent_not_occupied(self):
        entity_set = entities.EntitySet([
            entities.Wall(0, 0),
            entities.Wall(0, 2),
        ])
        agent = entities.Agent(0, 1)
        entity_set.append(agent)
        result = logic.move_agent_in_list(entity_set, agent, "left")
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
        result = logic.move_agent_in_list(entity_set, agent, "down")
        self.assertFalse(result)
        self.assertEqual(agent.x, 0)
        self.assertEqual(agent.y, 1)
