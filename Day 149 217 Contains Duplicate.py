'''Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

#bf
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
#time complexity: O(n^2)
#space complexity: O(1)

#sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
#time complexity: O(nlogn) n because of sorting, logn because of the sort function, sorting function is O(nlogn) because it uses Timsort algorithm
#space complexity: O(1)

#hashset
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # create a set to store the seen numbers becausse set has O(1) time complexity for lookups
        for num in nums:
            if num in seen:
                return True # if the number is already in the set, it means we have found a duplicate
            seen.add(num) # add the number to the set
        return False # if we have gone through the entire array and found no duplicates, return False
#time complexity: O(n) because we are going through the entire array once
#space complexity: O(n) because we are storing the seen numbers in a set, which can take up to O(n) space in the worst case if all numbers are unique