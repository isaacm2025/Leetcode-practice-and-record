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
        def backtrack(start, path): #backtracking function to generate all subsets
            if start == len(nums): #base case, if we have reached the end of the list, add the current path to the result set
                res.add(tuple(path))
                return
            path.append(nums[start])
            backtrack(start + 1, path)
            path.pop()
            backtrack(start + 1, path)
        nums.sort() #sort the input to handle duplicates
        backtrack(0, [])
        return [list(s) for s in res]
#time complexity: O(2^n * n) because we are generating 2^n subsets and for each subset we are converting it to a tuple and adding it to a set, which takes O(n) time, so the total time complexity is O(2^n * n)
#space complexity: O(2^n * n) because we are generating 2^n subsets and each subset takes O(n) space, so the total space complexity is O(2^n * n)

#iteration
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort the input to handle duplicates
        res = [[]] #start with the empty subset
        prev_Idx = idx = 0
        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0 
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res
#time complexity: O(2^n * n) because we are generating 2^n subsets and for each subset we are copying it and adding a new element, which takes O(n) time, so the total time complexity is O(2^n * n)
#space complexity: O(2^n) because we are generating 2^n subsets and O(1) space for each subset, so the total space complexity is O(2^n)
