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
        def bf(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            bf(i + 1, subset)
            subset.pop()
            bf(i + 1, subset)
        nums.sort()
        bf(0, [])
        return [list(s) for s in res]
#time complexity: O(2^n) where n is the length of nums. In the worst case, we have to explore all possible subsets of nums.
#space complexity: O(n) where n is the length of nums. The maximum depth of the recursion tree is n, and we are using a list to store the current subset which can have at most n elements.

#backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
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
#time complexity: O(2^n) where n is the length of nums. In the worst case, we have to explore all possible subsets of nums.
#space complexity: O(n) where n is the length of nums. The maximum depth of the recursion tree is n, and we are using a list to store the current subset which can have at most n elements.