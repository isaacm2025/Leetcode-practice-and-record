'''Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
Constraints:

1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
'''

#dfs
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid. We visit each cell once.
#space complexity: O(M * N) in the worst case, where the grid is filled with land and the recursion stack goes as deep as the number of cells in the grid.

#bfs
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr +row, dc + col
                    if nr < 0 or nc <0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0':
                        continue
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid. We visit each cell once.
#space complexity: O(min(M, N)) where M is the number of rows and N is the number of columns in the grid. In the worst case, the queue can contain all the cells in a row or a column