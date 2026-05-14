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
from ast import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."]* n for i in range(n)]
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = "Q"
                backtrack(row + 1)
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                board[row][c] = "."
        backtrack(0)
        return res
#time complexity: O(n!)
#space complexity: O(n^2)

#bit manipulation
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = 0
        posDiag = 0
        negDiag = 0
        res = []
        board = [["."] * n for i in range(n)]
        def backtrack(row):
            nonlocal col, posDiag, negDiag
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if ((col & (1 << c)) or (posDiag & (1 << (row + c))) or (negDiag & (1 << (row - c + n)))):
                    continue
                col ^= (1 << c)
                posDiag ^= (1 << (row + c))
                negDiag ^= (1 << (row - c + n))
                board[row][c] = "Q"
                backtrack(row + 1)
                col ^= (1 << c)
                posDiag ^= (1 << (row + c))
                negDiag ^= (1 << (row - c + n))
                board[row][c] = "."
        backtrack(0)
        return res
#time complexity: O(n!)
#space complexity: O(n^2)

