from file_parser import _is_private_method, _find_class, _is_property, _is_visible_property, _is_method_visible, _get_method_name, _get_method, parse_file
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class FileToTextParser(unittest.TestCase):
    def test_is_class_1(self):
        self.assertFalse(_find_class('_mat2'))

    def test_is_class_2(self):
        self.assertTrue(_find_class('class TestObject:'))

    def test_is_class_3(self):
        self.assertTrue(_find_class('class TestObject(dsadsa):'))

    def test_is_property_1(self):
        self.assertTrue(_is_property('    x = 0'))

    def test_is_property_2(self):
        self.assertFalse(_is_property('    def mat2():'))

    def test_is_property_3(self):
        self.assertFalse(_is_property('    class TestObject:'))

    def test_is_visible_property_1(self):
        self.assertTrue(_is_visible_property('    x = 0', ['x']))

    def test_is_visible_property_2(self):
        self.assertFalse(_is_visible_property('    x = 0', ['y']))

    def test_is_visible_property_3(self):
        self.assertFalse(_is_visible_property('    x = 0', []))

    def test_is_method_visible_1(self):
        self.assertTrue(_is_method_visible('''
                                            @visible
                                           def mat2(self):''',))

    def test_is_method_visible_2(self):
        self.assertFalse(_is_method_visible('''
                                            @blob
                                            def mat2(self):'''))

    def test_get_method_name_1(self):
        self.assertEqual(_get_method_name('def mat2(self):'), 'mat2')

    def test_get_method_name_2(self):
        self.assertEqual(_get_method_name('def mat2 (self, x):'), 'mat2')

    def test_get_method_name_3(self):
        self.assertEqual(_get_method_name('def     dsads_dsa():'), 'dsads_dsa')

    def test_is_private_method_1(self):
        self.assertTrue(_is_private_method('_mat2'))

    def test_is_private_method_2(self):
        self.assertFalse(_is_private_method('mat2'))

    def test_is_private_method_3(self):
        self.assertTrue(_is_private_method('__mat2'))

    def test_get_method_1(self):
        method = '''def mat2(self):
        print('mat2')
        a = 0'''
        self.assertEqual(_get_method(iter(method.split('\n'))),
                         "def mat2(self):        print('mat2')        a = 0")

    def test_get_method_2(self):
        method = '''def _mat2(self):
        print('mat2')
        a = 0'''
        self.assertEqual(_get_method(iter(method.split(
            '\n'))), "<font color=#FF0000>\ndef _mat2(self):        print('mat2')        a = 0\n</font>")

    def test_get_method_3(self):
        method = '''def mat2(self):
        print('mat2')
        a = 0

        def mat2(self):
        print('mat2')
        a = 0'''
        self.assertEqual(_get_method(iter(method.split('\n'))),
                         "def mat2(self):        print('mat2')        a = 0")

    def test_parse_file_1(self):
        with open('text_parsers/from_file_to_text/tests/TestObject.py', 'r') as file:
            self.assertEqual(parse_file(file, ['x']),
                             '''class Reg:
    x = 0

    def mat2(self):
        print('mat2')
        a = 0
<font color=#FF0000>
    def _mat2(self):
        print('mat2')
        a = 0

</font><font color=#FF0000>
    def __mat2(self):
        print('mat2')
        a = 0

</font>''')
