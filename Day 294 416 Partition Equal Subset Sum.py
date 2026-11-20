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

#dp
from typing import List
class Solution:
    def canpartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2. != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]
#time complexity: O(n * target)
#space complexity: O(n * target)

#hashset
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) -1, -1, -1):
            nextDp = set()
            for j in dp:
                if j + nums[i] == target:
                    return True
                nextDp.add(j)
                nextDp.add(j + nums[i])
            dp = nextDp
        return False
#time complexity: O(n * target)
#space complexity: O(target)