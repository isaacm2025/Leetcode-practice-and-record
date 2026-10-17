'''You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7
'''

#dp
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n + 1)]
        res[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k - i - 1]:
                        res[k].append("(" + left + ")" + right)
        return res[n]
#time complexity: O(4^n / sqrt(n)), where n is the number of pairs of parentheses
#space complexity: O(4^n / sqrt(n)), where n is the number of pairs of parentheses