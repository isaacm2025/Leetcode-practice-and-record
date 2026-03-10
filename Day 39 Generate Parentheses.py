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


