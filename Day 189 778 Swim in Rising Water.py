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
0 <= grid[i][j] < n^2
'''

#dijkstra's algorithm
from typing import List
import heapq
class Solution:
    def swimInWater(self, grid:List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc <0 or nr == n or nc == n or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
#time complexity: O(n^2 * log n) where n is the length of the grid. We may need to visit all n^2 cells in the grid, and for each cell, we perform a heap operation which takes O(log n) time.
#space complexity: O(n^2) where n is the length of the grid. We use a priority queue to store the cells to be processed, which can hold up to n^2 cells in the worst case. Additionally, we use a set to keep track of visited cells, which can also hold up to n^2 cells in the worst case.