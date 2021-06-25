from unittest import TestCase
from unittest.mock import patch
import entities


class Test_Agent(TestCase):

    def setUp(self):
        pass

    def test_starting_position(self):
        test_x = 2
        test_y = 22
        agent = entities.Agent(test_x, test_y)

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)

    def test_move_left(self):
        agent = entities.Agent(2, 22)
        agent.move("left")

        self.assertEqual(agent.x, 1)
        self.assertEqual(agent.y, 22)

    def test_move_right(self):
        agent = entities.Agent(2, 22)
        agent.move("right")

        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 22)

    def test_move_up(self):
        agent = entities.Agent(2, 22)
        agent.move("up")

        self.assertEqual(agent.x, 2)
        self.assertEqual(agent.y, 21)

    def test_move_down(self):
        agent = entities.Agent(2, 22)
        agent.move("down")

        self.assertEqual(agent.x, 2)
        self.assertEqual(agent.y, 23)

    def test_move_left_down(self):
        agent = entities.Agent(2, 22)
        agent.move("left")
        agent.move("down")

        self.assertEqual(agent.x, 1)
        self.assertEqual(agent.y, 23)
