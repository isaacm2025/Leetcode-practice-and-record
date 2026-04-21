'''You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

Example 1:

Input: amount = 4, coins = [1,2,3]

Output: 4
Explanation:

1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4
Example 2:

Input: amount = 7, coins = [2,4]

Output: 0
Constraints:

1 <= coins.length <= 100
1 <= coins[i] <= 5000
0 <= amount <= 5000
'''

#recursion
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])
            return res
        return dfs(0, amount)
#time complexity: O(2^(max(n, a/m)) where n is the number of coins, a is the amount and m is the smallest coin denomination
#space complexity: O(max(n, a/m)) where n is the number of coins, a is the amount and m is the smallest coin denomination

#dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]
#time complexity: O(n * a) where n is the number of coins and a is the amount
#space complexity: O(n * a) where n is the number of coins and a is the amount

#space optimized dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
#time complexity: O(n * a) where n is the number of coins and a is the amount
#space complexity: O(a) where a is the amount
    