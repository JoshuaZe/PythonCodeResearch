# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:09:41 2016
http://learnpythonthehardway.org/book/ex40.html
http://learnpythonthehardway.org/book/ex41.html
@author: Joshua
"""

mystuff = {'apple': "I AM APPLES!"}
mystuff['apples']

# Modules Are Like Dictionaries
import module11
module11.apple()
print module11.tangerine
module11.banana()
#Classes Are Like Modules
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLES!"
thing = MyStuff()
thing.apple()
thing.tangerine

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()