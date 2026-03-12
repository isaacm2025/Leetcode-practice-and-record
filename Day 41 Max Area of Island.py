'''You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:



Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:

1 <= grid.length, grid[i].length <= 50'''

from typing import List
#DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS, = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c))
        return area
#time complexity: O(m * n) where m and n are the number of rows and columns in the grid, respectively. In the worst case, we may have to visit every cell in the grid once.
#space complexity: O(m * n) in the worst case, if the grid is filled with land (1's), the depth of the recursion could be equal to the number of cells in the grid, leading to a space complexity of O(m * n) due to the call stack.

#BFS
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    res += 1
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area
#time complexity: O(m * n) where m and n are the number of rows and columns in the grid, respectively. In the worst case, we may have to visit every cell in the grid once.
#space complexity: O(min(m, n)) in the worst case, if the grid is filled with land (1's), the queue could hold all the cells in the grid, leading to a space complexity of O(min(m, n)) due to the breadth of the search