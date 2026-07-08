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

#backtracking solution
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return res
#time complexity: O(n*2^n) where n is the length of the input array. The number of subsets of a set of size n is 2^n, and for each subset, we may take O(n) time to copy it to the result list.
#space complexity: O(n) for the recursion stack and the subset list, where n is the length of the input array. The result list will take O(2^n) space to store all subsets, but this is not counted towards the space complexity since it is part of the output.

#iteration
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res
#time complexity: O(n*2^n) where n is the length of the input array. The number of subsets of a set of size n is 2^n, and for each subset, we may take O(n) time to copy it to the result list.
#space complexity: O(2^n) for the result list, where n is the length of the input array. 
# The result list will take O(2^n) space to store all subsets, but this is not counted towards the space complexity since it is part of the output.
            