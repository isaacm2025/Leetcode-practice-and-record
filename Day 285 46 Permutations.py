'''Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
'''

#recursion
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
#time complexity: O(n*n!) where n is the length of nums. We have n! permutations and for each permutation, we need to copy it to the result list which takes O(n) time.
#space complexity: O(n*n!) where n is the length of nums. We are storing n! permutations and each permutation can have at most n elements.
        
#iteration
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    newPerms.append(p_copy)
            perms = newPerms
        return perms
#time complexity: O(n*n!) where n is the length of nums. We have n! permutations and for each permutation, we need to copy it to the result list which takes O(n) time.
#space complexity: O(n*n!) where n is the length of nums. We are storing n! permutations and each permutation can have at most n elements.