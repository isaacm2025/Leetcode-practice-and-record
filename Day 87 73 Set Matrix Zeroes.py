#bf
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
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
    def setZeroes(self, matrix: List[List[int]]) -> None:
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

#optimal
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False
        col_zero = False
        for r in range(ROWS):
            if matrix[r][0] == 0:
                row_zero = True
                break
        for c in range(COLS):
            if matrix[0][c] == 0:
                col_zero = True
                break
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if row_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
        if col_zero:
            for c in range(COLS):
                matrix[0][c] = 0
#tc: O(m*n)
#sc: O(1)