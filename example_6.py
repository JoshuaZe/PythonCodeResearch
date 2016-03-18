# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:27:30 2016

@author: Joshua
"""

import ex6
sentence = "All good things come to those who wait."
words = ex6.break_words(sentence)
words

sorted_words = ex6.sort_words(words)
sorted_words

ex6.print_first_word(words)
ex6.print_last_word(words)
words

ex6.print_first_word(sorted_words)
ex6.print_last_word(sorted_words)
sorted_words

sorted_words = ex6.sort_sentence(sentence)
sorted_words

ex6.print_first_and_last(sentence)
ex6.print_first_and_last_sorted(sentence)