from typing import Counter
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

def evaluate(state):
    countX = state.count_pieces_alienated(-1,1)
    countO = state.count_pieces_alienated(1,-1)
    return countX - countO

max_depth = 6
#7-> 543.81
def cut_off(state, depth):
    return depth == max_depth

def min_max_prunning_cut_off(table, turn,difficulty):
    global max_depth
    global counter
    if (difficulty==1):
        max_depth = 4
    elif (difficulty==2):
        max_depth = 4
    elif (difficulty==3):
        max_depth = 3
    
    val = 0
    s_act = None
    actions = get_actions(table)
    variables_search = {"alpha":-999999, "beta":999999}
    v = 999999
    sigmov = max_value
    sigb = lambda x,y:x < y
    if turn == 1:
        sigmov = min_value
        sigb = lambda x,y:x > y
        v = -999999

    for index in actions:
        counter += 1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        val = sigmov(result(table,action,turn),next_actions,variables_search, change_turn(turn),0)
        table.clear_square(action)
        if (sigb(val,v)):
            v = val
            s_act = action
    return s_act, counter
def min_value(table, actions, variables_search,turn, depth):
    if (cut_off(table,depth) or len(actions)<=0): 
        return evaluate(table)
    v = 999999
    for index in actions:
        global counter
        counter += 1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        v = min(v, max_value(result(table,action,turn),next_actions,variables_search, change_turn(turn),depth+1))
        table.clear_square(action)
        if (v < variables_search["alpha"]):
            return v
        variables_search["beta"] = min(variables_search["beta"],v)
    return v

def max_value(table,actions,variables_search,turn,depth):
    if (cut_off(table,depth) or len(actions)<=0): 
        return evaluate(table)
    v = -999999
    for index in actions:
        global counter
        counter += 1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        
        v = max(v, min_value(result(table,action,turn),next_actions,variables_search, change_turn(turn),depth+1))
        table.clear_square(action)
        if (v > variables_search["beta"]):
            return v
        variables_search["alpha"] = max(variables_search["alpha"],v)
    return v

b = Board(3)
'''
b.table[0] = [-1,-1,-1,-1,1]
b.table[1] = [1,-1,1,1,0]
b.table[2] = [-1,-1,-1,-1,0]
b.table[3] = [1,-1,1,1,0]
b.table[4] = [-1,-1,-1,-1,0]
'''
#b.table[0][0]=-1
#b.table[2][0]=1
#b.table[2][1]=-1
#b.table[1][1]=1
#b.table[0][2]=-1
#3x3 tiempo: 0.06682252883911133
#4x4 tiempo: 442.15812063217163
'''
b = Board(3)
b.table[0][0]=-1
b.table[0][1]=1
b.table[0][2]=-1
b.table[1][0]=1
b.table[1][1]=-1
b.table[1][2]=-1
b.table[2][0]=1
b.table[2][1]=-1
b.table[2][2]=0
print(b.check())
print(b.table)
init = time.time()
print(min_max_prunning_cut_off(b,1,1))

end = time.time()
print(f"tiempo: {end-init}")

##aumentar turnos

'''
