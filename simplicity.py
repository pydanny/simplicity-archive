#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Greenfeld'
__version__ = "0.6.3"

import json
import string
import sys

# Python 3 compatibility
P3K = sys.version > '3'
STRING_TYPE = str if P3K else unicode
DIVIDERS = ['~', '=', '-', '+', '_']


def file_opener(filename):
    """ I'm basically a context manager for opening files! """
    with open(filename) as f:
        text = f.read()
    return text


def text_cleanup(data, key, last_type):
    """ I strip extra whitespace off multi-line strings if they are ready to be stripped!"""
    if key in data and last_type == STRING_TYPE:
        data[key] = data[key].strip()
    return data


def rst_to_json(text):
    """ I convert Restructured Text with field lists into Dictionaries!

        TODO: Convert to text node approach.
    """
    records = []
    last_type = None
    key = None
    data = {}
    directive = False

    lines = text.splitlines()
    for index, line in enumerate(lines):

        # check for directives
        if len(line) and line.strip().startswith(".."):
            directive = True
            continue

        # set the title
        if len(line) and (line[0] in string.ascii_letters or line[0].isdigit()):
            directive = False
            try:
                if lines[index + 1][0] not in DIVIDERS:
                    continue
            except IndexError:
                continue
            data = text_cleanup(data, key, last_type)
            data = {"title": line.strip()}
            records.append(
                data
            )
            continue

        # Grab standard fields (int, string, float)
        if len(line) and line[0].startswith(":"):
            data = text_cleanup(data, key, last_type)
            index = line.index(":", 1)
            key = line[1:index]
            value = line[index + 1:].strip()
            data[key], last_type = type_converter(value)
            directive = False
            continue

        # Work on multi-line strings
        if len(line) and line[0].startswith(" ") and directive == False:
            if not isinstance(data[key], str):
                # Not a string so continue on
                continue
            value = line.strip()
            if not len(value):
                # empty string, continue on
                continue
            # add next line
            data[key] += "\n{}".format(value)
            continue

        if last_type == STRING_TYPE and not len(line):
            data[key] += "\n"

    return json.dumps(records)


def type_converter(text):
    """ I convert strings into integers, floats, and strings! """
    if text.isdigit():
        return int(text), int

    try:
        return float(text), float
    except ValueError:
        return text, STRING_TYPE


def command_line_runner():
    """ I run functions from the command-line! """
    filename = sys.argv[-1]
    if not filename.endswith(".rst"):
        print("ERROR! Please enter a ReStructuredText filename!")
        sys.exit()
    print(rst_to_json(file_opener(filename)))

if __name__ == "__main__":
    command_line_runner()
