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

#dp
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and (i + 1 > (i + l - 2) or dp[i + 1][i + l - 2]))
        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
#time complexity: O(n * 2^n) where n is the length of the string s. The number of possible partitions is 2^(n-1) and checking if each partition is a palindrome takes O(1) time using the dp table.
#space complexity: O(n^2) where n is the length of the string s. 
#The dp table takes O(n^2) space, and the recursion stack can go up to O(n) in the worst case. The space used to store the current partition can also take up to O(n) space in the worst case. The space used to store the final result can also take up to O(n * 2^n) space in the worst case, but it is not counted towards the overall space complexity since it is not part of the recursion stack.

#recursive
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and (i + 1 > (i + l - 2) or dp[i + 1][i + l - 2]))
        def dfs(i):
            if i >= n:
                return [[]]
            res = []
            for j in range(i, n):
                if dp[i][j]:
                    nxt = dfs(j + 1)
                    for part in nxt:
                        cur = [s[i: j + 1]] + part
                        res.append(cur)
            return res
        return dfs(0)
#time complexity: O(n * 2^n) where n is the length of the string s. The number of possible partitions is 2^(n-1) and checking if each partition is a palindrome takes O(1) time using the dp table.
#space complexity: O(n^2) where n is the length of the string s. 
#The dp table takes O(n^2) space, and the recursion stack can go up to O(n) in the worst case. 
#The space used to store the final result can also take up to O(n * 2^n) space in the worst case, but it is not counted towards the overall space