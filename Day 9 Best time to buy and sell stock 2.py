'''You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same day. Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]

Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]

Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

Constraints:

1 <= prices.length <= 30,000
0 <= prices[i] <= 10,000
'''

from typing import List

#recursion

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def rec(i, bought):
            if i == len(prices):
                return 0 
            res = rec(i + 1, bought)
            if bought:
                res = max(res, prices[i] + rec(i + 1, False))
            else:
                res = max(res, -prices[i] + rec(i + 1, True))
            return res
        return rec(0, False)
#Time complexity: O(2^n)
#Space complexity: O(n)

#Dynamic programming (top-down)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def rec(i, bought):
            if i == len(prices):
                return 0 
            if (i,  bought) in dp:
                return dp[(i, bought)]
            res = rec(i + 1, bought)
            if bought:
                res = max(res, prices[i] + rec(i + 1, False))
            else:
                res = max(res, -prices[i] + rec(i + 1, True))
            dp[(i, bought)] = res
            return res
        return rec(0, False)
    
    #time complexity: O(n)
    #space complexity: O(n)

#Dynamic programming(bottom-up)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            dp[i][1] = max(dp[i + 1[1], prices[i] + dp[i+1][0]])

        return dp[0][0]
#time complexity: O(n)
#space complexity: O(n)

#greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i -1])
                profit += (prices[i] - prices[i -1])
        
        return profit
#time complexity: O(n)
#space complexity: O(1)

