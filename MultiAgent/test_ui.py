from unittest import TestCase
from unittest.mock import patch
from MultiAgent.ui import UserInterface


class TestInput(TestCase):
    method_patch = 'MultiAgent.ui.UserInterface.get_input'

    def setUp(self):
        self.ui = UserInterface()

    @patch(method_patch, return_value="w")
    def test_answer_w(self, input):
        self.assertEqual(self.ui.get_direction(), 0)

    @patch(method_patch, return_value="a")
    def test_answer_a(self, input):
        self.assertEqual(self.ui.get_direction(), 1)

    @patch(method_patch, return_value="s")
    def test_answer_s(self, input):
        self.assertEqual(self.ui.get_direction(), 2)

    @patch(method_patch, return_value="d")
    def test_answer_d(self, input):
        self.assertEqual(self.ui.get_direction(), 3)

    @patch(method_patch, return_value=" ")
    def test_answer_action(self, input):
        self.assertEqual(self.ui.get_direction(), 4)


class Test_Render(TestCase):
    pass
