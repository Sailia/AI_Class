#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:21:52 2020

@author: syema

Eliza Relationship Advisor
"""
__author__ = "Syema Ailia"

def welcome():
    name = input("Hello, my name is Eliza. What's your name?")
    feeling = input("Nice to meet you, " + name + ". How are you feeling today?")
    process(feeling)
    
def process(feeling):
    if(feeling.find(("/^[j|J]oy[ful|ness]*$/") != -1) or (("/^[h|H]app[y|iness]*$/") != 1)):
        if(relationship(feeling) == True):
            positive_relationship(feeling)
        else:
            explain_positive()
    elif(feeling.find(("/^[s|S]addened*$/") != -1) or ("/^I'm [s|S]addened*$/") != -1):
        if(relationship(feeling) == True):
            negative_relationship(feeling)
        else:
            past_negative(feeling)
    elif(feeling.find("^([o|O][k|K])$") != -1):
        current_neutral()
    elif(feeling.find("/^([b|B]ad/)$") != -1):
        current_negative()
    elif(feeling.find("/^([g|G]ood)$/") != -1):
        current_positive(feeling)
    elif(feeling == "/[b|B]ye/"):
        print("Goodbye!")
    
  
def relationship(talk):
    return (talk.find(("/^[m|M]o[m|ther]*$/") != -1) or 
           (talk.find("/^[d|D]ad*$/") != 1 ) or (talk.find("/^[f|F]ather*$/") != -1) 
           or (talk.find("/^[b|B]rother[s]*$/") != -1) or (talk.find("/^[s|S]ister[s]*$/") != -1) 
           or talk.find("/^[s|S]ister[s]*$/") != -1)
      
def current_positive(good):
    explain = input("Thats great, what was " + good + " about it?")
    process(explain)

     
def current_negative(bad):
    explain = input("I'm sorry. Why do you feel " + bad + " about it?")
    process(explain)

def current_neutral():
    explain = input("Just ok?")
    process(explain)
    
def explain_positive():
    explain = input("Thats wonderful to hear. Can you tell me more?")
    process(explain)
    
def past_negative(feeling):
    explain = input("I'm sorry you were " + feeling + " by it. Can you elaborate?")
    process(explain)


def negative_relationship(experience):
    explain = input("I'm sorry this happened. How did they handle it?")
    process(explain)

def positive_relationship(experience):
    explain = input("I'm so glad. How did they handle it?")
    process(explain)

















