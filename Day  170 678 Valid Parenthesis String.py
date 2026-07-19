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

#dp
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n -1, -1, -1):
            newDp = [False] * (n + 1)
            for open in range(n):
                if s[i] == '*':
                    newDp[open] = dp[open + 1] or open > 0 and dp[open - 1] or dp[open]
                elif s[i] == '(':
                    newDp[open] = dp[open + 1]
                elif open > 0:
                    newDp[open] = dp[open - 1]
            dp = newDp
        return dp[0]
#time complexity: O(n^2)
#space complexity: O(n)

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