import numpy as np
import copy as cp
from Board import Board
import time
counter = 0

def result(table, action,turn):
    row , col = action
    table.table[row][col] = turn    
    return table
def utility(value):
    if (value == -1):
        print("Empate")
    if (value == 1):
        print("Han ganado las X")
    if (value == 0):
        print("Han ganado las O")
        
def change_turn(turn):
    if turn == 1:
        turn = -1
    else:
        turn = 1
    return turn

def get_actions(board):
    limit = board.size
    actions_avalaible = dict()
    index = 0
    for i in range(limit):
        for j in range(limit):
            if (board.table[i][j]==0):
                actions_avalaible[index] = (i,j)
                index += 1
    return actions_avalaible

def min_max_decision(table, turn):
    global counter
    counter = 0
    best_action = None
    actions = get_actions(table)
    sigmov = max_value
    sigb = lambda x,y:x < y
    v = 9999999
    if turn == 1:
        sigmov = min_value
        sigb = lambda x,y:x > y
        v = -9999999
    value = 0
    for index in actions:
        counter +=1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        value = sigmov(result(table,action,turn),next_actions,change_turn(turn))
        if (sigb(value,v)):
            v = value
            best_action = action
        table.clear_square(action)
    return best_action, counter

def max_value(table, actions, turn):
    request = table.check()
    if (request != -2):
        return request
    v = -999999
    for index in actions:
        global counter
        counter +=1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        v = max(v, min_value(result(table,action,turn),next_actions,change_turn(turn)))
        table.clear_square(action)
    return v

def min_value(table, actions ,turn):
    request = table.check()
    if (request != -2):
        return request
    v = 999999
    for index in actions:
        global counter
        counter +=1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        v = min(v, max_value(result(table,action,turn),next_actions,change_turn(turn)))
        table.clear_square(action)

    return v

