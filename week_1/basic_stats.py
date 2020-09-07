#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:58:47 2020

@author: syema
"""

def avg(numbers):
    return (sum(numbers) / len(numbers))


def l_sqr(numbers):
    squared = []
    for number in numbers: squared.append(powered(number))
    return squared

def powered(num):
    return pow(num, 2)

"""
–avg: takes a list of numbers as a parameter and returns the average.
–l_sqr: takes a list of numbers as a parameter and returns a list with the 
corresponding values squared.
–var: takes a list of numbers X and computes

(∑x∈X(x−μ)^2) / n 

where μ is the average of the numbers in X and n is the number of elements of X.

"""
def var(x):
    n = len(x)
    average = avg(x)
    total = 0
    averaged_squares = []
    
    for l in x:
        averaged_squares.append(pow((l - average), 2))
    
    total = sum(averaged_squares)
        
        
    return total / n