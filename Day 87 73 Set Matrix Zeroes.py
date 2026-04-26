#bf
from ast import List


class Solution:
    def setZeroes(self, matrix: List[List][int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if mark[r][c] == 0:
                    for i in range(ROWS):
                        matrix[i][c] = 0
                    for j in range(COLS):
                        matrix[r][j] = 0
        for r in range(ROWS):
            for c in range(COLS):
                if mark[r][c] == 0:
                    matrix[r][c] = 0
#tc: O(m*n)
#sc: O(m*n)

#iterate through the matrix and mark the rows and columns that need to be set to zero. Then, iterate through the matrix again and set the marked rows and columns to zero.
class Solution:
    def setZeroes(self, matrix: List[List][int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if mark[r][c] == 0:
                    for i in range(ROWS):
                        matrix[i][c] = 0
                    for j in range(COLS):
                        matrix[r][j] = 0
#tc: O(m*n)
#sc: O(m*n)