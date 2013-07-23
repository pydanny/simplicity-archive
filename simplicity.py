#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Greenfeld'
__version__ = "0.6.0"

import json
import string
import sys

# Python 3 compatibility 
P3K = sys.version > '3'
STRING_TYPE = str if P3K else unicode


def file_opener(filename):
    """ I'm basically a context manager for opening files! """
    with open(filename) as f:
        text = f.read()
    return text


def rst_to_json(text):
    """ I convert Restructured Text with field lists into Dictionaries! """
    records = []
    last_type = None

    for line in text.splitlines():
        # set the title
        if len(line) and (line[0] in string.ascii_letters or line[0].isdigit()):
            data = {"title": line}
            records.append(
                data
            )
            continue

        # Grab standard text fields
        if len(line) and line[0].startswith(":"):
            index = line.index(":", 1)
            key = line[1:index]
            value = line[index + 1:].strip()
            data[key], last_type = type_converter(value)
            continue

        # Work on multi-line strings
        if len(line) and line[0].startswith(" "):
            if not isinstance(data[key], str):
                # Not a string so continue on
                continue
            value = line.strip()
            if not len(value):
                # empty string, continue on
                continue
            # add next line
            data[key] += "\n{}".format(value)

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
    output = rst_to_json("sample.rst")
    print(type(output))
    print(output)
