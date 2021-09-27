import numpy as np
from Board import Board
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

def actions(board):
    limit = board.size
    actions_avalaible = []
    for i in range(limit):
        for j in range(limit):
            if (board.table[i][j]==0):
                actions_avalaible.append((i,j))
    return actions_avalaible

def min_max_decision(table):
    best_action = None
    v = -9999999
    value = 0
    for action in actions(table):
        value = min_value(result(table,action,1))
        #print(value, action)
        #print("ssssssssssssssss")
        if (value >v):
            v = value
            best_action = action
    return best_action

def max_value(table):
    request = table.check()
    #print(request,"max")
    if (request != -2):
        return request
    v = -999999
    for action in actions(table):
        v = max(v, min_value(result(table,action,1)))
    return v

def min_value(table):
    request = table.check()
    #print(request,"min")
    if (request != -2):
        return request
    v = 999999
    for action in actions(table):
        v = min(v, max_value(result(table,action,-1)))
    return v

b = Board(3)

print(b.check())
print(b.table)

print(min_max_decision(b))

