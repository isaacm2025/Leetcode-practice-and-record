'''You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]]
  
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
'''
#bfs
from collections import deque
from typing import List
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = dr + row, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
#time complexity: O(M*N) where M and N are the number of rows and columns in the grid, respectively. In the worst case, we may need to perform a BFS from each land cell, and each BFS can take O(M*N) time in the worst case when the grid is filled with land and has no treasure chests. 
#Therefore, the overall time complexity is O((M*N)^2) in the worst case.
#space complexity: O(M*N) in the worst case when the grid is filled with land, the BFS queue can grow up to O(M*N) in the worst case. Additionally, we use a visited matrix of size O(M*N) to keep track of visited cells during the BFS. Therefore, the overall space complexity is O(M*N)