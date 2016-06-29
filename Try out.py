# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:08:10 2016

@author: Chang
"""

print "Hello World!"

list = [0,1]
print list[0]
print list[1]
for i in range(2,100):
    list.append(list[i-1]+list[i-2])
    print list[i]

