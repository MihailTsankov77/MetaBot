import unittest
import os   
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from text_parser import _check_has_code_classes, _check_has_code_privates, _check_code_for_bs, _check_code_for_imports, to_code

class TextToCodeParser(unittest.TestCase):
        def test_find_class(self):
            self.assertTrue(_check_has_code_classes('class TestClass:'))
            self.assertTrue(_check_has_code_classes('class TestClass():'))
            self.assertTrue(_check_has_code_classes('class TestClass(object):'))
            self.assertTrue(_check_has_code_classes('class Test   :'))
        
        def test_find_class_negative(self):
            self.assertFalse(_check_has_code_classes('dsa TestClass():'))
            self.assertFalse(_check_has_code_classes('claaass TestClass(object):'))
        
        def test_check_has_code_privates_1(self):
            self.assertTrue(_check_has_code_privates('da._dsa'))

        def test_check_has_code_privates_2(self):
            self.assertFalse(_check_has_code_privates('da.dsa'))
        
        def test_check_has_code_privates_3(self):
            self.assertFalse(_check_has_code_privates('da.dsa_'))
        
        def test_check_has_code_privates_4(self):
            self.assertTrue(_check_has_code_privates('da._dsa_'))
        
        def test_check_has_code_privates_5(self):
            self.assertTrue(_check_has_code_privates('a.__dsa'))

        def test_check_has_code_privates_6(self):
            self.assertTrue(_check_has_code_privates('s.__dsa__'))
        
        def test_check_code_for_bs_1(self):
            self.assertTrue(_check_code_for_bs('globals()'))
        
        def test_check_code_for_bs_2(self):
            self.assertTrue(_check_code_for_bs('locals()'))
        
        def test_check_code_for_bs_3(self):
            self.assertTrue(_check_code_for_bs('fork()'))
        
        def test_check_code_for_bs_4(self):
            self.assertTrue(_check_code_for_bs('exec()'))
        
        def test_check_code_for_bs_5(self):
            self.assertTrue(_check_code_for_bs('__dict__'))
        
        def test_check_code_for_bs_6(self):
            self.assertFalse(_check_code_for_bs('start()'))

        def test_check_code_for_imports_1(self):
            self.assertTrue(_check_code_for_imports('import os'))
        
        def test_check_code_for_imports_2(self):
            self.assertTrue(_check_code_for_imports('from os import sda'))

        def test_check_code_for_imports_3(self):
            self.assertTrue(_check_code_for_imports('import os as sda'))

        def test_to_code_1(self):
             with self.assertRaises(Exception):
                to_code('import a', {})

        def test_to_code_2(self):
            class Pl:
                def __init__(self):
                    self.x = 1

                def move(self):
                    self.x = 1

            class Test:
                def __init__(self):
                    self.bob = Pl()

                def test(self):
                    text = """
def m():
    ror.x = 3

ror.move = m
            """
                    to_code(text, {'ror': self.bob})

            test = Test()
            test.test()

            self.assertEqual(test.bob.x, 1)
            test.bob.move()
            self.assertEqual(test.bob.x, 3)
