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

#sp op
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(m - 1):
            newDp = [1] * n
            for j in range(n - 2, -1, -1):
                newDp[j] = dp[j] + newDp[j + 1]
            dp = newDp
        return dp[0]
#time complexity: O(m*n) where m is the number of rows and n is the number of columns
#space complexity: O(n) where n is the number of columns