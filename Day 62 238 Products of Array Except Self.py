'''Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''
from typing import List
#brute force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res
#time complexity is O(n^2) and space complexity is O(n)

#division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res
#time complexity is O(n) and space complexity is O(n), O(1) if we don't count the output array.

#prefix and suffix optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
#time complexity is O(n) and space complexity is O(n), O(1) if we don't count the output array.


