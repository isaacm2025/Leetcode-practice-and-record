'''You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

Return the maximum number of coins you can receive by bursting all of the balloons.

Example 1:

Input: nums = [4,2,3,7]

Output: 143

Explanation:
nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143
Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''

#dp
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        newNums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = newNums[l - 1] * newNums[i] * newNums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]
#time complexity: O(n^3) where n is the length of the input array nums. 
# The three nested loops each iterate up to n times, resulting in a cubic time complexity.
#space complexity: O(n^2) where n is the length of the input array nums. 
# The dp table is a 2D array of size (n+2) x (n+2), which requires O(n^2) space to store the maximum coins for each subproblem.