'''You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

Every left parenthesis '(' must have a corresponding right parenthesis ')'.
Every right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
Example 1:

Input: s = "((**)"

Output: true
Explanation: One of the '*' could be a ')' and the other could be an empty string.

Example 2:

Input: s = "(((*)"

Output: false
Explanation: The string is not valid because there is an extra '(' at the beginning, regardless of the extra '*'.

Constraints:

1 <= s.length <= 100
'''

#dp
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo= [[None] * (n + 1) for _ in range(n + 1)]
        def dfs(i, open):
            if open <0:
                return False
            if i == n:
                return open == 0
            if memo[i][open] is not None:
                return memo[i][open]
            if s[i] == '(':
                result = dfs(i + 1, open + 1)
            elif s[i] == ')':
                result = dfs(i + 1, open - 1)
            else:
                result = dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)
            memo[i][open] = result
            return result
        return dfs(0, 0)
#time complexity: O(n^2)
#space complexity: O(n^2)

#dp sp op
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n -1, -1, -1):
            newDp = [False] * (n + 1)
            for open in range(n):
                if s[i] == '*':
                    newDp[open] = (dp[open + 1] or (open > 0 and dp[open - 1]) or dp[open])
                elif s[i] == '(':
                    newDp[open] = dp[open + 1]
                elif open > 0:
                    newDp[open] = dp[open - 1]
            dp = newDp
        return dp[0]
#time complexity: O(n^2)
#space complexity: O(n)

#greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
#time complexity: O(n)
#space complexity: O(1)