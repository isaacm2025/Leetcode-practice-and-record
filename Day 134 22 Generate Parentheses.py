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

#bf
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else - 1
                if open < 0:
                    return False
            return not open
        def dfs(s: str):
            if n * 2 == len(s):
                if backtrack(s):
                    res.append(s)
                return
            dfs(s + '(')
            dfs(s + ')')
        dfs('')
        return res
#time complexity: O(2^(2n) * n) because we are generating 2^(2n) strings and for each string we are checking if it is valid, which takes O(n) time, so the total time complexity is O(2^(2n) * n)
#space complexity: O(2^(2n) * n) because we are generating 2^(2n) strings and each string takes O(n) space, so the total space complexity is O(2^(2n) * n)