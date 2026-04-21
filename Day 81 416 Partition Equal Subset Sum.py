'''You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 50'''

from typing import List
#recursive solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])
        return dfs(0, sum(nums) // 2)
#time complexity: O(2^n) where n is the length of the input array
#space complexity: O(n) where n is the length of the input array due to the recursive call stack


#dp
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
#time complexity: O(n * target) where n is the length of the input array and target is the sum of the input array divided by 2
#space complexity: O(target) where target is the sum of the input array divided by 2 due to the dp set storing all possible sums up to the target