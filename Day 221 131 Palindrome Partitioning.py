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
s contains only lowercase English letters.'''

#dp
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                dp[j][j + i - 1] = (s[j] == s[j + i - 1] and (j + 1 > (j + i - 2) or dp[j + 1][j + i - 2]))
        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
#time complexity: O(n * 2^n) because we have to explore all possible partitions and for each partition we have to check if it is a palindrome
#space complexity: O(n) for the recursion stack and the dp array