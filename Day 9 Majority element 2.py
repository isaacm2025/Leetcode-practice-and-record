'''You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times. You can return the result in any order.

Example 1:

Input: nums = [5,2,3,2,2,2,2,5,5,5]

Output: [2,5]
Example 2:

Input: nums = [4,4,4,4,4]

Output: [4]
Example 3:

Input: nums = [1,2,3]

Output: []
Constraints:

1 <= nums.length <= 50,000.
-1,000,000,000 <= nums[i] <= 1,000,000,000
Follow up: Could you solve the problem in linear time and in O(1) space?'''

from typing import List
#Brute approach
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > len(nums) // 3:
                res.add(num)
        return list(res)
#time complexity: O(n^2)
#space complexity: O(1) since output array size will be most 2

#sorting
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res, n = [], len(nums)

        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            if (j - i) > n // 3:
                res.append(nums[i])
            i = j
        return res
#time complexity: O(n log n)
#space complexity: O(1) or O(n) depend on the sorting algorithm

