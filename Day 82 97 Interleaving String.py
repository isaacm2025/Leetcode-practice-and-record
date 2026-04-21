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

#recursive solution
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
#time complexity: O(2^(m+n)) where m and n are the lengths of s1 and s2 respectively. In the worst case, we may have to explore all possible interleavings of s1 and s2 to check if they match s3.
#space complexity: O(m+n) due to the recursive call stack. In the worst case, the depth of the recursion can go up to m+n when we have to explore all characters of s1 and s2.

#dp optimal
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m +n != len(s3):
            return False
        if n < m:
            s1, s2, = s2, s1
            m, n = n, m
        dp = [False for _ in range(n+1)]
        dp[n] = True
        for i in range(m, -1, -1):
            nextDP = True if i == m else False
            for j in range(n, -1, -1):
                res = False if j < n else nextDP
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    res = True
                if j < n and s2[j] == s3[i + j] and nextDP:
                    res = True
                dp[j] = res
                nextDP = res
        return dp[0]
#time complexity: O(m*n) where m and n are the lengths of s1 and s2 respectively. We need to fill a 2D table of size (m+1) x (n+1) to determine if s3 can be formed by interleaving s1 and s2.
#space complexity: O(n) where n is the length of s2. We can optimize the space complexity to O(n) by using a 1D array instead of a 2D table, since the value of dp[i][j] only depends on the previous row (i-1) and the current row (i).
