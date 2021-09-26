# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:55:32 2021

@author: LEGION
"""

import numpy as np
import time
import os

def create_board(sizeState):
    board = np.zeros((sizeState,sizeState))
    return board

def print_board(board):
    col, fil = np.shape(board)
    num_fil = 1
    imp = str(num_fil) + "|"
    esp = " "
    
    if col == 3:
        print("   A   B   C")
    elif col == 4:
        print("   A   B   C   D")
    elif col == 5:
        print("   A   B   C   D   E")
    
    for i in range(col):
        esp = esp + "----"
    print(esp)
    esp = " "
    
    for i in range(fil):
        for j in range(col):
            if board[i][j] == 0:
                imp = imp + "   |"
            elif  board[i][j] == 1:
                imp = imp + " X |"
            elif  board[i][j] == 2:
                imp = imp + " O |"
        print(imp)
        for k in range(col):
            esp = esp + "----"
        print(esp)
        num_fil +=1
        imp = str(num_fil) + "|"
        esp = " "
    return 1

def translate(coordenate):
    letter = coordenate[0]
    number = int(coordenate[1]) - 1
    a = 0
    if letter == "A":
        a = 0
    elif letter == "B":
        a = 1
    elif letter == "C":
        a = 2
    elif letter == "D":
        a = 3
    elif letter == "E":
        a = 4
    return number,a

def check(board):
    result = False
    fil, col = np.shape(board)

    vertical = False
    horizontal = False
    val = 0
    for i in range(fil):
        cont = 0
        for j in range(col):
            if j == 0:
                val = board[i][j]
                if board[i][j] > 0:
                    cont +=1
            else:
                if board[i][j] == val and board[i][j] > 0:
                    cont +=1
        if cont > fil-1:
            horizontal = True
            if val == 1:
                print("Han ganado las X")
            else:
                print("Han ganado las O")
    
    for i in range(col):
        cont = 0
        for j in range(fil):
            if j == 0:
                val = board[j][i]
                if board[j][i] > 0:
                    cont +=1
            else:
                if board[j][i] == val and board[j][i] > 0:
                    cont +=1
        if cont > col-1 :
            vertical = True
            if val == 1:
                print("Han ganado las X")
            else:
                print("Han ganado las O")
            
    if horizontal == False and vertical == False:
        for i in range(fil):
            for j in range(col):
                if board[i][j] == 0:
                    result = True
        if result == False:
            print("Es un empate")
    return result

def multiplayer(board):
    valido = False
    while valido == False:
        print("Turno del segundo jugador")
        print("Seleccione una casilla: ")
        coordenate = input()
        a, b = translate(coordenate) 
        if board[a][b] != 0:
            print("No se puede jugar sobre esta casilla, intente con otra")
        else:
            valido = True
    return a, b

def Tic_Tac_Toe(gamemode):
    print("Seleccione el tamanio del tablero (Ejem: 3x3 = 3):")
    sizeState = int(input())
    board = create_board(sizeState)
    print_board(board)
    ind = 0
    
    print("Seleccione el turno del primer jugador:")
    print("1. Primer Turno ")
    print("2. Segundo Turno ")
    player = int(input())
    player_1 = False
    if player == 1:
        player_1= True
    
    while check(board) == True:
        if player_1 == True:
            print("Turno del primer jugador")
            print("Seleccione una casilla: ")
            coordenate = input()
            a, b = translate(coordenate)
            if board[a][b] == 0:
                if player == 1:
                    board[a][b]= 1
                else:
                    board[a][b]= 2
                print_board(board)
                ind +=1
                player_1 = False
            else:
                print("No se puede jugar sobre esta casilla, intente con otra")
        else:
            a, b = gamemode(board)
            if player == 1:
                board[a][b]= 2
            else:
                board[a][b]= 1
            print_board(board)
            player_1 = True
            
    print("La partida ha terminado")
    
    

    return 1

def menu():
    incise = -1
    while (incise != 0):
        print("Escoge el modo de juego:")
        print("1. Multijugador ")
        print("2. Min_Max ")
        print("3. Min_Max + AlphaBeta Prunning ")
        print("4. MinMaxCutoff")
        incise = int(input())
        if (incise == 1):
            functionH = multiplayer
        elif(incise == 2):
            #functionH = min_max
            functionH = multiplayer
        elif(incise == 3):
            #functionH = min_max_AlphaBeta
            functionH = multiplayer
        elif(incise == 4):
            #functionH = min_maxCutOff
            functionH = multiplayer
        if (incise >= 1 and incise <= 4):
            init = time.time()
            request, state,counter = Tic_Tac_Toe(functionH)
            end = time.time()
            #print("RESULTADOS:")
            #printSequency(state)
            #print(("" if request else "no ") + "se hallo la ruta al objetivo.")
            #print(f"Se expandio {counter} estados.")
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")
        input("presione enter para continuar.")

menu()
