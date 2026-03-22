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


from typing import List
#recursion
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        def dfs(i, j):
            if len(nums) == 2:
                return 0
            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(i - 1, i + 1)
                maxCoins = max(maxCoins, coins)
            return maxCoins
        return dfs(nums)

#time complexity: O(n * 2^n)
#space complexity: O(n)

#dynamic programming(top down)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            maxCoins = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                maxCoins = max(maxCoins, coins)
            dp[(l, r)] = maxCoins
            return maxCoins
        return dfs(1, len(nums) - 2)

#time complexity: O(n^3)
#space complexity: O(n^2)

