'''There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:



Input: m = 3, n = 6

Output: 21
Example 2:

Input: m = 3, n = 3

Output: 6
Constraints:

1 <= m, n <= 100
'''

#recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j + 1) + dfs(i + 1, j)
        return dfs(0, 0)
#time complexity: O(2^(m+n)) where m is the number of rows and n is the number of columns. This is because for each cell, we have two choices: move right or move down, leading to a binary tree of possibilities.
#space complexity: O(m+n) where m is the number of rows and n is the number of columns. This is because the maximum depth of the recursion tree can go up to m+n in the worst case.

#dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return dp[i][j]
        return dfs(0, 0)
#time complexity: O(m*n) where m is the number of rows and n is the number of columns. This is because we are storing the results of subproblems in a 2D array, and each cell is computed only once.
#space complexity: O(m*n) where m is the number of rows and n is the number of columns. This is because we are using a 2D array to store the results of subproblems.