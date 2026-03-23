'''You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

Return true if the pattern matches the entire input string, otherwise return false.

'.' Matches any single character
'*' Matches zero or more of the preceding element.
Example 1:

Input: s = "aa", p = ".b"

Output: false
Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.

Example 2:

Input: s = "nnn", p = "n*"

Output: true
Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.

Example 3:

Input: s = "xyz", p = ".*z"

Output: true
Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
Each appearance of '*', will be preceded by a valid character or '.'.'''

#recursion
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        def dfs(i, j):
            if j == n:
                return i == m
            match = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j + 1] == '*':
                return (dfs(i, j + 2) or match and dfs(i + 1, j))
            if match:
                return dfs(i + 1, j + 1)
            return False
        return dfs(0, 0)
#time complexity: O(2^(m + n))
#space complexity: O(m + n)

#dp (top down)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}
        def dfs(i, j):
            if j == n:
                return i == m
            if (i, j) in cache:
                return cache[(i, j)]
            match = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j + 1] == '*':
                cache[(i, j)] = (dfs(i, j + 2) or match and dfs(i + 1, j))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False
        return dfs(0, 0)
#time complexity: O(m * n)
#space complexity: O(m * n)


#space optimization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True
        for i in range(len(s), -1, -1):
            nextDp = [False] * (len(p) + 1)
            nextDp[len(p)] = (i == len(s))
            for j in range(len(p) -1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if (j + 1) < len(p) and p[j + 1] == '*':
                    nextDp[j] = nextDp[j + 2]
                    if match:
                        nextDp[j] = nextDp[j] or dp[j]
                elif match:
                    nextDp[j] = dp[j + 1]
            dp = nextDp
        return dp[0]
#time complexity: O(m * n)
#space complexity: O(n)
                    