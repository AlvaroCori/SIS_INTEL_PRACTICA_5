from typing import Counter
import numpy as np
import copy as cp
from Board import Board
import time
from heucaristic_best_worse import *
counter = 0
difficulty_board = 3
def next_state(table, action):
    row , col = action
    table.table[row][col] = table.turn    
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



max_depth = 6
#7-> 543.81
def cut_off(state):
    return state.depth == max_depth

def thanatos(table, turn):
    global max_depth
    global counter
    counter = 0
    table.turn = turn
    if (table.size <= 3):
        max_depth = 9
    elif (table.size == 4):
        max_depth = 5
    elif (table.size >= 5):
        max_depth = 3
    
    value = 0
    best_action = None
    actions = get_actions(table)
    variables_search = {"alpha":-999999, "beta":999999}
    v = 999999
    sigmov = max_value
    sigb = lambda x,y:x < y
    if turn == 1:
        sigmov = min_value
        sigb = lambda x,y:x > y
        v = -999999
    table.depth = 0
    for index in actions:
        counter += 1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        table.depth += 1 
        value = sigmov(next_state(table,action),next_actions,variables_search)
        if (sigb(value,v)):
            v = value
            best_action = action
        table.depth -= 1 
        table.clear_square(action)
        table.change_turn()
    return best_action, counter


def min_value(table, actions, variables_search):
    table.change_turn()
    if (cut_off(table) or table.check()!=-2): 
        return evaluate(table)
    
    v = 999999
    for index in actions:
        global counter
        counter += 1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        table.depth += 1
        v = min(v, max_value(next_state(table,action),next_actions,variables_search))
        table.clear_square(action)
        table.depth -= 1
        table.change_turn()
        if (v < variables_search["alpha"]):
            return v
        variables_search["beta"] = min(variables_search["beta"],v)
    return v

def max_value(table,actions,variables_search):
    table.change_turn()
    if (cut_off(table) or table.check()!=-2): 
        return evaluate(table)
    v = -999999
    for index in actions:
        global counter
        counter += 1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        table.depth += 1
        v = max(v, min_value(next_state(table,action),next_actions,variables_search))
        table.clear_square(action)
        table.depth -= 1
        table.change_turn()
        if (v > variables_search["beta"]):
            return v
        variables_search["alpha"] = max(variables_search["alpha"],v)
    return v


def evaluate(state):
    request = state.check()
    if (request == 1):
        return 100*(max_depth+1-state.depth)
    if (request == -1):
        return -100*(max_depth+1-state.depth)
    if (request == -2):
        first_i = 0
        first_j = 0
        take_first = False
        for i in range(state.size):
            for j in range(state.size):
                if (state.table[i][j] == 0):
                    request = 10
                    if (take_first == False):
                        first_i = i
                        first_j = j
                        take_first = True
                    if (i!=0 and i!=state.size-1 and j!=0 and j!=state.size-1):
                        return 20 * state.count_cross_pieces(i,j)
        if (request == 10):
            request += state.count_cross_pieces(first_i,first_j)
        return request * state.turn
    return request

'''
b = Board(3)
b.table[0][0] = -1
b.table[1][1] = 1
b.table[2][2] = -1
b.table[1][2] = 1
b.table[1][0] = -1
b.table[2][0] = 1
b.table[0][2] = -1
init = time.time()
print(thanatos(b,1))
end = time.time()
print(b.table)
print(b.check())
print(f"tiempo: {end-init}")
'''
'''
from Min_Max import min_max_decision
init = time.time()
print(min_max_decision(b,-1))
end = time.time()
print(b.table)
print(b.check())
print(f"tiempo: {end-init}")
'''
from best_worse import *

b = Board(3)
b.table[0][0] = -1
b.table[1][0] = 1
print(thanatos(b,-1))

#print(move(b,1))

