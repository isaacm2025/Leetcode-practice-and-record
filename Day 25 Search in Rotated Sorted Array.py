'''You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
All values of nums are unique.
nums is an ascending array that is possibly rotated.'''


from typing import List
#brute force
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): #iterate through the list
            if nums[i] == target: #if the target is found,
                return i #return the index
        return -1 # if the target is not found, return -1
#time complexity: O(n) where n is the length of the input list
#space complexity: O(1) since we are not using any additional data structures

#binary search (two pass)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left, right = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
#time complexity: O(log n) where n is the length of the input list
#space complexity: O(1) since we are not using any additional data structures

#binary search (one pass)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #initialize the left and right pointers to the start and end of the list, respectively
        while left <= right:
            mid = (left + right) // 2 #calculate the middle index
            if target == nums[mid]: #if the target is found,
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]: #if the target is in the left half of the array,
                    right = mid - 1 #if the target is in the left half of the array, we move the right pointer to mid - 1 to search for the target in the left half
                else:
                    left = mid + 1 #if the target is not in the left half of the array, it must be in the right half, so we move the left pointer to mid + 1
            else:
                if target > nums[mid] and target <= nums[right]: #if the target is in the right half of the array,
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 #if the target is not found, return -1
#time complexity: O(log n) where n is the length of the input list
#space complexity: O(1) since we are not using any additional data structures
    
