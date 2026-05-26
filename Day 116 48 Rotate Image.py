'''Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:



Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

#bf
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]
#time complexity: O(n^2), where n is the number of rows (or columns) in the input matrix, due to the nested loops.
#space complexity: O(n^2), where n is the number of rows (or columns) in the input matrix, due to the space used for the rotated matrix

#rotated by four cells
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
#time complexity: O(n^2), where n is the number of rows (or columns) in the input matrix, due to the nested loops.
#space complexity: O(1), since we are rotating the matrix in-place and not using any additional data structures that grow with the input size.