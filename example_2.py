# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 11:29:48 2016

@author: Joshua
"""

filename = "C:/Users/Joshua/Documents/Python Scripts/example_1.py"

txt = open(filename,"r")

print "Here's your file %r:" % filename
print txt.read()
