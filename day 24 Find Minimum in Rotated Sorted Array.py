'''You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
'''

from typing import List

#brute force:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
#time complexity: O(n) where n is the number of elements in the nums array
#space complexity: O(1)

#binary search:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1 #the minimum element must be in the left half of the array, which means we can ignore the right half of the array, and we can continue to search for the minimum element in the left half of the array until we find it
        while left <= right:
            if nums[left] < nums[right]: #if the left element is less than the right element, it means that the minimum element is in the left half of the array, which means we can ignore the right half of the array, and we can continue to search for the minimum element in the left half of the array until we find it
                res = min(res, nums[left]) #update the result with the minimum element in the left half of the array, which is the left element, and we can return the result because we have found the minimum element in the array
                break #break the loop because we have found the minimum element in the array
            mid = (left + right) // 2 #calculate the middle index of the array, which is the index of the middle element in the array
            res = min(res, nums[mid]) #update the result with the minimum element in the left half of the array, which is the middle element, and we can continue to search for the minimum element in the left half of the array until we find it
            if nums[mid] >= nums[left]: #if the middle element is greater than or equal to the left element, it means that the minimum element is in the right half of the array, which means we can ignore the left half of the array, and we can continue to search for the minimum element in the right half of the array until we find it
                left = mid + 1
            else:
                right = mid - 1
        return res
#time complexity: O(log n) where n is the number of elements in the nums array
#space complexity: O(1)

#binary search with a different approach:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 #the minimum element must be in the left half of the array, which means we can ignore the right half of the array, and we can continue to search for the minimum element in the left half of the array until we find it
        while left < right:
            mid = left + (right - left) // 2 #calculate the middle index of the array, which is the index of the middle element in the array
            if nums[mid] > nums[right]: #if the middle element is greater than the right element, it means that the minimum element is in the right half of the array, which means we can ignore the left half of the array, and we can continue to search for the minimum element in the right half of the array until we find it
                right = mid
            else:
                left = mid + 1
        return nums[left]
#time complexity: O(log n) where n is the number of elements in the nums array
#space complexity: O(1)