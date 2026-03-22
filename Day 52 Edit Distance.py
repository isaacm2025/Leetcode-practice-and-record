'''You are given two strings word1 and word2, each consisting of lowercase English letters.

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position
Return the minimum number of operations to make word1 equal word2.

Example 1:

Input: word1 = "monkeys", word2 = "money"

Output: 2
Explanation:
monkeys -> monkey (remove s)
monkey -> money (remove k)

Example 2:

Input: word1 = "neatcdee", word2 = "neetcode"

Output: 3
Explanation:
neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)

Constraints:

0 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.'''

#recursion
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            res = min(res, dfs(i + 1, j + 1))
            return res + 1
        return dfs(0, 0)

#time complexity: O(3^(m + n))
#space complexity: O(m + n)

#dynamic programming(top down)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp;
                return dp[(i, j)]
            if word1[i] ==[word2][j]:
                dp[(i, j)] = dfs(i + 1, j+ 1)
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                res = min(res, dfs(i + 1, j + 1))
                dp[(i, j)] = res + 1
            return dp[(i, j)]
        return dfs(0, 0)
#time complexity: O(m * n)
#space complexity: O(m * n)

#dp bottom up
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1
        return dp[0][0]
#time complexity: O(m * n)
#space complexity: O(m * n)
