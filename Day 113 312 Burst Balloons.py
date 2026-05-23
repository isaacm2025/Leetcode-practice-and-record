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
0 <= nums[i] <= 100'''

#bf, recursion
from ast import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        def dfs(nums):
            if len(nums) == 2:
                return 0
            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(nums[:i] + nums[i + 1:])
                maxCoins = max(maxCoins, coins)
            return maxCoins
        return dfs(nums)
#time complexity: O(n * 2^n)
#space complexity: O(n * 2^n)


#dp, top-down
from ast import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            dp[(left, right)] = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                dp[(left, right)] = max(dp[(left, right)], coins)
            return dp[(left, right)]
        return dfs(1, len(nums) - 2)
#time complexity: O(n^3)
#space complexity: O(n^2)