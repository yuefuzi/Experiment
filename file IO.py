# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:14:29 2016

@author: Chang
"""
import collections
population_dict = collections.defaultdict(int)


with open('/Users/Chang/Thinkful/lecz/lecz-urban.csv','rU') as inputFile:
    header = next(inputFile) 

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
   #         print("{0} {1} {2}".format(line[0], line[5], type(line[5])))
             population_dict[line[0]] += line[5]
             
with open('national_population.csv','w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k,v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
#/Users/Chang/Thinkful/lecz/lecz-urban.csv
    