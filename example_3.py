# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 11:32:18 2016

@author: Joshua
"""

filename = "C:/Users/Joshua/Documents/Python Scripts/tmp.txt"
target = open(filename, 'a')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()