'''You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:



Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4
Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1
Constraints:

1 <= grid.length, grid[i].length <= 10'''

#bfs
import collections
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if (rr in range(len(grid)) and cc in range(len(grid[0])) and grid[rr][cc] == 1):
                        grid[rr][cc] = 2
                        fresh -= 1
                        q.append((rr, cc))
            time += 1
        return time if fresh == 0 else - 1
#time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. We visit each cell at most once.
#space complexity: O(m * n) in the worst case, where all the cells in the grid are rotten fruits and we need to store all of them in the queue.