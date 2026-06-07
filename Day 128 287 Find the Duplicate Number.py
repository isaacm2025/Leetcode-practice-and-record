'''You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every other integer appears at most once.

Return the repeated integer.

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
1 <= nums[i] <= n
'''

#sorting
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1
#time complexity: O(nlogn)
#space complexity: O(1)

#hashset
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
#time complexity: O(n)
#space complexity: O(n)

#array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)
        for num in nums:
            if seen[num] == 1:
                return num
            seen[num - 1] = 1
        return -1
#time complexity: O(n)
#space complexity: O(n)

#bs
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        low, high = 1, n - 1
        while low < high:
            mid = low + (high - low) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)
            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid
        return low
#time complexity: O(nlogn)
#space complexity: O(1)