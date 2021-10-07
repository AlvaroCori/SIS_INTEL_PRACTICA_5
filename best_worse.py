# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:47:29 2021

@author: LEGION
"""

import numpy as np
import copy as cp
import math as mt
from Board import Board
import time
counter = 0

#turn 1 = O, -1 = X
def check_col(board, col, turn):
    count_x = 0
    count_o = 0
    utility = 0
    for i in range(board.size):
        if board.table[i][col] == 1:
            count_o+=1
        elif board.table[i][col] == -1:
            count_x+=1
    #print("C",col,": count_o:",count_o," count_x:",count_x)
    if count_o > 0 and count_x > 0:
        utility = 0
    elif turn == 1:
        if count_o > 0:
            utility = count_o + 1
        else:
            utility = count_x * -1
    elif turn == -1:
        if count_o > 0:
            utility = count_o * -1
        else:
            utility = count_x + 1
    return utility

def check_row(board, row, turn):
    count_x = 0
    count_o = 0
    utility = 0
    for i in range(board.size):
        if board.table[row][i] == 1:
            count_o+=1
        elif board.table[row][i] == -1:
            count_x+=1
    #print("R",row,": count_o:",count_o," count_x:",count_x)
    if count_o > 0 and count_x > 0:
        utility = 0
    elif turn == 1:
        if count_o > 0:
            utility = count_o + 1
        else:
            utility = count_x * -1
    elif turn == -1:
        if count_o > 0:
            utility = count_o * -1
        else:
            utility = count_x + 1
    return utility

def check_diagonal_LtoR(board, turn):
    count_x = 0
    count_o = 0
    utility = 1
    for i in range(board.size):
        if board.table[i][i] == 1:
            count_o+=1
        elif board.table[i][i] == -1:
            count_x+=1
    #print("D_LtoR: count_o:",count_o," count_x:",count_x)
    if count_o > 0 and count_x > 0:
        utility = 0
    elif turn == 1:
        if count_o > 0:
            utility = count_o + 1
        else:
            utility = count_x * -1
    elif turn == -1:
        if count_o > 0:
            utility = count_o * -1
        else:
            utility = count_x + 1
    return utility

def check_diagonal_RtoL(board, turn):
    count_x = 0
    count_o = 0
    utility = 1
    var = board.size
    for i in range(board.size):
        var -= 1
        if board.table[var][i] == 1:
            count_o+=1
        elif board.table[var][i] == -1:
            count_x+=1
    #print("D_RtoL: count_o:",count_o," count_x:",count_x)
    if count_o > 0 and count_x > 0:
        utility = 0
    elif turn == 1:
        if count_o > 0:
            utility = count_o + 1
        else:
            utility = count_x * -1
    elif turn == -1:
        if count_o > 0:
            utility = count_o * -1
        else:
            utility = count_x + 1
    return utility

def check_for_diagonal(board, turn):
    count_x = 0
    count_o = 0
    utility = 1
    for i in range(board.size):
        for j in range(board.size):
            if board.table[i][j] == 1:
                count_o+=1
            elif board.table[i][j] == -1:
                count_x+=1
        if turn == 1:
            if count_x > 3:
                utility = -1
        else:
            if count_o > 3:
                utility = -1
                
    for i in range(board.size):
        for j in range(board.size):
            if board.table[j][i] == 1:
                count_o+=1
            elif board.table[j][i] == -1:
                count_x+=1
        if turn == 1:
            if count_x > 3:
                utility = -1
        else:
            if count_o > 3:
                utility = -1

    return utility
    

#utility: 0 linea sin posibilidad de ganar o perder, Valor positivo a favor, y negativo en contra

def check(table, turn):
    best_row = 0
    utility_best_row = 0
    best_col = 0
    utility_best_col = 0
    worse_row = 0
    utility_worse_row = 0
    worse_col = 0
    utility_worse_col = 0
    for i in range(table.size):
        #print("best_row:",best_row, "utility_best_row:",utility_best_row)
        #print("best_col:",best_col, "utility_best_col:",utility_best_col)
        #print("worse_row:",worse_row, "utility_worse_row:",utility_worse_row)
        #print("worse_col:",worse_col, "utility_worse_col:",utility_worse_col)
        utility_row = check_row(table, i, turn)
        if  utility_row > utility_best_row:
            best_row = i
            utility_best_row = utility_row 
        elif utility_row < utility_worse_row:
            worse_row = i
            utility_worse_row = utility_row
            
        utility_col = check_col(table, i, turn)
        if utility_col > utility_best_col:
            best_col = i
            utility_best_col = utility_col
        elif utility_col < utility_worse_col:
            worse_col = i
            utility_worse_col = utility_col
            
    if utility_best_row > (utility_worse_row*-1):
        main_row = best_row
        minor_row = worse_row
        #print("mainR:",main_row, "minorR:", minor_row)
    else:
        main_row = worse_row
        minor_row = best_row
        #print("mainR:",main_row, "minorR:", minor_row)
    if utility_best_col > (utility_worse_col*-1):
        main_col = best_col
        minor_col = worse_col
        #print("mainC:",main_col, "minorC:", minor_col)
    else:
        main_col = worse_col
        minor_col = best_col
        #print("mainC:",main_col, "minorC:", minor_col)
    return main_row, minor_row, main_col, minor_col
        
def predef_plays(table, turn):
    count = 0
    a = -1
    b = -1
    for i in range(table.size):
        for j in range(table.size):
            if table.table[i][j] != 0:
                count += 1
    if count == 0:
        a, b = mt.floor(table.size/2), mt.floor(table.size/2)
    else:
        if table.size == 5:
            if table.table[2][2] == 0:
                #print("Al centro")
                a , b = 2, 2
            else:
                #print("Viendo Diagonales...")
                #print("LtoR", check_diagonal_LtoR(table, turn))
                #print("RtoL", check_diagonal_RtoL(table, turn))
                if check_for_diagonal(table, turn) > 0:
                    for k in range(table.size):
                        if table.table[k][k] == 0:
                            a, b = k, k
                            break
                    if a == -1:
                        for k in range(table.size):
                            var -=1
                            if table.table[var][k] == 0:
                                a, b = k, k
                                break
    return a, b

def move(table, turn):
    a, b = predef_plays(table, turn)
    #print("a:",a,"b:",b)
    if a == -1:
        main_row, minor_row, main_col, minor_col = check(table, turn)
        if table.table[main_row][main_col] == 0:
            #print("Signal1")
            a, b = main_row, main_col
        elif table.table[main_row][minor_col] == 0:
            #print("Signal2")
            a, b = main_row, minor_col
        elif table.table[minor_row][main_col] == 0:
            #print("Signal3")
            a, b = minor_row, main_col
        elif table.table[minor_row][minor_col] == 0:
            #print("Signal4")
            a, b = minor_row, minor_col
        elif main_row == minor_row:
            for i in range(table.size):
                if table.table[i][main_col] == 0:
                    a, b = i, main_col
                    break
        elif main_col == minor_col:
            for i in range(table.size):
                if table.table[main_row][i] == 0:
                    a, b = main_row, i
                    break
        if a == -1 and b == -1:
            for i in range(table.size):
                for j in range(table.size):
                    if table.table[i][j] == 0:
                        a, b = i, j
    return a, b

'''
b = Board(5)
b.table[2][2] = -1
#b.table[3][1] = -1
#b.table[3][3] = -1
#b.table[1][1] = 1
#b.table[1][3] = 1
#b.table[1][2] = 1
#b.table[1][0] = -1
#b.table[3][0] = 1
#b.table[2][4] = -1
#b.table[2][0] = 1
#b.table[0][4] = -1
#b.table[0][0] = 1
#b.table[4][4] = -1
#b.table[4][0] = 1
#b.table[1][4] = -1
#b.table[3][4] = 1
b.print_board()
mov_a, mov_b = move(b, 1)
print(mov_a, mov_b)
'''



