from unittest import TestCase
from unittest.mock import patch

from multi_agent_environments.envs import entities, envtest_two_agent


class TestEntitySet(TestCase):
    def setUp(self):
        self.agent = entities.Agent(2, 2)
        self.raw_entity_set = [
            entities.Goal(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), entities.Wall(1, 1), entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), self.agent, entities.Goal(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
        ]
        self.entity_set = entities.EntitySet(self.raw_entity_set)

    def test_max_x(self):
        result = self.entity_set.x_max
        expect = 3
        self.assertEqual(expect, result)

    def test_max_y(self):
        result = self.entity_set.y_max
        expect = 3
        self.assertEqual(expect, result)

    def test_min_x(self):
        result = self.entity_set.x_min
        expect = 0
        self.assertEqual(expect, result)

    def test_min_y(self):
        result = self.entity_set.y_min
        expect = 0
        self.assertEqual(expect, result)

    def test_get_raw_set(self):
        result = self.entity_set.get_raw_set()
        expect = self.raw_entity_set
        self.assertEqual(expect, result)

    def test_get_entity_by_correct_position(self):
        x, y = 2, 3
        entity_set = entities.EntitySet([entities.Wall(x, y)])
        entity = entity_set.get_entity_by_position(x, y)
        self.assertIsNotNone(entity)
        self.assertEqual(x, entity.x)
        self.assertEqual(y, entity.y)

    def test_get_entity_by_wrong_position(self):
        x, y = 8, 2
        entity_set = entities.EntitySet([entities.Wall(x, y)])
        entity = entity_set.get_entity_by_position(2, 1)
        self.assertIsNone(entity)

    def test_is_occupied_false(self):
        entity_set = entities.EntitySet([
            entities.Agent(3, 3),
            entities.Wall(0, 0)
        ])
        position = 5, 9
        result = entity_set.is_occupied(position)
        self.assertFalse(result)

    def test_is_occupied_true(self):
        entity_set = entities.EntitySet([
            entities.Agent(3, 3),
            entities.Wall(0, 0)
        ])
        position = 3, 3
        result = entity_set.is_occupied(position)
        self.assertTrue(result)

    def test_count_total_goals(self):
        result = self.entity_set.count_goals(only_activated=False)
        expect = 4
        self.assertEqual(result, expect)

    def test_count_activated_goals(self):
        self.entity_set.interact_with_surroundings(self.agent)

        result = self.entity_set.count_goals(only_activated=True)
        expect = 2
        self.assertEqual(result, expect)

    def test_agent_interact_with_two(self):
        agent = entities.Agent(1, 1)
        entity_set = entities.EntitySet([
            entities.Goal(0, 0), entities.Wall(0, 1), entities.Wall(0, 2),
            entities.Wall(1, 0), agent, entities.Goal(1, 2),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2),
        ])
        result = entity_set.interact_with_surroundings(agent)
        self.assertTrue(result)

    def test_agent_interact_with_non(self):
        agent = entities.Agent(1, 1)
        entity_set = entities.EntitySet([
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2),
            entities.Wall(1, 0), agent, entities.Wall(1, 2),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2),
        ])
        result = entity_set.interact_with_surroundings(agent)
        self.assertFalse(result)

    def test_agent_interact_with_non_nearby(self):
        agent = entities.Agent(1, 1)
        entity_set = entities.EntitySet([
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), agent, entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2), entities.Goal(2, 3),
        ])
        result = entity_set.interact_with_surroundings(agent)
        self.assertFalse(result)

    def test_agent_interact_with_one_nearby(self):
        result = self.entity_set.interact_with_surroundings(self.agent)
        self.assertTrue(result)

    def test_count_activated_entities(self):
        self.entity_set.interact_with_surroundings(self.agent)
        result = self.entity_set.count_goals(only_activated=True)
        expect = 2
        self.assertEqual(result, expect)


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
        entity = entities.Goal(x, y, interactive_with_group_id=5)
        agent = entities.Agent(x, y+1, group_id=3)
        self.assertFalse(entity.activated)

        entity.activate(agent)
        self.assertFalse(entity.activated)

    def test_activation_of_goal_True(self):
        x, y = 11, 0
        entity = entities.Goal(x, y, interactive_with_group_id=4)
        agent = entities.Agent(x, y+1, group_id=4)
        self.assertFalse(entity.activated)

        entity.activate(agent)
        self.assertTrue(entity.activated)

    def test_agent_activate_goal_default_True(self):
        agent = entities.Agent(2, 3)
        goal = entities.Goal(3, 3)

        result = goal.activate(agent)
        self.assertTrue(result)

    def test_agent_activate_goal_True(self):
        test_group_id = 42
        agent = entities.Agent(2, 3, group_id=test_group_id)
        goal = entities.Goal(3, 3, interactive_with_group_id=test_group_id)

        result = goal.activate(agent)
        self.assertTrue(result)

    def test_agent_activate_goal_False(self):
        agent = entities.Agent(2, 3, group_id=5)
        goal = entities.Goal(3, 3, interactive_with_group_id=7)

        result = goal.activate(agent)
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

        result = goal.activate(agent)
        self.assertTrue(result)
