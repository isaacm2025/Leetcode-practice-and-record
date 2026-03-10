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

#backtracking(hash set)
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= m or c >= n or (r, c) in path or board[r][c] != word[i]):
                return False
            path.add((r, c))
            res = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1)
            path.remove((r, c))
            return res
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
    
#time complexity: O(m * 4^n) where m is the number of cells in the board and n is the length of the word. In the worst case, we may have to explore all possible paths in the board for each cell, which can lead to a time complexity of O(m * 4^n).
#space complexity: O(n) where n is the length of the word. The space complexity is O(n) because in the worst case, we may have to explore a path of length n


