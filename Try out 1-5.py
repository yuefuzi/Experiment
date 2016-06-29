# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:06:21 2016

@author: Chang
"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i




