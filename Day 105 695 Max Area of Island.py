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

1 <= grid.length, grid[i].length <= 50
'''
#dfs
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area
#time complexity: O(M*N) where M and N are the number of rows and columns in the grid, respectively. We visit each cell at most once.
#space complexity: O(M*N) in the worst case when the grid is filled with land, the recursive call stack can go as deep as M*N in the worst case. 
#In practice, the space complexity is often less than O(M*N) due to the nature of the grid and the distribution of land and water.

