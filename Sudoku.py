import numpy as np
import math
class Sudoku:
    UNASSIGNED = 0
    sudoku = np.array([])
    def __init__(self,tablero):
        self.sudoku = tablero

#verifica si un numero se encuentra en la fila actual
    def encuentra_fila(self, row, number):
        lon = len(self.sudoku)
        for i in range(0,lon):
            if self.sudoku[row,i] == number:
                return True
        return False
    
#verifica si un numero se encuentra en la columna actual
    def encuentra_col(self, col, number):
        lon = len(self.sudoku)
        for i in range(0,lon):
            if self.sudoku[i,col] == number:
                return True
        return False
 
#verifica si un numero se encuentra en la caja 3x3 actual 
    def encuentra_caja(self, row, col, number):
        base = int(math.sqrt(len(self.sudoku)))
        r = row - row % base
        c = col - col % base
        for i in range(r,r+base):
            for j in range(c,c+base):
                if self.sudoku[i,j] == number:
                    return True
        return False

    def solve_sudoku_1x1(self):
        if self.sudoku[0] == 1 :
            return True
        else:
            self.sudoku[0]=1
            return True

    def isAllowed(self, row, col, number):
        return not(self.encuentra_fila(row, number) or self.encuentra_col(col, number) or self.encuentra_caja(row, col, number))

    def solve_sudoku(self):
        if len(self.sudoku) == 1:
            return self.solve_sudoku_1x1()
        else:
            l = len(self.sudoku)
            for row in range(0,l):
                for col in range(0,l):
                    if self.sudoku[row,col] == self.UNASSIGNED:
                        for number in range(1,l+1):
                            if self.isAllowed(row, col, number):
                                self.sudoku[row,col] = number
                                if (self.solve_sudoku()):
                                    return True
                                else:
                                    self.sudoku[row,col] = self.UNASSIGNED
                        return False
            return True            


