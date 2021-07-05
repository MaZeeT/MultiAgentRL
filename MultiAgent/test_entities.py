from unittest import skip
from unittest import TestCase
from unittest.mock import patch
import entities


class TestAgent(TestCase):

    def setUp(self):
        pass

    def test_starting_position(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)

    @skip("Feature implemented in the logic module, and not directly to the agent entity")
    def test_move_left(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)
        agent.move("left")

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)
        self.assertEqual(agent.position, (test_x, test_y))

    @skip("Feature implemented in the logic module, and not directly to the agent entity")
    def test_move_right(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)
        agent.move("right")

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)
        self.assertEqual(agent.position, (test_x, test_y))

    @skip("Feature implemented in the logic module, and not directly to the agent entity")
    def test_move_up(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)
        agent.move("up")

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)
        self.assertEqual(agent.position, (test_x, test_y))

    @skip("Feature implemented in the logic module, and not directly to the agent entity")
    def test_move_down(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)
        agent.move("down")

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)
        self.assertEqual(agent.position, (test_x, test_y))

    @skip("Feature implemented in the logic module, and not directly to the agent entity")
    def test_move_left_down(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)
        agent.move("left")
        agent.move("down")

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)
        self.assertEqual(agent.position, (test_x, test_y))
