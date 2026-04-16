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

from typing import List
#DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != '0'):
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        for r in range(ROWS):
            if board[r][0] == '0':
                capture(r, 0)
            if board[r][COLS - 1] == '0':
                capture(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == '0':
                capture(0, c)
            if board[r][ROWS - 1][c] == '0':
                capture(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '0':
                    board[r][c] = 'x'
                elif board[r][c] == 'T':
                    board[r][c] = '0'
#time complexity O(m * n) where m is the number of rows and n is the number of columns in the grid
#space complexity O(m * n) where m is the number of rows and n is the number of columns in the grid
        
