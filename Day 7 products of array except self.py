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
-20 <= nums[i] <= 20'''

#brute force solution
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # length of input array
        res = [0] * n # result array
        for i in range(n): # iterate through input array
            prod = 1 # product variable
            for j in range(n): # iterate through input array
                if i ==j: # skip the current index
                    continue # skip
                prod *= nums[j] # multiply
            res[i] = prod # assign product to result
        return res # return result
#time complexity: O(N^2)
#space complexity: O(1) extra space, O(n) space foor output array

#optimal solution
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # result array initialized to 1
        prefix = 1 # prefix product
        for i in range(len(nums)): # iterate through input array
            res[i] = prefix # assign prefix product to result
            prefix *= nums[i] # update prefix product
        postfix = 1 # postfix product
        for i in range(len(nums) -1, -1, -1): # iterate through input array in reverse
            res[i] *= postfix # multiply postfix product to result
            postfix *= nums[i] # update postfix product
        return res # return result
#time complexity: O(n)
#space complexity: O(1) extra space, O(n) space for output array