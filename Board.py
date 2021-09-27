import numpy as np
class Board:
    def __init__(self,size):
        self.size = size
        self.table = np.zeros((size,size))

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

    def check(self):
        result = -2
        fil, col = self.size, self.size
        vertical = False
        horizontal = False
        cruz = False
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
        
        cont = 1
        val = self.table[0][0]
        if val != 0:
        
            for i in range(1, self.size):
                if (val == self.table[i][i]):
                    cont +=1

            if (cont == self.size):
                    cruz = True
                    result = 1 if val==1 else -1
                    return result
        
        cont = 1
        val = self.table[self.size-1][0]
        if val != 0:
            for i in range(1, self.size):
                if (val == self.table[self.size-i][i]):
                    cont +=1

            if (cont == self.size):
                    cruz = True
                    result = 1 if val==1 else -1
        
        if horizontal == False and vertical == False and cruz == False:
            counter = 0
            for i in range(fil):
                for j in range(col):
                    if self.table[i][j] != 0:
                        counter = counter + 1
            if (counter==self.size**2):
                result = 0
        return result