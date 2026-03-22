'''You are given two strings s and t, both consisting of english letters.

Return the number of distinct subsequences of s which are equal to t.

Example 1:

Input: s = "caaat", t = "cat"

Output: 3
Explanation: There are 3 ways you can generate "cat" from s.

(c)aa(at)
(c)a(a)a(t)
(ca)aa(t)
Example 2:

Input: s = "xxyxy", t = "xy"

Output: 5
Explanation: There are 5 ways you can generate "xy" from s.

(x)x(y)xy
(x)xyx(y)
x(x)(y)xy
x(x)yx(y)
xxy(x)(y)
Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''

#recursion
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            return res
        return dfs(0, 0)
#time complexity: O(2^(m)) where m is the length of s
#space complexity: O(m) for the recursion stack

#dp (top-down)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return res
        return dfs(0, 0)
#time complexity: O(m*n) where m and n are the lengths of s and t
#space complexity: O(m*n) for the dp dictionary

#dp (bottom-up)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    dp[i][j] = dp[i + 1][j]
                    if s[i] == t[j]:
                        dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]
#time complexity: O(m*n) where m and n are the lengths of s and t
#space complexity: O(m*n) for the dp table

#dp (optimized space)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        next_dp = [0] * (n + 1)
        dp[n] = next_dp[n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                next_dp[j] = dp[j]
                if s[i] == t[j]:
                    next_dp[j] += dp[j + 1]
            dp = next_dp[:]
        return dp[0]
#time complexity: O(m*n) where m and n are the lengths of s and t
#space complexity: O(n) for the dp arrays

#dp optimal
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev
                prev = dp[j]
                dp[j] = res
        return dp[0]
#time complexity: O(m*n) where m and n are the lengths of s and t
#space complexity: O(n) for the dp array



