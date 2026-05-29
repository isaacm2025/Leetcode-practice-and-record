'''Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9'''

#bf
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
#time complexity: O(n^2) because of the nested loops
#space complexity: O(1) because we are not using any additional data structures

#sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #sort the array first
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: #if the current element is the same as the previous element, then we have found a duplicate
                return True
        return False #otherswise, we have not found any duplicates
#time complexity: O(n log n) because of the sorting step
#space complexity: O(1) because we are sorting the array in place, O(n) if we consider the space used by the sorting algorithm