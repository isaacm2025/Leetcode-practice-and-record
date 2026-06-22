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

1 <= matrix.length, matrix[i].length <= 100
'''

#dp
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} 
        def dfs(r, c, preVal):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= preVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
#time complexity: O(m*n) where m and n are the number of rows and columns in the matrix, respectively. 
# Each cell is visited at most once during the DFS traversal, and the results are stored in the dp dictionary to avoid redundant calculations.
#space complexity: O(m*n) in the worst case, where m and n are the number of rows and columns in the matrix, respectively. 
# This is because in the worst case, all cells in the matrix could be part of the longest increasing path, and the dp dictionary would store a value for each cell. Additionally, the recursive call stack could also grow to O(m*n) in the worst case if the longest path is very long.
