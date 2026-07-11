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
grid[i][j] is '0' or '1'.'''

#dfs
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid. In the worst case, we may have to visit every cell in the grid.
#space complexity: O(M * N) in the worst case, where M is the number of rows and N is the number of columns in the grid. This is because we may have to store all the cells in the grid in the call stack during the DFS traversal.


#bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        count = 0
        def bfs(r, c):
            queue = deque()
            grid[r][c] = '0'
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0':
                        continue
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
        return count
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid. In the worst case, we may have to visit every cell in the grid.
#space complexity: O(min(M, N)) where M is the number of rows and N is the number of columns in the grid. This is because we may have to store the cells in the queue during the BFS traversal. 
# In the worst case, the queue may contain all the cells in a single row or column, which is the minimum of M and N.
            