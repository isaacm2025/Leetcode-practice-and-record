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
        res = [[]]
        for num in nums:
            newRes = []
            for p in res:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, num)
                    newRes.append(pCopy)
            res = newRes
        return res
#time complexity: O(n^2 *n!) where n is the length of nums. We have n! permutations and for each permutation, we take O(n^2) time to insert the new number in all possible positions.
#space complexity: O(n*n!) where n is the length of nums. We have n! permutations and each permutation takes O(n) space to store.