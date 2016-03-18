# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 11:29:48 2016

@author: Joshua
"""

filename = "./example_1.py"

txt = open(filename,"r")

print "Here's your file %r:" % filename
print txt.read()

def print_all(f):
    print f.read()

print_all(txt)

def rewind(f):
    f.seek(0)
rewind(txt)

def print_a_line(line_count, f):
    print line_count, f.readline()
print_a_line(1,txt)