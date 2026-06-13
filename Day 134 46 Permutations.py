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
                p_copy = perm.copy()
                p_copy.insert(i, nums[0]) #insert the first number at position i
                res.append(p_copy) #add the new perm to the result
        return res
#time complexity: O(n! * n^2) because we are generating n! permutations and for each permutation we are inserting the first number in n positions, 
#which takes O(n) time, and we are doing this for each of the n! permutations, so the total time complexity is O(n! * n^2)
#space complexity: O(n! * n) because we are generating n! permutations and each permutation takes O(n) space, so the total space complexity is O(n! * n)