'''You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).


Example 1:



Input: grid = [[0,1],[2,3]]

Output: 3

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
0 <= grid[i][j] < n^2
'''

#dijkstra
from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n -1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr == n or nc == n or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))
#time complexity: O(n^2 * log(n^2)) where n is the length of the grid. We may potentially visit all n^2 cells in the grid, and for each cell, we perform a heap operation that takes O(log(n^2)) time.
#space complexity: O(n^2) for the minHeap and visit set, leading to a total space complexity of O(n^2).