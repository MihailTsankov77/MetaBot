from commands_string_builder import _get_params_string, build_commands_string
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class CommandsTests(unittest.TestCase):
    def test_get_params_string_1(self):
        self.assertEqual(_get_params_string(('x', 'y')), '(x, y)')

    def test_get_params_string_2(self):
        self.assertEqual(_get_params_string(('x', '')), '(x)')

    def test_get_params_string_3(self):
        self.assertEqual(_get_params_string(('x', 'y', '')), '(x, y)')

    def test_get_params_string_4(self):
        self.assertEqual(_get_params_string(('x', None, 'z')), '(x, z)')

    def test_get_params_string_5(self):
        self.assertEqual(_get_params_string(('')), '()')

    def test_get_params_string_6(self):
        self.assertEqual(_get_params_string(('x', 'y', 'z')), '(x, y, z)')

    def test_build_commands_string_1(self):
        self.assertEqual(build_commands_string(
            [('mat2', 'x', 'y'), ('mat3', 'z')], 'player', -1), 'player.mat2(x, y)\nplayer.mat3(z)')

    def test_build_commands_string_2(self):
        self.assertEqual(build_commands_string(
            [('mat2', 'x', 'y'), ('mat3', 'z')], 'player', 0), '<font color=#00FF00>player.mat2(x, y)</font>\nplayer.mat3(z)')

    def test_build_commands_string_3(self):
        self.assertEqual(build_commands_string([('mat2', 'x', 'y'), ('mat3', 'z')], 'player', 1),
                         '<font color=#FF0000>player.mat2(x, y)</font>\n<font color=#00FF00>player.mat3(z)</font>')
