'''You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:



Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.


Example 2:

Input: board = [["X"]]

Output: [["X"]]
Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
'''

#dfs
from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the board. This is because we are performing a DFS from each cell in the board, and each cell can be visited at most once.
#space complexity: O(M * N) where M is the number of rows and N is the number of columns in the board.


#bfs
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = deque()
            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                        queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            queue.append((nr, nc))
        bfs(0, 0)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the board. This is because we are performing a BFS from each cell in the board, and each cell can be visited at most once.
#space complexity: O(M * N) where M is the number of rows and N is the number of columns in the board. 
# This is because we are using a queue to keep track of the cells that need to be processed, and in the worst case, all cells can be added to the queue, so the space used by the queue can be proportional to the number of cells.