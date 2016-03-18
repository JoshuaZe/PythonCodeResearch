# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:14:57 2016
http://learnpythonthehardway.org/book/ex46.html
http://learnpythonthehardway.org/book/ex47.html
@author: Joshua
"""

# setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)

# tests/NAME_tests.py
from nose.tools import *
import NAME

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"