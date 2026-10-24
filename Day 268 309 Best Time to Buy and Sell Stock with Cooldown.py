'''You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

Example 1:

Input: prices = [1,3,4,0,4]

Output: 6
Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

Example 2:

Input: prices = [1]

Output: 0
Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000'''

#recursive
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                return max(sell, cooldown)
        return dfs(0, True)
#time complexity: O(2^n) where n is the length of prices. In the worst case, we have two choices at each step, leading to an exponential number of recursive calls.
#space complexity: O(n) for the recursion stack, where n is the length of prices

#dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)
#time complexity: O(n) where n is the length of prices. Each state (i, buying) is computed at most once and stored in the dp dictionary.
#space complexity: O(n) for the dp dictionary and the recursion stack, where n is the length of prices. In the worst case, the maximum depth of the recursion tree can be n.

#sp op
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1Buy, dp1Sell, dp2Buy = 0, 0, 0
        for i in range(n - 1, -1, -1):
            dpBuy = max(dp1Sell - prices[i], dp1Buy)
            dpSell = max(dp2Buy + prices[i], dp1Sell)
            dp2Buy = dp1Buy
            dp1Buy, dp1Sell = dpBuy, dpSell
        return dp1Buy
#time complexity: O(n) where n is the length of prices. We iterate through the prices array once, performing constant time operations for each element.
#space complexity: O(1)