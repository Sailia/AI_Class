#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:24:47 2020

@author: syema
"""

def read_file():
    f = open("test.txt", "r")
    r = f.readlines()
    # split_comma = r.split(",")
    print(r)
    f.close()
    

if __name__ == "__main__":
    read_file()