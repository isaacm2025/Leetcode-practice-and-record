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
#backtracking
from ast import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
#time complexity: O(n*2^n) where n is the length of the string s. This is because there are 2^(n-1) ways to partition a string of length n, and checking if each partition is a palindrome takes O(n) time in the worst case.
#space complexity: O(n) for the recursion stack and the space used to store the current partition. 
#The total space complexity can be O(n) in the worst case when all characters are the same, resulting in a single partition of the entire string.