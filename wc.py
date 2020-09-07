#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:22:41 2020

Create a program that reads a filename from the command line and prints the 
number of unique words, totalnumber of words (not unique), characters 
(including spaces) and lines in that file.  It must be called wc.py and must 
be run like so:python wc.py filenamewherefilenameis the actual name of the 
file to read.As an example, download this sample file: heaalthyeating.txt’.
Then, when your program is run with this file (python wc.py healthyeating.txt), 
the output ofthe program should be in the ballpark of lines:42, unique:429, 
words:819, chars:4878.The numbers may vary a bit, but not a lot.

@author: syema
"""

import sys


file = sys.argv

healthy_eating = open(file[1])

lines = []
line_count = 0
chars = 0
dict_words = {}
words = 0
unique_words = 0

for line in healthy_eating:
    lines.append(line)
    line_count += 1
    chars += len(line)

split = []
    
for line in lines:
    split = split + line.split()

for word in split:
    if word != '\[.*?\]':
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
        words += 1 

for word in dict_words:
    if(dict_words[word] == 1):
        unique_words += 1
  
frequency = {}        
highest = 1
lowest = 10

for key, val in dict_words.items():
    if val > highest:
        highest = val
        frequency["Most Frequency: "] = val
        frequency["Most Frequency Name: "] = key
    elif val < lowest:
        lowest = val
        frequency["Least Frequency: "] = val
        frequency["Least Frequency Name: "] = key

results = {"lines: ": line_count, "unique: ": unique_words, "words: ": words, "characters: ": chars}

print(results)
print(frequency)
  
healthy_eating.close()














