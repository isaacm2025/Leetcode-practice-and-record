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

1 <= s.length <= 100'''

#recursion
class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0
            if s[i] == '(':
                return dfs(i + 1, open + 1)
            elif s[i] == ')':
                return dfs(i + 1, open - 1)
            else:
                return dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)
        return dfs(0, 0)
#time complexity: O(3^n) where n is the length of string s
#space complexity: O(n) where n is the length of string s

#dp top down
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[None] * (n + 1) for _ in range(n + 1)]
        def dfs(i, open):
            if open < 0:
                return False
            if i == n:
                return open == 0
            if memo[i][open] is not None:
                return memo[i][open]
            if s[i] == '(':
                memo[i][open] = dfs(i + 1, open + 1)
            elif s[i] == ')':
                memo[i][open] = dfs(i + 1, open - 1)
            else:
                memo[i][open] = dfs(i + 1, open + 1) or dfs(i + 1, open - 1) or dfs(i + 1, open)
            return memo[i][open]
        return dfs(0, 0)
#time complexity: O(n^2) where n is the length of string s
#space complexity: O(n^2) where n is the length of string s
                