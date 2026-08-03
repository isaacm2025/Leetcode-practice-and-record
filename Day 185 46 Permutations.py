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

#iteration
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            newPerms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    pCopy = perm.copy()
                    pCopy.insert(i, num)
                    newPerms.append(pCopy)
            perms = newPerms
        return perms
#time complexity: O(n^2 * n!) because we generate all possible permutations of the input list
#space complexity: O(n^2 * n!) because we store all possible permutations in the result list

#backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums.copy())
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]
#time complexity: O(n * n!) because we generate all possible permutations of the input list
#space complexity: O(n * n!) for the recursion stack and the result list