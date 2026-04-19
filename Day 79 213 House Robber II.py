'''You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [3,4,3]

Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 200'''
from typing import List

#recurisive
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))
        return max(dfs(0, False), dfs(1, False))
#time complexity: O(2^n)
#space complexity: O(n) due to the recursion stack


#dp space optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                new_rob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
#time complexity: O(n) where n is the length of the input array nums
#space complexity: O(1) since we are using only a constant amount of space to store the variables rob1 and rob2