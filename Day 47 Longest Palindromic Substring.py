'''Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.'''

#brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r and j - i + 1 > resLen:
                    res = s[i:j + 1]
                    resLen = j - i + 1
        return res
#time complexity: O(n^3)
#space complexity: O(n)

#dynamic programming
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        res = i
                        resLen = j - i + 1
        return s[res:res + resLen]
#time complexity: O(n^2)
#space complexity: O(n^2)