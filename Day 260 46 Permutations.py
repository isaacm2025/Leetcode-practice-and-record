'''Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10'''

#iteration
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy() # Create a copy of the current permutation
                    pCopy.insert(i, num) # Insert the current number at position i
                    newPerms.append(pCopy)
            perms = newPerms # Update perms to the new list of permutations
        return perms
#time complexity: O(n^2 *n!), where n is the length of nums
#space complexity: O(n^2 *n!), where n is the length of nums