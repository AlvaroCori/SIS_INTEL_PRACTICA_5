import numpy as np
import copy as cp
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
        
def cambioturno(turno):
    if turno == 1:
        turno = -1
    else:
        turno = 1
    return turno

def actions(board):
    limit = board.size
    actions_avalaible = []
    for i in range(limit):
        for j in range(limit):
            if (board.table[i][j]==0):
                actions_avalaible.append((i,j))
    return actions_avalaible

def min_max_decision(table, turno):
    best_action = None
    sigmov = min_value
    sigb = lambda x,y:x < y
    v = 9999999
    if turno == 1:
        sigmov = max_value
        sigb = lambda x,y:x > y
        v = -9999999
    
    value = 0
    for action in actions(table):
        ctable = cp.deepcopy(table)
        #print("P1",ctable.table)
        
        value = sigmov(result(ctable,action,turno),cambioturno(turno))
        #print("P2",ctable.table)
        #print(value, action)
        #print("ssssssssssssssss")
        #print(value," ",v," ",sigb(value,v), " ",sigmov)
        if (sigb(value,v)):
            v = value
            best_action = action
    return best_action

def max_value(table, turno):
    request = table.check()
    #print(request,"max")

    #print("Llega max ",table.table)
    if (request != -2):
        #print("req:",request)
        return request
    v = -999999
    for action in actions(table):
        ctable = cp.deepcopy(table)
        #print("M1",ctable.table)
        v = max(v, min_value(result(ctable,action,turno),cambioturno(turno)))
        #print("M2",ctable.table)
        #print(request," max ", v)
    return v

def min_value(table, turno):
    request = table.check()
    #print(request,"min")

    #print("Llega min ",table.table)
    if (request != -2):
        #print("req:",request)
        return request
    v = 999999
    for action in actions(table):
        ctable = cp.deepcopy(table)
        #print("m1",ctable.table)
        #print("m1.b",table.table)
        v = min(v, max_value(result(ctable,action,turno),cambioturno(turno)))
        #print("m2",ctable.table)
        #print(request," min ",v)
    return v


b = Board(3)
'''
#----------------CASO5
#b.table[0][0] = 0
#b.table[0][1] = -1
#b.table[0][2] = 0
#b.table[1][0] = 1
#b.table[1][1] = 1
#b.table[1][2] = -1
#b.table[2][0] = -1
#b.table[2][0] = 1
#b.table[2][1] = 1
#b.table[2][2] = 0
'''
#----------------CASO6
b.table[0][0] = 0
b.table[0][1] = 1
b.table[0][2] = 0
b.table[1][0] = -1
b.table[1][1] = -1
b.table[1][2] = 1
b.table[2][0] = 0
b.table[2][1] = -1
b.table[2][2] = 1
print(b.check())
print(b.table)
b.print_board()

print(min_max_decision(b,-1))


