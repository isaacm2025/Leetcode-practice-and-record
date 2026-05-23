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
-1000 <= nums[i] <= 1000'''

#bf
from ast import List
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

#recursion
from ast import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(i, flag):
            if i == len(nums) - 1:
                return max(0, nums[i]) if flag else nums[i]
            if flag:
                return max(0, nums[i] + dfs(i + 1, True))
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
        return dfs(0, False)
#time complexity: O(2^n)
#space complexity: O(n)