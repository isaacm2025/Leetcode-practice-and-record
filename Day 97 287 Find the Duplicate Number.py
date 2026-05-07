'''You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O
(
1
)
O(1) extra space?

Constraints:

1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n'''

from ast import List
#sorting

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1
#time complexity: O(n log n) due to the sorting step.
#space complexity: O(1) if we ignore the space used by the sorting algorithm, otherwise O(n) if the sorting algorithm used is not in-place.

#hash set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
#time complexity: O(n) because we traverse the array once.
#space complexity: O(n) in the worst case, when all numbers are distinct except for one duplicate, which would require storing n - 1 unique numbers in the set.

#Negative marking
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        return -1
#time complexity: O(n) because we traverse the array once.
#space complexity: O(1) because we are modifying the input array in place and not using any additional data structures.

#bit manipulation
class Solution:
    def findDUplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = 0
        for b in range(32):
            x = y = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1
            for num in range(1, n):
                if num & mask:
                    y += 1
            if x > y:
                res |= mask
        return res
#time complexity: O(32 * n) because we traverse the array a constant number of times (32 times for the bit manipulation).
#space complexity: O(1) because we are using a constant amount of extra space to store the result and the counters for the bits.