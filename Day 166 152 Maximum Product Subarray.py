'''Given an integer array nums, find a subarray that has the largest product, and return the product.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

Example 1:

Input: nums = [2,4,-3,5]

Output: 8
Explanation: [2,4] has the largest product 8.


Example 2:

Input: nums = [-3,0,-2]

Output: 0
Explanation: The result cannot be 6, because [-3,-2] is not a subarray.


Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''

#bf
from typing import List

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

#kadane's algorithm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
#time complexity: O(n)
#space complexity: O(1)