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
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True
        for i in range(n - 1, -1, -1):
            for open in range(n):
                res = False
                if s[i] == '*':
                    res |= dp[i + 1][open + 1]
                    if open > 0:
                        res |= dp[i + 1][open - 1]
                    res |= dp[i + 1][open]
                else:
                    if s[i] == '(':
                        res |= dp[i + 1][open + 1]
                    elif open > 0:
                        res |= dp[i + 1][open -1]
                dp[i][open] = res
        return dp[0][0]
#time complexity: O(n^2) where n is the length of s.
#space complexity: O(n^2) because we use a 2D dp array of size n x n.

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
#time complexity: O(n) where n is the length of s.
#space complexity: O(n) because we use two stacks to store the indices of '(' and '*' characters.