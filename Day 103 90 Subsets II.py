'''You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20'''

#bf
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)
        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]
#time complexity: O(n * 2^n) where n is the length of nums.
#space complexity: O(2^n) for the result set and the recursion stack.

#backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, subset):
            res.append(subset[::])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res
#time complexity: O(n * 2^n) where n is the length of nums.
#space complexity: O(2^n) for the result list and the recursion stack, O(n) for the subset list.

#iteration
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_idx = idx = 0
        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res
#time complexity: O(n * 2^n) where n is the length of nums.
#space complexity: O(2^n) for the result list, O(1) for the temporary list.