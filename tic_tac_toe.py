# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:55:32 2021

@author: LEGION
"""

from typing import Coroutine
import numpy as np
import time
import os
from Board import Board
from Min_Max import min_max_decision
#from Min_Max_Branching import Alpha_Beta_Search
def utility(value):
    if (value == 0):
        print("Es un empate")
    if (value == -1):
        print("Han ganado las X")
    if (value == 1):
        print("Han ganado las O")

def cambioturno(turno):
    if turno == 1:
        turno = -1
    else:
        turno = 1
    return turno

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

def min_max(board,size_table):
    best_position = min_max_decision(board)
    

def multiplayer(board,turno):
    valido = False
    while valido == False:
        print("Turno del segundo jugador")
        print("Seleccione una casilla: ")
        coordenate = input()
        while(len(coordenate)!=2):
            print("Seleccione una casilla: ")
            coordenate = input()
        a, b = translate(coordenate,board.size) 
        while(a == -1 or b == -1):
                print("Seleccione una casilla: ")
                coordenate = input()
                a, b = translate(coordenate,board.size)       
        if board.table[a][b] != 0:
            print("No se puede jugar sobre esta casilla, intente con otra")
        else:
            valido = True
    return a, b

#def min_max(board,size_table):
#    continue

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
    
    while (request == -2):
        if player_1 == True: # primer jugador (humano)
            print("Turno del primer jugador")
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
            a, b = gamemode(board, cambioturno(player_turn))
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

