import numpy as np
import copy as cp
from Board import Board
import time


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

def Alpha_Beta_Search(table, turn):
    val = 0
    s_act = None
    actions = get_actions(table)
    v = 999999
    sigmov = max_value
    sigb = lambda x,y:x > y
    if turn == 1:
        sigmov = min_value
        sigb = lambda x,y:x > y
        v = -999999

    for index in actions:
        next_actions = actions.copy()
        action = next_actions.pop(index)
        val = sigmov(result(table,action,turn),next_actions,-99999,99999, change_turn(turn))
        if (sigb(val,v)):
            v = val
            s_act = action
    return s_act
def min_value(table, actions, alpha, beta,turn):
    request = table.check()
    if (request!=-2):
        return request
    v = 999999
    for index in actions:
        next_actions = actions.copy()
        action = next_actions.pop(index)
        v = min(v, max_value(result(table,action,turn),next_actions,alpha,beta, change_turn(turn)))
        if (v <= alpha):
            return v
        beta = min(beta,v)
    return v

def max_value(table,actions,alpha,beta,turn):
    request = table.check()
    if (request!=-2):
        return request
    v = -999999
    for index in actions:
        next_actions = actions.copy()
        action = next_actions.pop(index)
        v = max(v, min_value(result(table,action,turn),next_actions,alpha,beta, change_turn(turn)))
        if (alpha >= beta):
            return v
        alpha = max(alpha,v)
    return v

b = Board(3)
'''
b.table[0] = [-1,-1,-1,-1,1]
b.table[1] = [1,-1,1,1,0]
b.table[2] = [-1,-1,-1,-1,0]
b.table[3] = [1,-1,1,1,0]
b.table[4] = [-1,-1,-1,-1,0]
'''
b.table[0][0]=-1
b.table[2][0]=1
b.table[2][1]=-1
b.table[1][1]=1
b.table[0][2]=-1

print(b.check())
print(b.table)
init = time.time()
print(Alpha_Beta_Search(b,1))
end = time.time()
print(f"tiempo: {end-init}")

##aumentar turnos

