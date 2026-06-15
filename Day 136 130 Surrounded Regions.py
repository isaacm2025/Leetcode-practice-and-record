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
        
#time complexity: O(m*n) where m is the number of rows and n is the number of columns  
#space complexity: O(m*n) in the worst case when all cells are 'O' and we have to capture all of them