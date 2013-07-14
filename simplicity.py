#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Greenfeld'
__version__ = "0.2.0"

import json
import string
import sys

filename = sys.argv[-1]


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
            value = line[index+1:].strip()
            data[master_key][key] = value

    return json.dumps(records)


if __name__=="__main__":
    output = rst_to_json(filename)
    print(type(output))
    print(output)