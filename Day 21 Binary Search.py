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

#recursive binary search:
from typing import List
class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return - 1
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] > target:
            return self.binary_search(m + 1, r, nums, target) #if the middle element is greater than the target, we need to search in the right half of the array
        return self.binary_search(l, m - 1, nums, target) #if the middle element is less than the target, we need to search in the left half of the array
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target) #call the binary search helper function with the initial left and right pointers set to the start and end of the array, respectively
#time complexity: O(log n) where n is the number of elements in the input array
#space complexity: O(log n) for the recursive call stack

#iterative binary search:
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2) #calculate the middle index to avoid potential overflow issues that can arise with large values of l and r

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                r = m + 1
            else:
                return m
        return -1
#time complexity: O(log n) where n is the number of elements in the input array
#space complexity: O(1)
