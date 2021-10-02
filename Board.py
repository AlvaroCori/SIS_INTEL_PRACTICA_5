import numpy as np
from functools import reduce
class Board:
    def get_actions():
        return 
    def __init__(self,size):
        self.size = size
        self.table = np.zeros((size,size))
        self.actions = set()
    def copy_table(self):
        new_table = Board(self.size)
        for i in range(self.size):
            for j in range(self.size):
                new_table.table[i][j] = self.table[i][j]
        return new_table
    
    def clear_square(self, position):
        self.table[position[0]][position[1]] = 0

    def print_board(self):
        col, fil = self.size, self.size
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
                if self.table[i][j] == 0:
                    imp = imp + "   |"
                elif  self.table[i][j] == -1:
                    imp = imp + " X |"
                elif  self.table[i][j] == 1:
                    imp = imp + " O |"
            print(imp)
            for k in range(col):
                esp = esp + "----"
            print(esp)
            num_fil +=1
            imp = str(num_fil) + "|"
            esp = " "
        return 1
    def check_horizontal(self):
        horizontal = False
        result = -2
        val = 0
        for i in range(self.size):
            cont = 1
            val = self.table[i][0]
            if val == 0:
                break
            for j in range(1,self.size):
                if (val == self.table[i][j]):
                    cont += 1
            if (cont == self.size):
                horizontal = True
                result = 1 if val==1 else -1
        return horizontal, result

    def check_vertical(self):
        vertical = False
        result = -2
        val = 0
        for i in range(self.size):
            cont = 1
            val = self.table[0][i]
            if val == 0:
                break
            for j in range(1,self.size):
                if (val == self.table[j][i]):
                    cont += 1
            if (cont == self.size):
                vertical = True
                result = 1 if val==1 else -1
        return vertical,result

    def check_cruz_left_to_right(self):
        cont = 1
        result = -2
        cruz = False
        val = self.table[0][0]
        if val != 0:
            for i in range(1, self.size):
                if (val == self.table[i][i]):
                    cont +=1
            if (cont == self.size):
                    cruz = True
                    result = 1 if val==1 else -1
        return cruz, result
    
    def check_cruz_right_to_left(self):
        cont = 1
        result = -2
        cruz = False
        val = self.table[self.size-1][0]
        if val != 0:
            for i in range(1, self.size):
                if (val == self.table[self.size-i][i-1]):
                    cont +=1

            if (cont == self.size):
                    cruz = True
                    result = 1 if val==1 else -1
        return cruz, result

#Result valores: (10 ganan O, -10 ganan X, 0 empate, -2 sigue el juego )

    def check(self):
        result = -2
        fil, col = self.size, self.size
        vertical = False
        horizontal = False
        cruz = False
        horizontal, result = self.check_horizontal()
        if (horizontal):
            return result
        vertical, result = self.check_vertical()
        if (vertical):
            return result
        cruz, result = self.check_cruz_left_to_right()
        if (cruz):
            return result
        cruz, result = self.check_cruz_right_to_left()
        if (cruz):
            return result
        counter = 0
        for i in range(fil):
            for j in range(col):
                 if self.table[i][j] != 0:
                    counter = counter + 1
        if (counter==self.size**2):
            result = 0

        return result

    def count_pieces_alienated(self, mark):
        counter = 0
        for row in range(self.size):
            for col in range(self.size):
                if (self.table[row][col] == mark or self.table[col][row] == mark):
                    counter += 1
        for i in range(self.size):
            if (self.table[i][i] == mark):
                counter += 1

        for i in range(self.size):
            if (self.table[self.size-i-1][i] == mark):
                counter += 1
        return counter
        
    #reduce
    #https://www.geeksforgeeks.org/reduce-in-python/
    #dictionary
    #https://realpython.com/iterate-through-dictionary-python/