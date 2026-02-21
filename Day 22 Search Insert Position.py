'''You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 5

Output: 4
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 10

Output: 6
Constraints:

1 <= nums.length <= 10,000.
-10,000 < nums[i], target < 10,000
nums contains distinct values sorted in ascending order.
'''
#linear search
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): #iterate through the list
            if nums[i] >= target: #if the current number is greater than or equal to the target, return the index
                return i #if the target is greater than all numbers in the list, return the length of the list
        return len(nums) #if the target is greater than all numbers in the list, return the length of the list

#time complexity: O(n)
#space complexity: O(1)

#binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums) #initialize the result to the length of the list, which is the index where the target would be inserted if it is greater than all numbers in the list
        left, right = 0, len(nums) - 1 #initialize the left and right pointers
        while left <= right: #while the left pointer is less than or equal to the right pointer
            mid = (left + right) // 2 #calculate the middle index
            if nums[mid] == target: #if the middle number is equal to the target, return the middle index
                return mid #if the middle number is greater than the target, update the result to the middle index and move the right pointer to the left of the middle index
            if nums[mid] > target: #if the middle number is greater than the target, update the result to the middle index and move the right pointer to the left of the middle index
                res = mid #update the result to the middle index
                right = mid - 1 #move the right pointer to the left of the middle index
            else:
                left = mid + 1 #move the left pointer to the right of the middle index
        return res
#time complexity: O(log n)
#space complexity: O(1)