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
                open += 1 if c == '(' else -1
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
        dfs("")
        return res
#time complexity: O(2^(2n) * n) where n is the number of pairs of parentheses. We generate 2^(2n) strings and check if each string is valid in O(n) time.
#space complexity: O(2^(2n) * n) for the result list and the recursion stack.


#dp
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n + 1)]
        res[0] = [""]
        for i in range(1, n + 1):
            for j in range(i):
                for left in res[j]:
                    for right in res[i - 1 - j]:
                        res[i].append("(" + left + ")" + right)
        return res[-1]
#time complexity: O(4^n / sqrt(n)) where n is the number of pairs of parentheses. This is the nth Catalan number.
#space complexity: O(n) for the result list.