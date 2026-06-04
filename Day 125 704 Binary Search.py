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
All the integers in nums are unique.
'''

#recursive bs
from typing import List
class Solution:
    def BS(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.BS(mid + 1, r, nums, target)
        return self.BS(l, mid - 1, nums, target)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.BS(0, len(nums) - 1, nums, target)
#time O(logn) because we are halving the search space at each step
#space O(logn) because of the recursive call stack

#iterative bs
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
#time O(logn) because we are halving the search space at each step
#space O(1) because we are using constant space for the pointers and variables