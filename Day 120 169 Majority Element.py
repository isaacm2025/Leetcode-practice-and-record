'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5
Example 2:

Input: nums = [2,2,2]

Output: 2
Constraints:

1 <= nums.length <= 50,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
Follow-up: Could you solve the problem in linear time and in O(1) space?'''

#bf
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n // 2:
                return num
#time complexity: O(n^2) because we are iterating through the input list nums and counting the occurrences of each element, which takes O(n) time for each element
#space complexity: O(1) because we are using a constant amount of space to store the loop variables

#sorting
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
#time complexity: O(n log n) because we are sorting the input list nums, which takes O(n log n) time
#space complexity: O(1) because we are sorting the input list nums in place and using a constant amount of space to store the return value