from unittest import TestCase
from unittest.mock import patch

from multi_control.envs import human_input


class TestInput(TestCase):
    method_patch = 'multi_control.envs.human_input.get_input'

    @patch(method_patch, return_value="w")
    def test_answer_w(self, input):
        result = human_input.get_direction()
        expect = 0
        self.assertEqual(result, expect)

    @patch(method_patch, return_value="a")
    def test_answer_a(self, input):
        result = human_input.get_direction()
        expect = 1
        self.assertEqual(result, expect)

    @patch(method_patch, return_value="s")
    def test_answer_s(self, input):
        result = human_input.get_direction()
        expect = 2
        self.assertEqual(result, expect)

    @patch(method_patch, return_value="d")
    def test_answer_d(self, input):
        result = human_input.get_direction()
        expect = 3
        self.assertEqual(result, expect)

    @patch(method_patch, return_value=" ")
    def test_answer_action(self, input):
        result = human_input.get_direction()
        expect = 4
        self.assertEqual(result, expect)


class Test_Render(TestCase):
    pass
