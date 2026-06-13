'''Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10'''

from typing import List
#recursion
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: #base case, if there are no numbers, there is only one permutation, the empty list
            return [[]]
        perms = self.permute(nums[1:]) #get the perms of the rest of the list
        res = []
        for perm in perms: #for each perm, insert the first number in every possible position
            for i in range(len(perm) + 1):
                p_copy = perm.copy() #make a copy of the current permutation
                p_copy.insert(i, nums[0]) #insert the first number at position i
                res.append(p_copy) #add the new perm to the result
        return res
#time complexity: O(n! * n^2) because we are generating n! permutations and for each permutation we are inserting the first number in n positions, 
#which takes O(n) time, and we are doing this for each of the n! permutations, so the total time complexity is O(n! * n^2)
#space complexity: O(n! * n) because we are generating n! permutations and each permutation takes O(n) space, so the total space complexity is O(n! * n)

#iteration
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]] #start with the empty list as the only permutation
        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1): #for each perm, insert the current number in every possible position
                    p_copy = perm.copy() #make a copy of the current permutation
                    p_copy.insert(i, num)
                    new_perms.append(p_copy) #add the new perm to the new perms list
            perms = new_perms #update perms to the new perms
        return perms
#time complexity: O(n! * n^2) because we are generating n! permutations and for each permutation we are inserting the current number in n positions, which takes O(n) time, and we are doing this for each of the n! permutations, so the total time complexity is O(n! * n^2)
#space complexity: O(n! * n) because we are generating n! permutations and each permutation takes O(n) space, so the total space complexity is O(n! * n)

#backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]
#time complexity: O(n! * n) because we are generating n! permutations and for each permutation we are copying the list, which takes O(n) time, so the total time complexity is O(n! * n)
#space complexity: O(n) because we are using O(n) space for the recursion stack and O(n) space for the current permutation, so the total space complexity is O(n)