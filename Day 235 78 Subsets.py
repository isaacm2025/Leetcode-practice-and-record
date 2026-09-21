'''Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

#backtracking
from typing import List
class Solution:
    def subsetss(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
#time complexity: O(n*2^n) where n is the length of nums. We have 2^n subsets and for each subset, we take O(n) time to copy it to the result.
#space complexity: O(n) where n is the length of nums. The maximum depth of the recursion tree is n, and we use O(n) space to store the current subset.
