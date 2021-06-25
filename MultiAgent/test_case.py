from unittest import TestCase
from unittest.mock import patch
import case
import entities


class Test_Case(TestCase):

    def setUp(self):
        pass

    def test_int_to_entity_field(self):
        int_array = [
            [1, 0],
            [0, 1],
        ]
        entity_array = case.entity_field(int_array)
        self.assertIsInstance(entity_array[0][0], entities.Wall)
        self.assertIsInstance(entity_array[1][1], entities.Wall)
        self.assertIsInstance(entity_array[1][0], entities.EmptySpace)
        self.assertIsInstance(entity_array[0][1], entities.EmptySpace)