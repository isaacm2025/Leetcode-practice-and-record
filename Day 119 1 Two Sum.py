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
            for j in range(i + 1, len(nums)): #we start the inner loop from i + 1 to avoid checking the same pair of indices twice and to ensure that i != j
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
#time complexity: O(n^2) because of the nested loops
#space complexity: O(1) because we are not using any additional data structures

#sorting
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums): #we create a new list A to store the numbers and their indices, we use enumerate to get both the index and the number at the same time
            A.append([num, i]) 
        A.sort() #sort the list A based on the numbers, this will allow us to use the two pointer technique to find the pair of numbers that add up to the target
        i, j = 0, len(nums) - 1 #we initialize two pointers, one at the beginning of the list and one at the end of the list
        while i < j:
            curSum = A[i][0] + A[j][0] #we calculate the sum of the numbers at the two pointers, we access the number using A[i][0] and A[j][0] because A is a list of lists where each inner list contains the number and its index
            if curSum == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])] #if the sum is equal to the target, we return the indices of the two numbers, we use min and max to ensure that we return the smaller index first as required by the problem statement
            elif curSum < target:
                i += 1
            else:
                j -= 1
        return []
#time complexity: O(n log n) because of the sorting step
#space complexity: O(n) because we are creating a new list A to store the numbers and their indices

#hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #create a hashmap to store the previously seen numbers and their indices, the key is the number and the value is its index
        for i, n in enumerate(nums): #iterate through the array using enumerate to get both the index and the number at the same time
            diff = target - n #calculate the difference between the target and the current number, this is the number we need to find in the hashmap to complete the pair that adds up to the target
            if diff in prevMap: #if the difference is already in the hashmap, then we have found the pair of numbers that add up to the target, we return their indices
                return [prevMap[diff], i]
            prevMap[n] = i #otherwise, we add the current number and its index to the hashmap, this will allow us to find it later if we encounter a number that needs it to complete the pair
        return []
#time complexity: O(n) because we are iterating through the array once
#space complexity: O(n) because in the worst case, we may have to store all the numbers in the hashmap if they are all unique