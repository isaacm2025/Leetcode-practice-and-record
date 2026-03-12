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
All strings within words are distinct.'''

from typing import List
#backtracking 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        result = set()
        def backtracking(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]):
                return False
            board[r][c] = '#'
            res = (backtracking(r + 1, c, i + 1) or
                   backtracking(r - 1, c, i + 1) or
                   backtracking(r, c + 1, i + 1) or
                   backtracking(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
        for word in words:
            flag = False
            for r in range(ROWS):
                if flag:
                    break
                for c in range(COLS):
                    if board[r][c] != word[0]:
                        continue
                    if backtracking(r, c, 0):
                        result.add(word)
                        flag = True
                        break
        return list(result)
#time complexity: O(w * m * n * 4 * 3^t - 1) where w is the number of words, m and n are the dimensions of the board, and t is the average length of the words. The 4 represents the four possible directions to move in the board, and 3^t - 1 accounts for the fact that we can only move in three directions after the first move (since we cannot go back to the previous cell).
#space complexity: O(t) 