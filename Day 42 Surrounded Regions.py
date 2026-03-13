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

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(ROWS):
            if board[r][0] == "0":
                dfs(r, 0)
            if board[r][COLS - 1] == "0":
                dfs(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == "0":
                dfs(0, c)
            if board[ROWS - 1][c] == "0":
                dfs(ROWS - 1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "0":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "0"
#time complexity: O(m*n) time complexity, O(m*n) space complexity