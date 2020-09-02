#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:16:54 2020

@author: syema
"""
import sys

array = sys.argv
count = 1
numbers = []
while(count < len(array)):
    numbers.append(array[count])
    count += 1
    
print(max(numbers, key=numbers.count))