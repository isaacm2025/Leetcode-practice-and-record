'''You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7'''

from typing import List

#brute force
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return open == 0
        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            dfs(s + '(')
            dfs(s + ')')
        dfs('')
        return res

#time complexity: O(2^(2n) * n) where 2^(2n) is the number of possible combinations of parentheses and n is the time taken to validate each combination.
#space complexity: O(2^(2n) * n) where 2^(2n) is the number of valid combinations of parentheses and n is the space taken to store each combination

#backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
#time complexity: O(4^n / sqrt(n)) where 4^n is the number of possible combinations of parentheses and sqrt(n) is the time taken to generate each combination.
#space complexity: O(n) where n is the maximum depth of the recursion stack.

#Dynamic programming
class Solution:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n + 1)]
        res[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k - 1 - i]:
                        res[k].append(f"({left}){right}")
        return res[-1]
#time complexity: O(4^n / sqrt(n)) where 4^n is the number of possible combinations of parentheses and sqrt(n) is the time taken to generate each combination.
#space complexity: O(n) where n is the maximum depth of the recursion stack.

