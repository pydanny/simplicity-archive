#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import unittest

import simplicity

# Python 3 compatibility
P3K = sys.version > '3'
STRING_TYPE = str if P3K else unicode

MULTILINE_STRING_TEST = """A fun programming language.

Used to build simplicity!"""


class Rst2Json(unittest.TestCase):
    """ I test all facets of the Rst2Json function! Cool!"""

    def setUp(self):
        with open('sample.rst') as f:
            text = simplicity.rst_to_json(f.read())
        self.data = json.loads(text)

    def test_number_of_records(self):
        """ I test that the right number of records are created! """
        self.assertEqual(len(self.data), 3)

    def test_types(self):
        """ I test that Simplicity makes a list and each element is a dictionary! """
        self.assertTrue(isinstance(self.data, list))
        self.assertTrue(isinstance(self.data[0], dict))
        self.assertTrue(isinstance(self.data[1], dict))
        self.assertTrue(isinstance(self.data[2], dict))

    def test_titles(self):
        """ I test that each record has it's title element as it's dictionary title!"""
        self.assertEqual(self.data[0]['title'], "Python")
        self.assertEqual(self.data[1]['title'], "Java")
        self.assertEqual(self.data[2]['title'], "GitHub")

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
        self.assertEquals(self.data[0]['description'], MULTILINE_STRING_TEST)
        print self.data


class FileOpener(unittest.TestCase):

    def test_basics(self):
        """ I test that file_opener returns more than just itself!"""
        text = simplicity.file_opener("sample.rst")
        self.assertNotEqual(text, "sample.rst")
        text = simplicity.file_opener("README.rst")
        self.assertNotEqual(text, "README.rst")

    def test_open(self):
        """ I test that file_opener gets things correctly!"""
        with open("sample.rst") as f:
            text = f.read()
        self.assertEqual(text, simplicity.file_opener("sample.rst"))


class TextCleanup(unittest.TestCase):
    pass


class TypeConverter(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
