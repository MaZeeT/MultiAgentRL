from unittest import TestCase
from unittest.mock import patch
import logic
import case
import entities
import ui


class TestLogic(TestCase):
    def setUp(self):
        self.field = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
        x = 3
        y = 3

        self.field = case.entity_field(self.field)
        self.agents = []
        agent = entities.Agent(x, y)
        self.agents.append(agent)
        self.field[x][y] = agent

    def test_move_agent_up(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "up")
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 2)

    def test_move_agent_up_two(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "up")
        logic.move_agent(self.field, agent, "up")
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 1)

    def test_move_agent_down(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "down")
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 4)

    def test_move_agent_left(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "left")
        self.assertEqual(agent.x, 2)
        self.assertEqual(agent.y, 3)

    def test_move_agent_right(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "right")
        self.assertEqual(agent.x, 4)
        self.assertEqual(agent.y, 3)

    def test_validity_of_move_up_true(self):
        agent = self.agents[0]
        result = logic.is_move_valid(self.field, agent, "up")
        self.assertTrue(result)

    def test_validity_of_move_up_false(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "up")
        logic.move_agent(self.field, agent, "up")
        result = logic.is_move_valid(self.field, agent, "up")
        self.assertFalse(result)

    def test_validity_of_move_right_true(self):
        agent = self.agents[0]
        result = logic.is_move_valid(self.field, agent, "right")
        self.assertTrue(result)

    def test_validity_of_move_right_false(self):
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "right")
        logic.move_agent(self.field, agent, "right")
        result = logic.is_move_valid(self.field, agent, "right")
        self.assertFalse(result)

    def test_invalid_move_up(self):
        agent = self.agents[0]
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 3)

        self.field, self.agents[0] = logic.move_agent(self.field, agent, "up")
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 2)

        self.field, self.agents[0] = logic.move_agent(self.field, agent, "up")
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 1)

        logic.move_agent(self.field, self.agents[0], "up")
        self.assertEqual(self.agents[0].x, 3)
        self.assertEqual(self.agents[0].y, 1)

    def test_invalid_move_right(self):
        agent = self.agents[0]
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 3)

        logic.move_agent(self.field, agent, "right")
        self.assertEqual(agent.x, 4)
        self.assertEqual(agent.y, 3)

        logic.move_agent(self.field, agent, "right")
        self.assertEqual(agent.x, 5)
        self.assertEqual(agent.y, 3)

        logic.move_agent(self.field, agent, "right")
        self.assertEqual(agent.x, 5)
        self.assertEqual(agent.y, 3)

    def test_move_agent_up_left(self):
        ui.render_field(self.field)
        agent = self.agents[0]
        logic.move_agent(self.field, agent, "up")
        ui.render_field(self.field)
        logic.move_agent(self.field, agent, "left")
        ui.render_field(self.field)
        self.assertEqual(agent.x, 2)
        self.assertEqual(agent.y, 2)
