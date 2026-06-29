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

#bf
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            res[i] = product
        return res
#time complexity: O(n^2) where n is the length of the input array.
#space complexity: O(n) where n is the length of the input array, O(1) extra space is used for the product variable.s


#division
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeroCount = 1, 0
        for num in nums:
            if num:
                product *= num
            else:
                zeroCount += 1
        if zeroCount > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zeroCount:
                res[i] = 0 if c else product
            else:
                res[i] = product // c
        return res
#time complexity: O(n) where n is the length of the input array.
#space complexity: O(n) where n is the length of the input array, O(1) extra space is used for the product and zeroCount variables.