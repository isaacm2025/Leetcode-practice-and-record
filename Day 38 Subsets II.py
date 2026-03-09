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


from typing import List
#brute force
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
#time complexity: O(n * 2^n) where n is the length of the input array. This is because we are generating all possible subsets, which can be up to 2^n, and each subset can take O(n) time to copy into the result set.
#space complexity: O(2^n) due to the space required to store all possible subsets in the result set. Additionally, the recursion stack can go up to O(n) in the worst case, but this is overshadowed by the space needed for the result set.