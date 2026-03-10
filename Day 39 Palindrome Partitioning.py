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

from typing import List
#backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
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
#time complexity: O(n*2^n) where n is the length of the string. In the worst case, we have to check all possible partitions of the string, which is 2^(n-1). For each partition, we check if each substring is a palindrome, which takes O(n) time.
#space complexity: O(n) for the recursion stack and the temporary list used to store the current partition. The output list can also take up to O(n*2^n) space in the worst case, if all partitions are palindromic.
