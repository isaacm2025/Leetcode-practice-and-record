'''Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9'''


from typing import List
#brute force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
#time complexity is O(n^2) and space complexity is O(n)

#hash set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        longest = 0
        for num in NumSet:
            if num - 1 not in NumSet:
                length = 1 # start with 1 since we are counting the current number
                while num + length in NumSet:
                    length += 1
                longest = max(length, longest)
        return longest
#time complexity is O(n) and space complexity is O(n)