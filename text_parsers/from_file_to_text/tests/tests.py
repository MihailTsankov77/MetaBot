import unittest

from file_parser import parse_file

class FileToTextParser(unittest.TestCase):

    def test_file_to_text_base(self):
        
        parse_file('text_parsers/from_file_to_text/TestObject.py')

