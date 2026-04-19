'''Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:

Input: nums = [1,2,-3,4]

Output: 4
Example 2:

Input: nums = [-2,-1]

Output: 2
Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10'''

from typing import List
#bf
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
        return res
#time complexity: O(n^2)
#space complexity: O(1)