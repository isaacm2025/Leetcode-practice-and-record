'''Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:

Input: nums = [-1]

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
'''

from typing import List
#bf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        return res
#time complexity: O(n^2)
#space complexity: O(1)

#dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[n - 1][1] = dp[n - 1][0] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1])
            dp[i][0] = max(dp[i + 1][0], dp[i][1])
        return dp[0][0]
#time complexity: O(n)
#space complexity: O(n)

#dp optimal
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)
#time complexity: O(n)
#space complexity: O(n)