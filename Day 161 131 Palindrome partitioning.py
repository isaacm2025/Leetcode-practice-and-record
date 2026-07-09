'''Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"

Output: [["a"]]
Constraints:

1 <= s.length <= 20
s contains only lowercase English letters.
'''

#dp
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and (i + 1 > (i + l - 2)or dp[i + 1][i + l - 2]))
        res, path= [], []
        def dfs(i):
            if i>= len(s):
                res.append(path.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return res
