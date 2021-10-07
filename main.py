from Min_Max_Branching import Alpha_Beta_Search
from tic_tac_toe import *
def menu():
    incise = -1
    dificulty = 0
    player_turn = 18
    dificulty_string = ["facil 3x3", "mediano 4x4", "dificil 5x5"]
    while (incise != 0):
        print("Escoge el modo de juego:")
        print(f"Dificultad: {dificulty_string[dificulty]}")
        print("Primer turno del jugador: Primero "+("Jugador_1" if player_turn == 1 else "Maquina"))
        print("1. Multijugador ")
        print("2. Min_Max ")
        print("3. Min_Max + AlphaBeta Prunning ")
        print("4. MinMaxCutoff")
        print("8. Best_Worse")
        print("5. Heuristica nueva")
        print("6. Cambiar dificultad.")
        print("7. Cambiar turno del jugador")
        print("0. Salir")
        incise = int(input())
        if (incise == 1):
            functionH = multiplayer
        elif(incise == 2):
            functionH = min_max
        elif(incise == 3):
            functionH = min_max_prunning
        elif(incise == 4):
            functionH = min_max_cut_off
        elif(incise == 5): 
            functionH = min_max_cut_off   
        elif(incise == 8): 
            functionH = move
        elif(incise == 6):
            print("\n1 : Facil\n 2 : Menidiano\n 3 : Dificil")
            dificulty = int(input()) -1
        elif (incise == 7):
                print("Seleccione el turno del primer jugador:")
                print("1. Segundo Turno ")
                print("2. Primer Turno ")
                player_turn = int(input())
        if (incise >= 1 and incise <= 5 or incise == 8):
            counters = Tic_Tac_Toe(functionH, dificulty, player_turn)
            print(f"contador de estados expandidos maquina/segundo_jugador: {counters}")
        input("presione enter para continuar.")

menu()