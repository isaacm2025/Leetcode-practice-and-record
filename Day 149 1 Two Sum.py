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
Only one valid answer exists.
'''

#bf
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
#time complexity: O(n^2) because we are going through the entire array twice
#space complexity: O(1) because we are not using any extra space

#sorting
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums): #enumerate gives us both the index and the number in the array
            A.append([num, i]) # create a list of lists where each inner list contains the number and its index
        A.sort() # sort the list of lists based on the numbers
        i, j = 0, len(nums) - 1 # initialize two pointers, one at the start and one at the end of the list
        while i < j:
            cur = A[i][0] + A[j][0] # calculate the sum of the numbers at the two pointers
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])] # return the indices of the two numbers in sorted order
            elif cur < target:
                i += 1 # if the sum is less than the target, move the left pointer to the right to increase the sum
            else:
                j -= 1
        return []
#time complexity: O(nlogn) because we are sorting the list of lists, n because of sorting, logn because of the sort function, sorting function is O(nlogn) because it uses Timsort algorithm
#space complexity: O(n) because we are creating a new list of lists to store the numbers and their indices

#hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i] # if the difference is already in the dictionary, return the indices of the two numbers
            seen[num] = i # add the current number and its index to the dictionary
        return []
#time complexity: O(n) because we are going through the entire array once
#space complexity: O(n) because we are storing the seen numbers and their indices in a dictionary, which can take up to O(n) space in the worst case if all numbers are unique