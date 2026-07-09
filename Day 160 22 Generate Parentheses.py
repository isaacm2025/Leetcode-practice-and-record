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

#dp
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                for left in dp[i]:
                    for right in dp[k - 1 - i]:
                        dp[k].append("(" + left + ")" + right)
        return dp[n]
#time complexity: O(4^n / sqrt(n)) where n is the number of pairs of parentheses. 
# The number of valid parentheses combinations is given by the nth Catalan number, which is approximately 4^n / (n^(3/2) * sqrt(pi)). The time complexity is dominated by the number of valid combinations, which is O(4^n / sqrt(n)).
#space complexity: O(n)

#backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
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
#time complexity: O(4^n / sqrt(n)) where n is the number of pairs of parentheses. The number of valid parentheses combinations is given by the nth Catalan number, which is approximately 4^n / (n^(3/2) * sqrt(pi)). The time complexity is dominated by the number of valid combinations, which is O(4^n / sqrt(n)).
#space complexity: O(n) for the recursion stack and the stack list, where n is the number of pairs of parentheses. The result list will take O(4^n / sqrt(n)) space to store all valid combinations, but this is not counted towards the space complexity since it is part of the output.