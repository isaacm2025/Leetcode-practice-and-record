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

#backtracking
from ast import List


class Solution:
    def genParenthesis(self, n: int) -> List[str]:
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
#time complexity: O(4^n/sqrt(n))  Catalan number
#space complexity: O(n)  for the recursion stack and the result list


#dp
class Solution:
    def genParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n + 1)]
        res[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k - i - 1]:
                        res[k].append("(" + left + ")" + right)
        return res[-1]
#time complexity: O(4^n/sqrt(n))  Catalan number
#space complexity: O(n)  for the result list