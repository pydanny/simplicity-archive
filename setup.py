#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os
import sys

import simplicity


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (
            simplicity.__version__, simplicity.__version__))
    print("  git push --tags")
    sys.exit()

LONG_DESCRIPTION = open('README.rst').read()
HISTORY = open('HISTORY.rst').read()

setup(
    name='simplicity',
    version=simplicity.__version__,
    description="Converts ReStructuredText into JSON",
    long_description=LONG_DESCRIPTION + '\n\n' + HISTORY,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup"
    ],
    keywords='python,json',
    author=simplicity.__author__,
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/simplicity',
    license='MIT',
    py_modules=['simplicity', ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'simplicity=simplicity:command_line_runner',
        ]
    },
)

# (*) Please direct queries to Github issue list, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
