'''Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

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
Only one valid answer exists.'''

from typing import List
#brute force approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return []
# Time Complexity: O(n^2)
# Space Complexity: O(1)


#sorting
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i, num in enumerate(nums): # Create an array of pairs (number, original index)
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1 # two pointers
        while i < j:
            cur = A[i][0] + A[j][0] # sum of the two numbers at indices i and j
            if cur == target: #if sum matches target
                return [A[i][1], A[j][1]]  #return original indices
            elif cur < target: #move left pointer to right
                i+= 1 #move right pointer to left
            else: # move right pointer to left
                j -= 1 # move left pointer to right
        return []
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the additional array

#hash map approach (two pass)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums): # First pass: build the hashmap
            hashmap[n] = i  # Store the number and its index in the hashmap

        for i, n in enumerate(nums): # Second pass: check for the complement
            diff = target - n
            if diff in hashmap and hashmap[diff] != i:
                return [hashmap[diff], i] # Return indices of the two numbers
        return [] # No valid pair found
# Time Complexity: O(n)
# Space Complexity: O(n) for the hashmap
        
#hash map approach (one pass)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Initialize an empty hashmap
        for i, n in enumerate(nums): # Iterate through the array once
            diff = target - n # Calculate the complement (the number needed to reach the target)
            if diff in hashmap: # Check if the complement exists in the hashmap
                return [hashmap[diff], i] # If it exists, return the indices of the complement and the current number
            hashmap[n] = i  # Store the number and its index in the hashmap

        return [] # No valid pair found
# Time Complexity: O(n)
# Space Complexity: O(n) for the hashmap