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
    def maAreaOfisland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r <0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid. In the worst case, we may have to visit every cell in the grid.
#space complexity: O(M * N) in the worst case, where M is the number of rows and N is the number of columns in the grid. This is because we may have to store all the cells in the grid in the call stack during the DFS traversal.