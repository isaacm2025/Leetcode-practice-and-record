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

#bf
import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        def dfs(node, time):
            r, c = node
            if min(r, c) <0 or max(r, c) >= n or visit[r][c]:
                return 100000000
            if r == (n - 1) and c == (n - 1):
                return max(time, grid[r][c])
            visit[r][c] = True
            time = max(time, grid[r][c])
            res = min(dfs((r + 1, c), time), dfs((r -1, c), time), dfs((r, c + 1), time), dfs((r, c - 1), time))
            visit[r][c] = False
            return res
        return dfs((0, 0), 0)
#time complexity is O(4^N^2) because we are exploring all possible paths in the grid and each cell has 4 possible directions to move. The space complexity is O(N^2) because we are using a visited matrix to keep track of the cells we have already visited.
#space complexity is O(N^2) because we are using a visited matrix to keep track of the cells we have already visited.


#dfs
import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        minHeap = maxHeap = grid[0][0]
        for row in range(n):
            maxHeap = max(maxHeap, max(grid[row]))
            minHeap = min(minHeap, min(grid[row]))
        def dfs(node, time):
            r, c = node
            if min(r, c) < 0 or max(r, c) >= n or visit[r][c] or grid[r][c] > time:
                return False
            if r ==(n - 1) and c == (n -1):
                return True
            visit[r][c] = True
            return (dfs((r + 1, c), time) or dfs((r - 1, c), time) or dfs((r, c + 1), time) or dfs((r, c - 1), time))
        for time in range(minHeap, maxHeap):
            if dfs((0, 0), time):
                return time
            for r in range(n):
                for c in range(n):
                    visit[r][c] = False
        return maxHeap
#time complexity is O(N^4)
#space complexity is O(N^2) because we are using a visited matrix to keep track of the cells we have already visited.