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

def Alpha_Beta_Search(table):
    v = -999999
    val = 0
    s_act = None
    for action in actions(table):
        val = min_value(result(table,action,1),-99999,99999)
        if (val>v):
            v = val
            s_act = action
    return s_act
def min_value(table, alpha, beta):
    request = table.check()
    if (request!=-2):
        return request
    v = 99999999
    for action in actions(table):
        v = min(v, max_value(result(table,action,-1),alpha,beta))
        if (v <= alpha):
            return v
        beta = min(beta,v)
    return v

def max_value(table,alpha,beta):
    request = table.check()
    if (request!=-2):
        return request
    v = -99999999
    for action in actions(table):
        v = max(v, min_value(result(table,action,1),alpha,beta))
        if (alpha >= beta):
            return v
        alpha = max(alpha,v)
    return v

b = Board(5)
b.table[0][0] = -1

print(b.check())
print(b.table)

print(Alpha_Beta_Search(b))