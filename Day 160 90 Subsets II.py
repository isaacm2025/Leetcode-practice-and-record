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
#time complexity: O(n*2^n) where n is the length of the input array. The number of subsets of a set of size n is 2^n, and for each subset, we may take O(n) time to copy it to the result list.
#space complexity: O(n) for the recursion stack and the subset list, where n is the length of the input array. The result set will take O(2^n) space to store all unique subsets, but this is not counted towards the space complexity since it is part of the output. The conversion of the set to a list will also take O(2^n) space
    

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
#time complexity: O(n*2^n) where n is the length of the input array. The number of subsets of a set of size n is 2^n, and for each subset, we may take O(n) time to copy it to the result list.
#space complexity: O(n) for the recursion stack and the subset list, where n is the length of the input array. The result list will take O(2^n) space to store all unique subsets, but this is not counted towards the space complexity since it is part of the output.
