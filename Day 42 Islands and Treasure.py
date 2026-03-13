'''You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}'''

from typing import List

#brute force backtracking
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647 #2**31 - 1, represents infinity
        visit = [[False for _ in range(COLS)] for _ in range(ROWS)]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visit[r][c] or grid[r][c] == -1:
                return INF
            if grid[r][c] == 0:
                return 0
            
            visit[r][c] = True
            res = INF
            for dx, dy in directions:
                res = min(res, dfs(r + dx, c + dy) + 1)
            visit[r][c] = False
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)
#time complexity: O(m*n*4^(m*n)) time complexity, O(m*n) space complexity
#space complexity: O(m * n)



