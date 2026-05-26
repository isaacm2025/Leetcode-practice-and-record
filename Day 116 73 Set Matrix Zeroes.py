'''Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:



Input: matrix = [
  [0,1],
  [1,0]
]

Output: [
  [0,0],
  [0,0]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
Constraints:

1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1

'''

#bf
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range((COLS))] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for i in range(COLS):
                        mark[r][i] = 0
                    for j in range(ROWS):
                        mark[j][c] = 0
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = mark[r][c]
#time complexity: O((m* n) * (m +n)), where m is the number of rows and n is the number of columns in the input matrix, due to the nested loops and the additional loops for marking.
#space complexity: O(m * n), where m is the number of rows and n is the number of columns in the input matrix, due to the space used for the mark matrix

#iteration
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
            for r in range(ROWS):
                for c in range(COLS):
                    if rows[r] or cols[c]:
                        matrix[r][c] = 0
#time complexity: O(m * n), where m is the number of rows and n is the number of columns in the input matrix, due to the nested loops.
#space complexity: O(m + n), where m is the number of rows and n is the number of columns in the input matrix, due to the space used for the rows and cols arrays

#iteration space optimization
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
#time complexity: O(m * n), where m is the number of rows and n is the number of columns in the input matrix, due to the nested loops.
#space complexity: O(1), due to the constant space used for the rowZero variable and the in-place modifications to the input matrix.