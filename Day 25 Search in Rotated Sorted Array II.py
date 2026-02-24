'''You are given an array of length n which was originally sorted in non-decreasing order (not necessarily with distinct values). It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return true if target is in nums, or false if it is not present.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [3,4,4,5,6,1,2,2], target = 1

Output: true
Example 2:

Input: nums = [3,5,6,0,0,1,2], target = 4

Output: false
Constraints:

1 <= nums.length <= 5000
-10,000 <= target, nums[i] <= 10,000
nums is guaranteed to be rotated at some pivot.'''


from typing import List
#brute force
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
#time complexity: O(n) where n is the length of the input list
#space complexity: O(1) since we are not using any additional data structures

#binary search
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2 #calculate the middle index
            if nums[mid] == target: #if the middle element is the target, return True
                return True
            if nums[left] == nums[mid] == nums[right]: #if the left, mid, and right elements are the same, we cannot determine which side is sorted, so we can only move the left and right pointers inward
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]: #if the left side is sorted
                if nums[left] <= target < nums[mid]: #if the target is in the left side, we can move the right pointer to mid - 1
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: #if the target is in the right side, we can move the left pointer to mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
        return False
#time complexity: O(log n) in the average case, but O(n) in the worst case when there are many duplicates
#space complexity: O(1) since we are not using any additional data structures