from unittest import TestCase
from unittest.mock import patch
import logic
import case
import entities
import ui


class TestObjectLogic(TestCase):
    def test_is_occupied_false(self):
        entity_set = [
            entities.Agent(3, 3),
            entities.Wall(0, 0)
        ]
        position = 5, 9
        result = logic.is_occupied(entity_set, position)
        self.assertFalse(result)

    def test_is_occupied_true(self):
        entity_set = [
            entities.Agent(3, 3),
            entities.Wall(0, 0)
        ]
        position = 3, 3
        result = logic.is_occupied(entity_set, position)
        self.assertTrue(result)

    def test_move_agent_not_occupied(self):
        entity_set = [
            entities.Wall(0, 0),
            entities.Wall(0, 2),
        ]
        agent = entities.Agent(0, 1)
        entity_set.append(agent)
        result = logic.move_agent_in_list(entity_set, agent, "left")
        self.assertTrue(result)
        self.assertEqual(agent.x, -1)
        self.assertEqual(agent.y, 1)

    def test_move_agent_occupied(self):
        entity_set = [
            entities.Wall(0, 0),
            entities.Wall(0, 2),
        ]
        agent = entities.Agent(0, 1)
        entity_set.append(agent)
        result = logic.move_agent_in_list(entity_set, agent, "down")
        self.assertFalse(result)
        self.assertEqual(agent.x, 0)
        self.assertEqual(agent.y, 1)

    def test_agent_interact_with_two(self):
        agent = entities.Agent(1, 1)
        entity_set = [
            entities.Goal(0, 0), entities.Wall(0, 1), entities.Wall(0, 2),
            entities.Wall(1, 0), agent, entities.Goal(1, 2),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2),
        ]
        result = logic.interact_with_surroundings(agent, entity_set)
        self.assertTrue(result)

    def test_agent_interact_with_non(self):
        agent = entities.Agent(1, 1)
        entity_set = [
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2),
            entities.Wall(1, 0), agent, entities.Wall(1, 2),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2),
        ]
        result = logic.interact_with_surroundings(agent, entity_set)
        self.assertFalse(result)

    def test_agent_interact_with_non_nearby(self):
        agent = entities.Agent(1, 1)
        entity_set = [
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), agent, entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2), entities.Goal(2, 3),
        ]
        result = logic.interact_with_surroundings(agent, entity_set)
        self.assertFalse(result)

    def test_agent_interact_with_one_nearby(self):
        agent = entities.Agent(3, 2)
        entity_set = [
            entities.Wall(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), entities.Wall(1, 1), entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Wall(2, 2), entities.Goal(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), agent, entities.Wall(3, 3),
        ]
        result = logic.interact_with_surroundings(agent, entity_set)
        self.assertTrue(result)

    def test_count_activated_entities(self):
        agent = entities.Agent(2, 2)
        entity_set = [
            entities.Goal(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), entities.Wall(1, 1), entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), agent, entities.Goal(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
        ]
        logic.interact_with_surroundings(agent, entity_set)
        result = logic.count_activated_entities(entity_set)
        expect = 2
        self.assertEqual(result, expect)

    def test_count_total_goals(self):
        entity_set = [
            entities.Goal(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), entities.Wall(1, 1), entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), entities.Goal(2, 2), entities.Goal(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
        ]
        result = logic.count_goals(entity_set, only_activated=False)
        expect = 5
        self.assertEqual(result, expect)

    def test_count_activated_goals(self):
        agent = entities.Agent(2, 2)
        entity_set = [
            entities.Goal(0, 0), entities.Wall(0, 1), entities.Wall(0, 2), entities.Goal(0, 3),
            entities.Wall(1, 0), entities.Wall(1, 1), entities.Wall(1, 2), entities.Goal(1, 3),
            entities.Wall(2, 0), entities.Wall(2, 1), agent, entities.Goal(2, 3),
            entities.Wall(3, 0), entities.Wall(3, 1), entities.Wall(3, 2), entities.Wall(3, 3),
        ]
        logic.interact_with_surroundings(agent, entity_set)
        result = logic.count_goals(entity_set, only_activated=True)
        expect = 2
        self.assertEqual(result, expect)


class TestArrayLogic(TestCase):
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
