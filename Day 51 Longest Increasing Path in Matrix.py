'''You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

Return the length of the longest strictly increasing path within matrix.

From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

Example 1:



Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]

Output: 4
Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].

Example 2:



Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]

Output: 7
Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].

Constraints:

1 <= matrix.length, matrix[i].length <= 100'''

from typing import List
#recursion
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, prev):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev):
                return 0
            res = 1
            for d in directions:
                res = max(res, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))
            return res
        LTP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LTP = max(LTP, dfs(r, c, float('-inf')))
        return LTP
#time complexity: O(m*n*4^(m*n)) where m and n are the number of rows and columns in the matrix
#space complexity: O(m*n) for the recursion stack