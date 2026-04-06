'''You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.'''

#recursive binary search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, r, target)
        return self.binarySearch(nums, l, mid - 1, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
#time complexity: O(logn) where n is the number of elements in the array, we are halving the search space at each step
#space complexity: O(logn) due to the recursive call stack, in the worst case when the target is not found, 
#we will have logn recursive calls on the call stack. In the best case when the target is found at the first mid point, we will have only one recursive call on the call stack, so the space complexity is O(1) in that case. Overall, the space complexity is O(logn) in the worst case.

#iterative binary search
class solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
#time complexity: O(logn) where n is the number of elements in the array, we are halving the search space at each step
#space complexity: O(1) since we are using a constant amount of space to store the left and right pointers and the mid index

#built in binary search
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else - 1
#time complexity: O(logn) where n is the number of elements in the array, the bisect_left function uses binary search to find the insertion point for the target in the sorted array
#space complexity: O(1) since we are using a constant amount of space to store the index returned by the bisect_left function

