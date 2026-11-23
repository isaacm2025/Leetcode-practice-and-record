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
        memo = [[None] * n for _ in range(n + 1)]
        def dfs(i, j):
            if j < 0:
                return False
            if i == n:
                return j == 0
            if memo[i][j] is not None:
                return memo[i][j]
            if s[i] == '(':
                result = dfs(i + 1, j + 1)
            elif s[i] == ')':
                result = dfs(i + 1, j - 1)
            else:
                result = dfs(i + 1, j) or dfs(i + 1, j + 1) or dfs(i + 1, j - 1)
            memo[i][j] = result
            return result
        return dfs(0, 0)
#time complexity: O(n^2)
#space complexity: O(n^2)

#stack
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left
#time complexity: O(n)
#space complexity: O(n)