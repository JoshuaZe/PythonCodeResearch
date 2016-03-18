# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 11:40:47 2016

@author: Joshua
"""

# something like argv
# That * tells Python to take all the arguments to 
# the function and then put them in args as a list

def print_two_A(*args):
    #arg1,arg2=args
    print "arg1: %r, arg2: %r" % (args)
def print_two_B(*args):
    arg1,arg2=args
    print "arg1: %r, arg2: %r" % (arg1,arg2)
def print_two_C(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

print_two_A("hi","good")

