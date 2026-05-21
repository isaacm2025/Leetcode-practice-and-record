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

#recursion
from ast import List
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
#time complexity: O(2^n)
#space complexity: O(n)


#dp top down
from ast import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]
        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))
            return memo[i][target]
        return dfs(0, target)
#time complexity: O(n*target)
#space complexity: O(n*target)