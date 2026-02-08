'''Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false'''

from typing import List

#brute force
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
#time complexity: O(n^2)
#space complexiity: O(1)

#Sorting
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
#time complexity: O(n log n)
#space complexity: O(1) or O(n) depending on the sorting algorithm

#Hash set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#time complexity: O(n)
#space complexity: O(n)

#Hash set length
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len (nums)
    
#time complexity: O(n)
#space complexity: O(n)