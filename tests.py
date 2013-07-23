#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import unittest

from simplicity import rst_to_json

# Python 3 compatibility 
P3K = sys.version > '3'
STRING_TYPE = str if P3K else unicode

MULTILINE_STRING_TEST = """Build software better, together.

Runs with git or svn"""




class FileOpener(unittest.TestCase):
    pass

class Rst2Json(unittest.TestCase):
    
    def setUp(self):
        with open('sample.rst') as f:
            text = rst_to_json(f.read())
        self.data = json.loads(text)

    def test_integer(self):
        """ I test integers by looking at the age of Python! """
        self.assertTrue(isinstance(self.data[0]['age'], int))

    def test_float(self):
        """ I test floats by looking at how much it costs to download Python! """
        self.assertTrue(isinstance(self.data[0]['price'], float))

    def test_string(self):
        """ I test strings by looking at Python's mascot! """
        self.assertTrue(isinstance(self.data[0]['mascot'], STRING_TYPE))
        
    def test_multiline_string(self):
        self.assertEquals(self.data[2]['description'], MULTILINE_STRING_TEST)
        

if __name__ == '__main__':
    unittest.main()


