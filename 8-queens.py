#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:46:49 2020

@author: syema
"""
import random
import sys
__author__ = "Syema Ailia"

def runner():
    boards_to_create = enter_boards()
    generated_boards = generate_boards(boards_to_create)
    generated_boards.append([2,4,6,8,3,1,7,5])
    runs = 0
    solved = 0
    for board in generated_boards:
        result = hillClimbing(board)
        runs += result[0]
        solved += result[1]
    print("Hill climbing board solved: " + str(solved/boards_to_create))
    print("Cost: " + str(runs/boards_to_create))
    print(generated_boards) 
    
def enter_boards():
    return int(sys.argv[1])
    
def generate_boards(boards):
    countdown = int(boards)
    board = []
    appended_boards = []
    while countdown != 0:
        board = []
        for num in range(9):
            board.append(random.randrange(1, 9))
        appended_boards.append(board)
        countdown = countdown - 1
    return appended_boards
        
def hillClimbing(board):
    # number of boards created 
    # was problem solved? (heuristic == 0)
    solution = 0
    iterations = 0
    current = board
    all_successors = successors(current)
    while True:
        iterations += 1
        neighbour = highest_value_successor(all_successors)
        if (evaluate_heuristic(neighbour) >= evaluate_heuristic(current)):
            if(evaluate_heuristic(current) < 1):
                solution = 1
            return (iterations, solution, current)
        current = neighbour
        all_successors = successors(current)
    
    
def successors(board):
    successors = []
    for i in range(len(board)):
        for j in range(1, len(board)):
            update = board.copy()
            update[i] = j
            if(update not in successors):
                successors.append(update)
    return successors  
        
def highest_value_successor(all_successors):
    # get all successors
    
    # find the successor with the minimum heuristic
    minimum = evaluate_heuristic(all_successors[0])
    minimum_successor = all_successors[0]
    for successor in all_successors:
        if(evaluate_heuristic(successor) < minimum):
            minimum = evaluate_heuristic(successor)
            # also keep track of the successor that resulted in the minimum
            minimum_successor = successor
    # return the minimum successor
    return minimum_successor

def evaluate_heuristic(board):
    attacking_queens = 0
    count = 0
    for queen in board:
        count_other = count+1
        for other_queen in board[count + 1:]:
            #get the distance between queen and the next
            queen_distance = abs(count - count_other) 
            # get the distance between the rows of the two queens I'm comparing
            row_distance = abs(queen - other_queen)
            # if row distance equals 0 then increase the attack by one
            if(row_distance == 0):
                attacking_queens += 1
            #if the queen distance equals to row distance then attacking queens increments by one (count, other_count)
            elif(queen_distance == row_distance):
                attacking_queens += 1
            count_other += 1
        count += 1
    return attacking_queens       

if(__name__ == "__main__"):
   # enter_boards()
   b = [1,1,8,5,4,7,2,6]
   print(runner())
   b = [4,3,2,5,4,3,2,3]
   print(evaluate_heuristic(b))
   print(evaluate_heuristic(highest_value_successor(successors(b))))
   
   
   
   
   