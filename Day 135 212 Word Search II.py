'''Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]
Example 2:



Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []
Constraints:

1 <= board.length, board[i].length <= 12
board[i] consists only of lowercase English letter.
1 <= words.length <= 30,000
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.
'''

# backtracking
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = []
        def backtrack(r, c, i, word):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i]):
                return False
            board[r][c] = '*'
            ret = (
                backtrack(r + 1, c, i + 1, word)
                or backtrack(r - 1, c, i + 1, word)
                or backtrack(r, c + 1, i + 1, word)
                or backtrack(r, c - 1, i + 1, word)
            )
            board[r][c] = word[i]
            return ret
        for word in words:
            flag = False
            for r in range(ROWS):
                if flag:
                    break
                for c in range(COLS):
                    if board[r][c] != word[0]:
                        continue
                    if backtrack(r, c, 0, word):
                        res.append(word)
                        flag = True
                        break
        return res
            