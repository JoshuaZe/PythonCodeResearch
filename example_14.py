# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:55:06 2016
http://learnpythonthehardway.org/book/ex44.html
@author: Joshua
"""

# Inheritance Versus Composition
# Implicit Inheritance
# Override Explicitly
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
    def override(self):
        print "PARENT override()"
    def altered(self):
        print "PARENT altered()"
class Child(Parent):
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.override()
son.override()

# Composition
class Other(object):
    def __init__(self):
        self.parent = Parent()

    def implicit(self):
        self.parent.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.parent.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()
