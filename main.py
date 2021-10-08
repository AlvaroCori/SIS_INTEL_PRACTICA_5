from tic_tac_toe import *
def menu():
    incise = -1
    dificulty = 0
    player_turn = 1
    dificulty_string = ["facil 3x3", "mediano 4x4", "dificil 5x5"]
    while (incise != 0):
        print("Escoge el modo de juego:")
        print(f"Dificultad: {dificulty_string[dificulty]}")
        print("Primer turno del jugador: Primero "+("Jugador_1" if player_turn == 1 else "Maquina"))
        print("1. Multijugador ")
        print("2. Min_Max ")
        print("3. Min_Max + AlphaBeta Prunning ")
        print("4. Cut Off diferencias entre casillas")
        print("5. Thanatos Cut Off")
        print("6. Entrenador de algoritmos.")
        print("7. Cambiar dificultad.")
        print("8. Cambiar turno del jugador")
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
            functionH = min_max_cut_off_thanatos 
        elif(incise == 6): 
            functionH = move
        elif(incise == 7):
            print("*********************************")
            print("\n 1 : Facil\n 2 : Mediano\n 3 : Dificil\n")
            print("*********************************")
            dificulty = int(input()) -1
        elif (incise == 8):
                print("Seleccione el turno del primer jugador:")
                print("1. Primer Turno.")
                print("2. Segundo Turno.")
                player_turn = int(input())
        if (incise >= 1 and incise <= 6):
            counters = Tic_Tac_Toe(functionH, dificulty, player_turn)
            print(f"contador de estados expandidos maquina/segundo_jugador: {counters}")
            print(f"Total: {sum(counters)}")
        if (incise != 0):
            input("presione enter para continuar.")

menu()