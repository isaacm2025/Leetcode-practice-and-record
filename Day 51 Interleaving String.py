'''You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

|n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
You may assume that s1, s2 and s3 consist of lowercase English letters.

Example 1:



Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

Output: true
Explanation: We can split s1 into ["aa", "aa"], s2 can remain as "bbbb" and s3 is formed by interleaving ["aa", "aa"] and "bbbb".

Example 2:

Input: s1 = "", s2 = "", s3 = ""

Output: true
Example 3:

Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"

Output: false
Explanation: We can't split s3 into ["ab", "xz", "cy"] as the order of characters is not maintained.

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200'''

#recursion
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1) and j == len(s2))
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True
            return False
        return dfs(0, 0, 0)
#time complexity: O(2^(m+n)) where m and n are the lengths of s1 and s2
#space complexity: O(m+n) for the recursion stack

#dp (top-down)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1) and (j == len(s2)))
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            dp[(i, j)] = res
            return res
        return dfs(0, 0, 0)
#time complexity: O(m*n) where m and n are the lengths of s1 and s2
#space complexity: O(m*n) for the dp dictionary

#dp (bottom-up)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
#time complexity: O(m*n) where m and n are the lengths of s1 and s2
#space complexity: O(m*n) for the dp table

#dp (optimized space)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(m, -1, -1):
            next_dp = [False for _ in range(n + 1)]
            if i == m:
                next_dp[n] = True
            for j in range(n, -1, -1):
                if i < len(s1) and s1[i] == s3[i + j]:
                    next_dp[j] = dp[j]
                if j < len(s2) and s2[j] == s3[i + j]:
                    next_dp[j] = next_dp[j] or next_dp[j + 1]
            dp = next_dp
        return dp[0]
#time complexity: O(m*n) where m and n are the lengths of s1 and s2
#space complexity: O(n) for the dp array