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
#brute force solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 # result variable
        store = set(nums) # store input array in a set for O(1) lookups

        for num in nums: # iterate through input array
            streak, curr = 0, num # streak variable to count consecutive sequence, curr variable to check for consecutive numbers
            while curr in store: # check if current number is in set
                streak += 1 # increment streak
                curr += 1 # increment current number to check for next consecutive number
            res = max(res, streak) # update result with maximum streak
        return res 
#time complexity: O(n^2)
#space complexity: O(n)

#hash set solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
#space complexity: O(n)
#time complexity: 0(n)

