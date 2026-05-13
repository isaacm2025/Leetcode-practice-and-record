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

#backtracking
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            if self.isPalindrome(s, j, i):
                part.append(s[j: i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            dfs(j, i + 1)
        dfs(0, 0)
        return res
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, rr = l + 1, r - 1
        return True
#time complexity: O(n * 2^n) where n is the length of the string s. The number of possible partitions is 2^(n-1) and checking if each partition is a palindrome takes O(n) time.
#space complexity: O(n) where n is the length of the string s. 
# The recursion stack can go up to O(n) in the worst case, and the space used to store the current partition can also take up to O(n) space in the worst case. The space used to store the final result can also take up to O(n * 2^n) space in the worst case, but it is not counted towards the overall space complexity since it is not part of the recursion stack.