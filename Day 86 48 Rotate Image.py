#bf
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[1][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]
#time complexity: O(n^2) where n is the number of rows (or columns) in the matrix. This is because we need to iterate through each element of the matrix to create the rotated version and then copy it back to the original matrix.
#space complexity: O(n^2) where n is the number of rows (or columns) in the matrix. This is because we create a new matrix to store the rotated version, which requires additional space proportional to the size of the original matrix.

#reverse and transpose
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#time complexity: O(n^2) where n is the number of rows (or columns) in the matrix. This is because we need to iterate through each element of the matrix to reverse it and then transpose it.
#space complexity: O(1) because we are modifying the matrix in place and not using any additional data structures that grow with the size of the input.