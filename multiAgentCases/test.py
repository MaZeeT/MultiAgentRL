import unittest
import entities as entities


class TestEntities(unittest.TestCase):

    def test_agent_move_down(self):
        direction = "down"
        agent = entities.Agent(2, 2)
        start_x = agent.x
        start_y = agent.y

        agent.move(direction)

        end_x = agent.x
        end_y = agent.y

        self.assertNotEqual(start_x, end_x)
        self.assertEqual(start_y, end_y)

    def test_agent_move_left(self):
        direction = "left"
        agent = entities.Agent(2, 2)
        start_x = agent.x
        start_y = agent.y

        agent.move(direction)

        end_x = agent.x
        end_y = agent.y

        self.assertEqual(start_x, end_x)
        self.assertNotEqual(start_y, end_y)