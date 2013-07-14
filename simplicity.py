#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Greenfeld'
__version__ = "0.3.0"

import json
import string
import sys


def rst_to_json(filename):
    with open(filename) as f:
        text = f.read()

    records = []

    for line in text.splitlines():
        if len(line) and (line[0] in string.ascii_letters or line[0].isdigit()):
            master_key = line
            data = {master_key: {}}
            records.append(
                data
            )
        if len(line) and line[0].startswith(":"):
            index = line.index(":", 1)
            key = line[1:index]
            value = line[index + 1:].strip()
            data[master_key][key] = value

    return json.dumps(records)


def command_line_runner():
    filename = sys.argv[-1]
    if filename.endswith("simplicity"):
        print("ERROR! Please enter a ReStructuredText filename!")
        sys.exit()
    print(rst_to_json(filename))


if __name__ == "__main__":
    output = rst_to_json("sample.rst")
    print(type(output))
    print(output)
