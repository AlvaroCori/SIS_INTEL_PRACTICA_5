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
        #print("P1",ctable.table)
        #print(table.table)
        counter +=1
        next_actions = actions.copy()
        action = next_actions.pop(index)
        value = sigmov(result(table,action,turn),next_actions,change_turn(turn))
        #print("P2",ctable.table)
        #print("ssssssssssssssss")
        #print(value," ",v," ",sigb(value,v), " ",sigmov)
        if (sigb(value,v)):
            v = value
            best_action = action
        table.clear_square(action)
    return best_action, counter

def max_value(table, actions, turn):
    request = table.check()
    #print(request,"max")

    #print("Llega max ",table.table)
    if (request != -2):
        #print("req:",request)
        return request
    v = -999999
    for index in actions:
        global counter
        counter +=1
        #print("M1",ctable.table)
        next_actions = actions.copy()
        action = next_actions.pop(index)
        v = max(v, min_value(result(table,action,turn),next_actions,change_turn(turn)))
        table.clear_square(action)
        #print("M2",ctable.table)
        #print(request," max ", v)



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


'''
b = Board(3)
print(b.check())
print(b.table)
init = time.time()
print(min_max_decision(b,-1))
end = time.time()
print(f"tiempo: {end-init}")
print(f"counter: {counter}")
'''
'''
#----------------CASO5
b.table[0][0] = 0
b.table[0][1] = -1
b.table[0][2] = 0
b.table[1][0] = 1
b.table[1][1] = 1
b.table[1][2] = -1
b.table[2][0] = -1
b.table[2][0] = 1
b.table[2][1] = 1
b.table[2][2] = 0
'''
'''
b = Board(3)
print(b.check())
b.table[0][0] = 1
b.table[0][1] = 1
b.table[0][2] = -1
b.table[1][0] = 1
b.table[1][1] = -1
b.table[1][2] = 0
b.table[2][0] = 0
b.table[2][1] = 0
b.table[2][2] = 0
print(b.table)
print(min_max_decision(b,-1))
'''
'''
b = Board(3)
print(b.check())
b.table[0][0] = -1

print(b.table)
print(min_max_decision(b,1))
'''
