'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
#time complexity: O(n^2) since we have two nested loops iterating through the array
#space complexity: O(1)

#sorting
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append((num, i))
        A.sort() #sort the array of tuples based on the first element (the number)
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0] #calculate the sum of the two numbers at indices i and j
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])] #return the original indices of the two numbers in sorted order
            elif cur < target:
                i += 1 #if the sum is less than the target, move the left pointer to the right to increase the sum
            else:
                j -= 1 #if the sum is greater than the target, move the right pointer to the left to decrease the sum
        return []
#time complexity: O(n log n) due to the sorting step, and O(n) for the two-pointer traversal, resulting in O(n log n) overall
#space complexity: O(n) for the additional array of tuples storing the numbers and their original indices

#hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            indices[num] = i #store the index of each number in a hash map
        for i, num in enumerate(nums):
            diff = target - num #calculate the difference needed to reach the target
            if diff in indices and indices[diff] != i: #check if the difference exists in the hash map and is not the same index as the current number
                return [i, indices[diff]] #return the current index and the index of the difference
        return []
#time complexity: O(n) for building the hash map and O(n) for the second loop, resulting in O(n) overall
#space complexity: O(n) for the hash map