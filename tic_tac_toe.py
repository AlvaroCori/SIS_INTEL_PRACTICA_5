# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:55:32 2021

@author: LEGION
"""
import numpy as np
import time
import os
import copy
from Board import Board
from Cut_Off import min_max_prunning_cut_off
from Min_Max import min_max_decision
from Min_Max_Branching import Alpha_Beta_Search
#from Min_Max_Branching import Alpha_Beta_Search
def utility(value):
    if (value == 0):
        print("Es un empate")
    if (value == -1):
        print("Han ganado las X")
    if (value == 1):
        print("Han ganado las O")

def change_turn(turn):
    cturn = 1
    if turn == 1:
        cturn = -1
    else:
        cturn = 1
    return cturn

def translate(coordenate, size_table):
    table_positions = {}
    table_positions["A"]=0
    table_positions["B"]=1
    table_positions["C"]=2
    if (size_table == 4):
        table_positions["D"]=3
    if (size_table == 5):
        table_positions["D"]=3
        table_positions["E"]=4
    letter = coordenate[0].upper()
    number = int(coordenate[1]) - 1
    if (number < 0 or number > size_table):
        number = -1
    a = table_positions.get(letter, -1)
    return number,a

def min_max(board,turn):
    best_position = min_max_decision(copy.deepcopy(board),turn)
    return best_position

def min_max_prunning(board,turn):
    best_position = Alpha_Beta_Search(board,turn)
    return best_position

def min_max_cut_off(board,turn):
    difficulty = 3
    if (board.size == 3):
        difficulty = 1
    elif (board.size == 5):
        difficulty = 2
    elif (board.size == 7):
        difficulty = 3
    best_position = min_max_prunning_cut_off(board,turn,difficulty)
    return best_position

def multiplayer(board,turno):
    valido = False
    a = 0
    b = 0
    while valido == False:
        print("Turno del segundo jugador")
        a, b = select_position(board.size)
        if board.table[a][b] != 0:
            print("No se puede jugar sobre esta casilla, intente con otra")
        else:
            valido = True
    return a, b

#def min_max(board,size_table):
#    continue
def select_position(size_table):
    a = -1
    b = -1
    print("Seleccione una casilla: ")
    coordenate = input()
    while(len(coordenate)!=2):
        print("Seleccione una casilla: ")
        coordenate = input()
    a, b = translate(coordenate,size_table)
    while(a == -1 or b == -1):
        print("Seleccione una casilla: ")
        coordenate = input()
        a, b = translate(coordenate,size_table)

    return a,b

def Tic_Tac_Toe(gamemode,size_state, player_turn):
    size_table = size_state + 3
    board = Board(size_table)
    board.print_board()  
    request = -2
    ind = 0
    a = 0
    b = 0
    player = 1
    player_1 = False
    if player == player_turn:
        player_1= True
        player=-1
    while (request == -2):
        if player_1 == True: # primer jugador (humano)
            print("Turno del primer jugador")
            a, b = select_position(size_table)
            if board.table[a][b] == 0:
                if player == 1:
                    board.table[a][b]= -1
                else:
                    board.table[a][b]= 1
                board.print_board()
                ind +=1
                player_1 = False
            else:
                print("No se puede jugar sobre esta casilla, intente con otra")
        else:#segundo jugador (humano, maquina)
            a, b = gamemode(board, change_turn(player_turn))
            if player == 1:
                board.table[a][b]= 1
            else:
                board.table[a][b]= -1
            board.print_board()
            player_1 = True
        request = board.check()

    utility(request)
    print("La partida ha terminado")
    
    

    return 1,1,1

#diccionario
#https://stackoverflow.com/questions/9358983/dictionaries-and-default-values

