'''You are given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [-2,-1,0]

Output: 1
Example 2:

Input: nums = [1,2,4]

Output: 3
Example 3:

Input: nums = [1,2,4,5,6,3,1]

Output: 7
Constraints:

1 <= nums.length <= 100,000
-(2^31) <= nums[i] <= ((2^31)-1)'''
from typing import List
#brute force
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        while True:
            flag = True
            for num in nums:
                if missing == num:
                    flag = False
                    break
            if flag:
                return missing
            missing += 1
#time complexity: O(n^2)
#space complexity: O(1)

#boolean array
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n
        for num in nums:
            if num > 0 and num <= n:
                seen[num - 1] = True

        for num in range(1, n + 1):
            if not seen[num - 1]:
                return num
        return n + 1
    
#time complexity: O(n)
#space complexity: O(n)

#Algorithm
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
    #time complexity: O(n)
    #space complexity: O(1)

    