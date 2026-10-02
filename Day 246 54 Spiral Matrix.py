'''Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:



Input: matrix = [[1,2],[3,4]]

Output: [1,2,4,3]
Example 2:



Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]

Example 3:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:

1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100

'''

#iteration
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        steps = [len(matrix[0]), len(matrix) - 1]
        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res
#time complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix. We visit each element of the matrix exactly once, resulting in a time complexity of O(m * n).
#space complexity: O(1), as we are using a constant amount of extra space for variables (res, directions, steps, r, c, d) regardless of the input size. The output list res is not considered extra space since it is required to store the result.