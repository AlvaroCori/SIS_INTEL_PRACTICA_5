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
    utility = 1
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
        elif count_x > 0:
            utility = count_x * -1
    elif turn == -1:
        if count_o > 0:
            utility = count_o * -1
        elif count_x > 0:
            utility = count_x + 1
    #print("col:",col," utility:",utility)
    return utility

def check_row(board, row, turn):
    count_x = 0
    count_o = 0
    utility = 1
    for i in range(board.size):
        if board.table[row][i] == 1:
            count_o+=1
        elif board.table[row][i] == -1:
            count_x+=1
    #print("R",row,": count_o:",count_o," count_x:",count_x, "u:",utility)
    if count_o > 0 and count_x > 0:
        utility = 0
    elif turn == 1:
        if count_o > 0:
            utility = count_o + 1
        elif count_x > 0:
            utility = count_x * -1
    elif turn == -1:
        if count_o > 0:
            utility = count_o * -1
        elif count_x > 0:
            utility = count_x + 1
    #print("row:",row," utility:",utility)
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

#utility: 0 linea sin posibilidad de ganar o perder, Valor positivo a favor, y negativo en contra

def check_utility(table, turn):
    utility = 0
    best_row = 0
    utility_best_row = 1
    best_col = 0
    utility_best_col = 1
    worse_row = 0
    utility_worse_row = 1
    worse_col = 0
    utility_worse_col = 1
    for i in range(table.size):
        print("i:",i)
        
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
            
        print("best_row:",best_row, "utility_best_row:",utility_best_row)
        print("best_col:",best_col, "utility_best_col:",utility_best_col)
        print("worse_row:",worse_row, "utility_worse_row:",utility_worse_row)
        print("worse_col:",worse_col, "utility_worse_col:",utility_worse_col)
    
    best_dia = check_diagonal_LtoR(table, turn)
    rev = check_diagonal_RtoL(table, turn)
    if rev > best_dia:
        best_dia = rev
    
    
    if utility_best_row > abs(utility_worse_row):
        main_row = utility_best_row 
    else:
        main_row = utility_worse_row 
    if utility_best_col > abs(utility_worse_col):
        main_col = utility_best_col
    else:
        main_col = utility_worse_col 
    print("main_row:",main_row,"main_col:",main_col,"best_dia:",best_dia,)
    
    if abs(main_row) > abs(main_col) and abs(main_row) > abs(best_dia):
        if main_row > 0:
            utility = 1
        elif main_row < 0:
            utility = -1
    elif abs(main_col) > abs(main_row) and abs(main_col) > abs(best_dia):
        if main_col > 0:
            utility = 1
        elif main_col < 0:
            utility = -1
    elif abs(best_dia) > abs(main_row) and abs(best_dia) > abs(main_col):
        if best_dia > 0:
            utility = 1
        elif best_dia < 0:
            utility = -1
        
    return utility
        

b = Board(5)
b.table[2][2] = -1
b.table[3][1] = -1
b.table[3][3] = -1
b.table[1][1] = 1
b.table[1][3] = 1
b#.table[1][2] = 1
#b.table[1][0] = 1
#b.table[4][0] = -1
#b.table[4][3] = -1
#b.table[2][0] = 1
#b.table[0][4] = -1
#b.table[0][0] = 1
#b.table[4][4] = -1
#b.table[4][0] = 1
#b.table[1][4] = -1
#b.table[3][4] = 1
b.print_board()
print(check_utility(b, 1))

