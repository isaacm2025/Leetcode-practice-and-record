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
#time complexity:O(nlogn) due to the sorting step, where n is the length of the input array nums.
#space complexity:O(1) if we ignore the space used by the sorting algorithm, otherwise O(n) if the sorting algorithm used is not in-place.

#hash set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
#time complexity:O(n) where n is the length of the input array nums, because we need to iterate through the array once.
#space complexity:O(n) in the worst case, if all numbers in the array are unique except for one duplicate, we would need to store n - 1 unique numbers in the set before finding the duplicate. In the best case, if the duplicate number is the first one we encounter, we would only need to store one number in the set, resulting in O(1) space complexity.

