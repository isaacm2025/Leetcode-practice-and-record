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
word1 and word2 consist of lowercase English letters.
'''

#dp space optimized
from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = [0] * (n + 1)
        nextDp = [0] * (n+1)
        for j in range(n + 1):
            dp[j] = n - j
        for i in range(m - 1, -1, -1):
            nextDp[n] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    nextDp[j] = dp[j + 1]
                else:
                    nextDp[j] = 1 + min(dp[j], nextDp[j + 1], dp[j + 1])
            dp = nextDp[:]
        return dp[0]
#time complexity: O(m*n) where m and n are the lengths of word1 and word2, respectively. 
# The algorithm iterates through each character of both strings, resulting in a time complexity of O(m*n).
#space complexity: O(n) where n is the length of the shorter string (after the optimization). 
# The space complexity is reduced to O(n) because we only need to store the current and next row of the DP table, which has a length of n (the length of the shorter string).

#dp optimal
from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = [n - i for i in range(n + 1)]
        for i in range(m - 1, -1, -1):
            nextDp = dp[n]
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = nextDp
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], nextDp)
                nextDp = temp
        return dp[0]
#time complexity: O(m*n) where m and n are the lengths of word1 and word2, respectively. 
# The algorithm iterates through each character of both strings, resulting in a time complexity of O(m*n).
#space complexity: O(n) where n is the length of the shorter string (after the optimization). 
# The space complexity is reduced to O(n) because we only need to store the current row of the DP table, which has a length of n (the length of the shorter string).