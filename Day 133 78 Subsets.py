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
-10 <= nums[i] <= 10'''

#backtracking
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i): #i is the index of the current element in nums
            if i >= len(nums): #if we have considered all elements in nums, we can add the current subset to the result
                res.append(subset.copy())
                return #we can either include the current element in the subset or not include it
            subset.append(nums[i]) #include the current element in the subset
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0) #start from the first element in nums
        return res
#time: O(n * 2^n), 
#space: O(n) for subset, O(n * 2^n) for res, because there are 2^n subsets and each subset can have at most n elements.

#iteration
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
#time: O(n * 2^n), space: O(n * 2^n)

