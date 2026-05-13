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
board and word consists of only lowercase and uppercase English letters.
'''

#backtracking
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word:str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
#tiime complexity: O(m * 4^n) where m is the number of cells in the board and n is the length of the word
#space complexity: O(n) where n is the length of the word, which is the maximum depth of the recursion stack. The path set can also take up to O(n) space in the worst case, but it is not counted towards the overall space complexity since it is not part of the recursion stack.

#optimal
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word:str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == '#'):
                return False
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
#time complexity: O(m * 4^n) where m is the number of cells in the board and n is the length of the word
#space complexity: O(n) where n is the length of the word, which is the maximum depth of the recursion stack. The board is modified in place to mark visited cells, so it does not require additional space for a path set