#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Greenfeld'
__version__ = "0.5.1"

import json
import string
import sys


def rst_to_json(filename):
    """ I convert RST files with field lists into Dictionaries! """
    with open(filename) as f:
        text = f.read()

    records = []

    for line in text.splitlines():
        if len(line) and (line[0] in string.ascii_letters or line[0].isdigit()):
            data = {"title": line}
            records.append(
                data
            )
        if len(line) and line[0].startswith(":"):
            index = line.index(":", 1)
            key = line[1:index]
            value = line[index + 1:].strip()
            data[key] = type_converter(value)

    return json.dumps(records)


def type_converter(text):
    """ I convert strings into integers, floats, and strings! """
    if text.isdigit():
        return int(text)

    try:
        return float(text)
    except ValueError:
        return text


def command_line_runner():
    """ I run functions from the command-line! """
    filename = sys.argv[-1]
    if filename.endswith("simplicity"):
        print("ERROR! Please enter a ReStructuredText filename!")
        sys.exit()
    print(rst_to_json(filename))


if __name__ == "__main__":
    output = rst_to_json("sample.rst")
    print(type(output))
    print(output)
