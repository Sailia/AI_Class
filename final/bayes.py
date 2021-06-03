'''
The goal of this program is to predict whether a student will get good or bad grades based on their attributes. 
These attributes are the column names in the given csv data and are as follows: 

gender 
race/ethnicity 
parental level of education
lunch
test preparation course

The grades are based on the following:

math score 
reading score
writing score

The data is named Student Performance in Exams from the website Kaggle. 
The data can be downloaded here: https://www.kaggle.com/spscientist/students-performance-in-exams
'''
import sys
import csv
import statistics as std
import re

# Globals
above_avg_observations = {'female': 0, 'male': 0, 'group A': 0, 'group B':0, 'group C':0, 'group D': 0, 'group E': 0, "master's degree": 0, "bachelor's degree": 0, "associate's degree": 0, "some college": 0, "high school": 0, "some high school": 0, 'standard': 0, "free/reduced": 0, 'none': 0, 'completed': 0}
below_avg_observations = {'female': 0, 'male': 0, 'group A': 0, 'group B':0, 'group C':0, 'group D': 0, 'group E': 0, "master's degree": 0, "bachelor's degree": 0, "associate's degree": 0, "some college": 0, "high school": 0, "some high school": 0, 'standard': 0, "free/reduced": 0, 'none': 0, 'completed': 0}

above_avg_probabilities = {'female': 0, 'male': 0, 'group A': 0, 'group B':0, 'group C':0, 'group D': 0, 'group E': 0, "master's degree": 0, "bachelor's degree": 0, "associate's degree": 0, "some college": 0, "high school": 0, "some high school": 0, 'standard': 0, "free/reduced": 0, 'none': 0, 'completed': 0}
below_avg_probabilities = {'female': 0, 'male': 0, 'group A': 0, 'group B':0, 'group C':0, 'group D': 0, 'group E': 0, "master's degree": 0, "bachelor's degree": 0, "associate's degree": 0, "some college": 0, "high school": 0, "some high school": 0, 'standard': 0, "free/reduced": 0, 'none': 0, 'completed': 0}

index_selection = {'2': 'female', '3':'male', '4':'group A', '5':'group B', '6':'group C', '7':'group D', '8':'group E', '9':"master's degree", '10':"bachelor's degree", '11':"associate's degree", '12':"some college", '13':"high school", '14':"some high school", '15':'standard', '16':"free/reduced", '17':'none', '18':'completed'}


def user_input_score():
    score = input("Please enter 0 for above average or 1 for below average")
    return score


def user_input(user_choices): 
    
    gender = None
    while (gender is None):
	    _g = input("Enter 2 for female, 3 for male or 'S' to skip")
	    if (_g in ["2", "3", "S"]):
	    	gender = _g

    group = None
    while (group is None):
	    _gr = input("Enter 4 for group A, 5 for group B, 6 for group C, 7 for group D, 8 for group E or 'S' to skip")
	    if (_gr in ["4", "5", "6", "7", "8", "S"]):
	    	group = _gr
    
    parent_ed = None
    while (parent_ed is None):
	    _pe = input("Enter 9 for master's degree, 10 for bachelor's degree, 11 for associate's degree, 12 for some college, 13 for high school, 14 some high school or 'S' to skip")
	    if (_pe in ["9", "10", "11", "12", "13", "14", "S"]):
	    	parent_ed = _pe

    lunch = None
    while (lunch is None):
	    _l = input("Enter 15 for free/reduced lunch, 16 for standard lunch or 'S' to skip")
	    if (_l in ["15", "16", "S"]):
	    	lunch = _l

    test_prep = None
    while (test_prep is None):
	    _tp = input("Enter 17 for no test preparation course, 18 for completed test preparation course or 'S' to skip")
	    if (_tp in ["17", "18", "S"]):
	    	test_prep = _tp


    user_choices.extend([gender, group, parent_ed, lunch, test_prep])
    
    return user_choices


def probability_given_user_input(score, user_choices):   
    probability = None
    convert_number_responses = []
        
    for choice in user_choices:
        if(choice.isnumeric()):
            convert_number_responses.append(index_selection[choice])
    
    if(score == 0):
        for choice in convert_number_responses:
            if probability is None:
                probability = float(above_avg_probabilities[choice])
            else:
                probability *= float(above_avg_probabilities[choice])
    else:
        for choice in convert_number_responses:
            if probability is None:
                probability = float(below_avg_probabilities[choice])
            else:
                probability *= float(below_avg_probabilities[choice])
    return probability


# calculate probability for each occurences of p(x | given above average) by dividing by the average of above average math scores
def calculate_probability_of_above_avg(total_above_average):
    for x in above_avg_observations:
        val = above_avg_observations[x]
        above_avg_probabilities[x] = float(val / total_above_average)


# count all occurences of x given above average
def x_given_above_avg(row, mean_of_math_scores):
    for x in row:
        if(above_average(row, mean_of_math_scores)):
            if(x != 'math score' and x != 'reading score' and x != 'writing score'):
                above_avg_observations[row[x]] += 1


# calculates the percent of above average math scores
def count_above_avg(row, mean_of_math_scores):  
    if(above_average(row, mean_of_math_scores)):
        return 1
    return 0


def calculate_probability_of_below_avg(total_below_average):
    for x in below_avg_observations:
        val = below_avg_observations[x]
        below_avg_probabilities[x] = float(val / total_below_average)


def x_given_below_avg(row, mean_of_math_scores):
    for x in row:
        if(below_average(row, mean_of_math_scores)):
            if(x != 'math score' and x != 'reading score' and x != 'writing score'):
                below_avg_observations[row[x]] += 1 


def count_below_avg(row, mean_of_math_scores):
    if(below_average(row, mean_of_math_scores)):
        return 1
    return 0


# generate math score list for the standard deviation method
def append_math_score(row, score_list):
    math_score = int(row['math score'])
    score_list.append(math_score)
    return score_list


# return standard deviation of math scores
def standard_deviation(scores):
    stan = std.stdev(scores)
    return stan


# Returns true if the row's math score is higher than the average math score
def above_average(row, mean_of_math_scores):
    above = float(row['math score'])
    return above >= mean_of_math_scores


def below_average(row, mean_of_math_scores):
    below = int(row['math score'])
    return below < mean_of_math_scores



def run_bayes():
	with open('StudentsPerformance.csv', 'r') as file:
	    csv_dict = csv.DictReader(file)
	    total_math_scores = 0
	    math_score_list = []
	    avg_prob = 0
	    total_above_average = 0
	    total_below_average = 0
	    score = 0
	    user_choices = []
	    
	    for row in csv_dict:
	        math_score = int(row['math score'])
	        math_score_list = append_math_score(row, math_score_list)
	        total_math_scores += math_score  # get the total math score for calculating the mean
	    
	    mean_of_math_scores = total_math_scores / len(math_score_list) # get the average math score    
	    
	    file.seek(0) # start at the beginning of the csv_dict file
	    next(csv_dict) # and skip the header
	    
	    for row in csv_dict: 
	        total_above_average += count_above_avg(row, mean_of_math_scores)
	        total_below_average += count_below_avg(row, mean_of_math_scores)
	    
	    file.seek(0) # start at the beginning of the csv_dict file
	    next(csv_dict) # and skip the header
	    
	    for row in csv_dict: 
	        x_given_above_avg(row, mean_of_math_scores)   
	        x_given_below_avg(row, mean_of_math_scores)
	        
	calculate_probability_of_above_avg(total_above_average) # calculate probability for each occurences of p(x | given above average) by dividing by the average of above average math scores
	calculate_probability_of_below_avg(total_below_average)

	print("The probability is " + str(probability_given_user_input(int(user_input_score()), user_input(user_choices))))


if(len(sys.argv) > 1 and sys.argv[1] == "-help"):
	print("To find out the probability of a students performance on their math exam, please enter the following information:")

run_bayes();
