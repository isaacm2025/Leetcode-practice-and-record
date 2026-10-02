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
#time complexity: O(n^2), where n is the number of rows (or columns) in the matrix. We iterate through each element of the matrix to create the rotated version, resulting in a time complexity of O(n^2).
#space complexity: O(n^2), where n is the number of rows (or columns) in the matrix. We create a new matrix of the same size to store the rotated version, resulting in a space complexity of O(n^2).

#reverse and transpose
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#time complexity: O(n^2), where n is the number of rows (or columns) in the matrix. We iterate through each element of the matrix to perform the reverse and transpose operations, resulting in a time complexity of O(n^2).
#space complexity: O(1), as we are performing the rotation in-place without using any additional data structures that scale with the input size. The only extra space used is for a few temporary variables during the swapping process, which does not depend on the size of the input matrix.