'''You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

Example 1:



Input: grid = [[0,1],[2,3]]

Output: 3
Explanation: For a path to exist to the bottom right square grid[1][1] the water elevation must be at least 3. At time t = 3, the water level is 3.
Example 2:



Input: grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]
]

Output: 8
Explanation: The water level must be at least 8 to reach the bottom right square. The path is [0, 1, 2, 4, 8, 7, 6].

Constraints:

grid.length == grid[i].length
1 <= grid.length <= 50
0 <= grid[i][j] < n^2'''

#bs + dfs
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        minH = maxH = grid[0][0]
        for i in range(n):
            maxH = max(maxH, max(grid[i]))
            minH = min(minH, min(grid[i]))
        def dfs(node, t):
            r, c = node
            if (min(r, c) < 0 or max(r, c) >= n or visit[r][c] or grid[r][c] > t):
                return False
            if r == n - 1 and c == n - 1:
                return True
            visit[r][c] = True
            return dfs((r + 1, c), t) or dfs((r - 1, c), t) or dfs((r, c + 1), t) or dfs((r, c - 1), t)
        l, r = minH, maxH
        while l < r:
            mid = (l + r) >> 1
            if dfs((0, 0), mid):
                r = mid
            else:
                l = mid + 1
            for i in range(n):
                for j in range(n):
                    visit[i][j] = False
        return r
#time comlexity: O(n^2 log n) where n is the length of the grid. The binary search takes log n time, and for each mid value, we perform a DFS that can visit up to n^2 cells in the grid.   
#space complexity: O(n^2) where n is the length of the grid. We use a 2D list visit to keep track of visited cells during the DFS, which takes up O(n^2) space.