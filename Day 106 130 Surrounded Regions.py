'''You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:



Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.'''

#dfs
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        for r in range(ROWS):
            if board[r][0] == 'O':
                capture(r, 0)
            if board[r][COLS - 1] == 'O':
                capture(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == 'O':
                capture(0, c)
            if board[ROWS - 1][c] == 'O':
                capture(ROWS - 1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
#time complexity: O(M*N)
#space complexity: O(M*N)

#bfs
from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                if (row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != 'O'):
                    continue
                board[row][col] = 'T'
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))
        for r in range(ROWS):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][COLS - 1] == 'O':
                bfs(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[ROWS - 1][c] == 'O':
                bfs(ROWS - 1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
#time complexity: O(M*N)
#space complexity: O(M*N)