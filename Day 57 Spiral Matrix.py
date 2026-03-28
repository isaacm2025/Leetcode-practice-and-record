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
-100 <= matrix[i][j] <= 100'''


from typing import List
#recursion
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n =len(matrix), len(matrix[0])
        res = []
        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return
            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])
            dfs(row - 1, col, r, c, dc, -dr)
        dfs(m, n, -1, 0, 0, 1)
        return res
#time complexity O(m*n)
#space complexity O(m*n) for the result list and O(m+n) for the recursion stack

#iterative
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
#time complexity O(m*n)
#space complexity O(m*n) for the result list

#iteration optimized
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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
#time complexity O(m*n)
#space complexity O(m*n) for the result list

