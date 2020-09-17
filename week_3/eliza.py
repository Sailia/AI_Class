#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:21:52 2020

@author: syema

Eliza Relationship Advisor
"""
import re
import random
__author__ = "Syema Ailia"

def welcome():
    name = input("Hello, my name is Eliza. What's your name?\n")
    feeling = input("Nice to meet you, " + name + ". How are you feeling today?\n")
    process(feeling)
    
def process(feeling):
    feeling = re.sub("'", "", feeling)
    if(relationship(feeling) == True): 
        relationship_explain(feeling)
    elif( re.search(r"(\b[j|J]oy)", feeling) is not None or re.search(r"(\b[h|H]app[y|i])", feeling) is not None):
        explain_positive()
    elif(re.search(r"[s|S]ad", feeling) is not None):
        if(re.search("[s|S]ad[?+d|n+$]", feeling) is not None):
            past_negative(feeling)
        else:
            current_negative()
    elif( re.search("[o|O][k|K]", feeling) is not None):
        current_neutral()
    elif(re.search("([n|N]ot sure)", feeling) is not None or re.search("([D|d]ont know)", feeling) is not None):
        assurance()
    elif( re.search("[b|B]ad", feeling) is not None):
        current_negative()
    elif( re.search("[g|G]ood*", feeling) is not None):
        current_positive()
    elif( re.search("[d|D]one*", feeling) is not None):
        done()
    elif( re.search("(end)", feeling) is not None or re.search("(start)", feeling) is not None):
        if(re.search("end(\w*)\s\w", feeling) is not None or re.search("start(\w*)\s\w", feeling) is not None):
            understood()
        else:
            when(feeling)
    elif(feeling == "[b|B]ye"):
         print("Goodbye!")
    else:
        sysrand = random.randint(0,2)
        if(sysrand == 0):
            understood()
        elif(sysrand == 1):
            misunderstood(feeling)
        else:
            lets_talk()


  
def relationship(talk):
    relations = ["[m|M]o[m|ther]", "[d|D]ad", "[f|F]ather", "[b|B]rother[s]", "[s|S]ister[s]", "husband(s)?", "wife[s]"]
    for relation in relations:
        match = re.search(relation, talk)
        if match:
            return True

def done():
    explain = input("How do you feel about it being done?\n")
    process(explain)
    
def current_positive():
    explain = input("Thats great, what was good about it?\n")
    process(explain)
    
def explain_positive():
    explain = input("Awesome, what else happened?\n")
    process(explain)

def current_negative():
    explain = input("I'm sorry. Want to talk about it?\n")
    process(explain)

def current_neutral():
    explain = input("Just ok?\n")
    process(explain)
    
def past_negative(feeling):
    explain = input("I'm sorry you felt this way. Can you elaborate?\n")
    process(explain)

def relationship_explain(experience):
    explain = input("What did they think?\n")
    process(explain)

def when(start_end):
    if(re.search("(start)", start_end) is not None):
        explain = input("When did it start?\n")
    else:
        explain = input("When did it end?\n")
    process(explain)
    
def understood():
    explain = input("I see. How do you feel now that you've talked about it?\n")
    process(explain)
    
def misunderstood(response):
    explain = input(response + "?\n")
    process(explain)

def lets_talk():
    explain = input("Go on...\n")
    process(explain)
    
def assurance():
    explain = input("Thats OK. What else would you like to talk about?\n")
    process(explain)
        
if(__name__ == "__main__"):
    welcome()














