import unittest
import numpy as np
from Sudoku import Sudoku
class TestSudoku(unittest.TestCase):

    tablero_1x1 = np.array([1])
    tablero_1x1_2 = np.array([0])

    tablero_4x4 = np.array([[0,1,0,0],
                            [0,0,0,2],
                            [1,0,0,0],
                            [0,0,4,0]])

    tablero_9x9 = np.array([[0,7,2,0,0,4,9,0,0],
                            [3,0,4,0,8,9,1,0,0],
                            [8,1,9,0,0,6,2,5,4],
                            [7,0,1,0,0,0,0,9,5],
                            [9,0,0,0,0,2,0,7,0],
                            [0,0,0,8,0,7,0,1,2],
                            [4,0,5,0,0,1,6,2,0],
                            [2,3,7,0,0,0,5,0,1],
                            [0,0,0,0,2,5,7,0,0]])


    def test_encuentra_fila(self):
        sudoku = Sudoku(self.tablero_4x4)
        self.assertTrue(sudoku.encuentra_fila(0,0))

    def test_encuentra_col(self):
        sudoku = Sudoku(self.tablero_4x4)
        self.assertTrue(sudoku.encuentra_col(0,1))

    def test_encuentra_caja(self):
        sudoku = Sudoku(self.tablero_4x4) 
        self.assertTrue(sudoku.encuentra_caja(1,1,0))

    def test_sudoku_1x1(self):
        sudoku = Sudoku(self.tablero_1x1)
        self.assertTrue(sudoku.solve_sudoku())
        sudoku = Sudoku(self.tablero_1x1_2)
        self.assertTrue(sudoku.solve_sudoku())
        esp = np.array([[1]])
        self.assertEqual(esp.any(),(sudoku.sudoku).any(),msg="Compara Resultado esperado con el resultado obtenido, True--> si son iguales, False-->si no lo son")

    def test_sudoku_4x4(self):
        esperado = np.array([[2, 1, 3, 4],
                             [4, 3, 1, 2],
                             [1, 4, 2, 3],
                             [3, 2, 4, 1]])
        sudoku = Sudoku(self.tablero_4x4)
        self.assertTrue(sudoku.solve_sudoku()) 
        self.assertEqual(esperado.any(),(sudoku.sudoku).any(),msg="Compara Resultado esperado con el resultado obtenido, True--> si son iguales, False-->si no lo son")

    def test_sudoku_9x9(self):
        esperado = np.array( [[6, 7, 2, 1, 5, 4, 9, 3, 8],
                            [3, 5, 4, 2, 8, 9, 1, 6, 7],
                            [8, 1, 9, 3, 7, 6, 2, 5, 4],
                            [7, 2, 1, 6, 4, 3, 8, 9, 5],
                            [9, 4, 8, 5, 1, 2, 3, 7, 6],
                            [5, 6, 3, 8, 9, 7, 4, 1, 2],
                            [4, 8, 5, 7, 3, 1, 6, 2, 9],
                            [2, 3, 7, 9, 6, 8, 5, 4, 1],
                            [1, 9, 6, 4, 2, 5, 7, 8, 3]])
        sudoku = Sudoku(self.tablero_9x9)
        self.assertTrue(sudoku.solve_sudoku())
        self.assertEqual(esperado.any(),(sudoku.sudoku).any(),msg="Compara Resultado esperado con el resultado obtenido, True--> si son iguales, False-->si no lo son")
    
t=TestSudoku()
t.test_encuentra_fila()
t.test_encuentra_caja()
t.test_encuentra_col()
t.test_sudoku_1x1()
t.test_sudoku_4x4()
t.test_sudoku_9x9()
