'''Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.'''

#backtracking optimal
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[idx] != board[r][c] or board[r][c] == '#'):
                return False
            board[r][c] = '#' #mark the cell as visited
            res = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1)) #explore all four directions
            board[r][c] = word[idx] #unmark the cell
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): #start the dfs from each cell
                    return True
        return False
#time complexity: O(m * 4^n) because we are starting the dfs from each cell, which takes O(m) time, and for each cell we are exploring all four directions, which takes O(4^n) time, where n is the length of the word, so the total time complexity is O(m * 4^n)
#space complexity: O(n) because we are using a recursive stack to explore the paths, and the maximum depth of the stack is n, which is the length of the word, so the total space complexity is O(n)