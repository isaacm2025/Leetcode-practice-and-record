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
s and t consist of English letters.'''

#recursion with memoization
from typing import List
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
#time complexity: O(2^m) where m is the length of string s. In the worst case, the function explores all possible subsequences of s, which can lead to an exponential number of calls.
#space complexity: O(m + n) where m is the length of string s and n is the length of string t. The maximum depth of the recursion can be m (when we explore all characters of s) and we also need space for the call stack, which can grow up to O(m) in the worst case. 
#Additionally, we may have O(n) space for the call stack when we explore all characters of t. Therefore, the overall space complexity is O(m + n).

#dp
from typing import List
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]
#time complexity: O(m*n) where m is the length of string s and n is the length of string t. We fill a 2D dp array of size (m+1) x (n+1), and each cell is computed in constant time.
#space complexity: O(m*n) where m is the length of string s and n is the length of string t. We use a 2D dp array of size (m+1) x (n+1) to store the number of distinct subsequences for each substring of s and t.

#dp optimized
from typing import List
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
#time complexity: O(m*n) where m is the length of string s and n is the length of string t. We fill a 1D dp array of size (n+1), and each cell is computed in constant time.
#space complexity: O(n) where n is the length of string t. 
# We use a 1D dp array of size (n+1) to store the number of distinct subsequences for each substring of t. The space complexity is reduced from O(m*n) to O(n) by only keeping track of the current and previous row of the dp array.