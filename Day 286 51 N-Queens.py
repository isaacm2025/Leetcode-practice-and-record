'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.

Example 1:



Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: [["Q"]]
Constraints:

1 <= n <= 8'''

#hashset
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        postDiag = set()  # r + c
        negDiag = set()  # r - c
        res = []
        board = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in postDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                postDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                col.remove(c)
                postDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
#time complexity: O(n!)  for each row, we have n choices, then n-1 choices for the next row, and so on, leading to n! possible arrangements. However, due to the constraints of the problem (no two queens can attack each other), the actual number of valid arrangements is much less than n!. The time complexity is still considered O(n!) in the worst case.
#space complexity: O(n)  for the recursion stack and the sets used to track the columns and diagonals. The board itself takes O(n^2) space, but since we are only storing the final results, the space complexity is dominated by the recursion stack and the sets