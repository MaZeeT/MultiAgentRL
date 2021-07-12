import builtins
from unittest import skip
from unittest import TestCase
from unittest.mock import patch
import entities


class TestEntities(TestCase):
    def test_instantiation_of_wall(self):
        x, y = 2, 3
        entity = entities.Wall(x, y)
        self.assertEqual(x, entity.x)
        self.assertEqual(y, entity.y)

    def test_instantiation_of_agent(self):
        x, y = 6, 1
        entity = entities.Agent(x, y)
        self.assertEqual(x, entity.x)
        self.assertEqual(y, entity.y)

    def test_instantiation_of_empty_space(self):
        x, y = 5, 3
        entity = entities.EmptySpace(x, y)
        self.assertEqual(x, entity.x)
        self.assertEqual(y, entity.y)

    def test_instantiation_of_goal(self):
        x, y = -1, 0
        entity = entities.Goal(x, y, "Unused in this test")
        self.assertEqual(x, entity.x)
        self.assertEqual(y, entity.y)

    def test_group_id_of_agent_default(self):
        x, y = 6, 1
        agent = entities.Agent(x, y)
        self.assertEqual(agent.group_id, 0)

    def test_group_id_of_agent_defined(self):
        x, y = 6, 1
        test_id = 4
        agent = entities.Agent(x, y, group_id=test_id)
        self.assertEqual(agent.group_id, test_id)

    def test_activation_of_goal_False(self):
        x, y = 11, 0
        entity = entities.Goal(x, y, 5)
        self.assertFalse(entity.activated)

        entity.activate(4)
        self.assertFalse(entity.activated)

    def test_activation_of_goal_True(self):
        x, y = 11, 0
        activation = 3
        entity = entities.Goal(x, y, activation)
        self.assertFalse(entity.activated)

        entity.activate(activation)
        self.assertTrue(entity.activated)

    def test_agent_activate_goal_default_True(self):
        agent = entities.Agent(2, 3)
        goal = entities.Goal(3, 3)

        result = goal.activate(agent.group_id)
        self.assertTrue(result)

    def test_agent_activate_goal_True(self):
        test_group_id = 42
        agent = entities.Agent(2, 3, group_id=test_group_id)
        goal = entities.Goal(3, 3, interactive_with_group_id=test_group_id)

        result = goal.activate(agent.group_id)
        self.assertTrue(result)

    def test_agent_activate_goal_False(self):
        agent = entities.Agent(2, 3, group_id=5)
        goal = entities.Goal(3, 3, interactive_with_group_id=7)

        result = goal.activate(agent.group_id)
        self.assertFalse(result)


class TestAgent(TestCase):

    def setUp(self):
        pass

    def test_starting_position(self):
        test_x, test_y = 2, 22
        agent = entities.Agent(test_x, test_y)

        self.assertEqual(agent.x, test_x)
        self.assertEqual(agent.y, test_y)

    def test_move_left(self):
        agent = entities.Agent(2, 4)
        agent.move("left")

        self.assertEqual(agent.x, 1)
        self.assertEqual(agent.y, 4)

    def test_move_right(self):
        agent = entities.Agent(5, 7)
        agent.move("right")

        self.assertEqual(agent.x, 6)
        self.assertEqual(agent.y, 7)

    def test_move_up(self):
        agent = entities.Agent(7, 8)
        agent.move("up")

        self.assertEqual(agent.x, 7)
        self.assertEqual(agent.y, 7)

    def test_move_down(self):
        agent = entities.Agent(4, 4)
        agent.move("down")

        self.assertEqual(agent.x, 4)
        self.assertEqual(agent.y, 5)

    def test_move_left_down(self):
        agent = entities.Agent(4, 8)
        agent.move("left")
        agent.move("down")

        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 9)

    def test_check_move_up(self):
        agent = entities.Agent(3, 3)
        x, y = agent.check_next_move("up")
        self.assertEqual(x, 3)
        self.assertEqual(y, 2)
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 3)

    def test_check_move_down(self):
        agent = entities.Agent(3, 3)
        x, y = agent.check_next_move("down")
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 3)

    def test_check_move_left(self):
        agent = entities.Agent(3, 3)
        x, y = agent.check_next_move("left")
        self.assertEqual(x, 2)
        self.assertEqual(y, 3)
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 3)

    def test_check_move_right(self):
        agent = entities.Agent(3, 3)
        x, y = agent.check_next_move("right")
        self.assertEqual(x, 4)
        self.assertEqual(y, 3)
        self.assertEqual(agent.x, 3)
        self.assertEqual(agent.y, 3)


class TestInteractiveEntities(TestCase):
    def test_interactive_interface_type_True(self):
        test_entity = entities.Goal(2, 2)

        result = isinstance(test_entity, entities.InteractiveEntity)
        self.assertTrue(result)

    def test_interactive_interface_type_False(self):
        test_entity = entities.Wall(2, 2)

        result = isinstance(test_entity, entities.InteractiveEntity)
        self.assertFalse(result)

    def test_action_between_agent_and_goal_true(self):
        agent = entities.Agent(2, 2)
        goal = entities.Goal(6, 7)

        result = goal.activate(agent.group_id)
        self.assertTrue(result)
