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
-20 <= nums[i] <= 20
'''

#bf
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i, cur):
            if i == len(nums):
                res.add(tuple(cur))
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs((i + 1), cur)
        nums.sort()
        dfs(0, [])
        return [list(s) for s in res]
#time complexity: O(n*2^n) where n is the length of nums.
#space complexity: O(2^n) where n is the length of nums.
        

#iteration
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prevIdx = idx = 0
        for i in range(len(nums)):
            idx = prevIdx if i >= 1 and nums[i] == nums[i - 1] else 0
            prevIdx = len(res)
            for j in range(idx, prevIdx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res
#time complexity: O(n*2^n) where n is the length of nums.
#space complexity: O(n*2^n) where n is the length of nums.