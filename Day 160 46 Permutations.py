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
        res = [[]]
        for num in nums:
            new_perms = []
            for p in res:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            res = new_perms
        return res
#time complexity: O(n^2 *n!) where n is the length of the input array. The number of permutations of a set of size n is n!, and for each permutation, we may take O(n^2) time to generate it. The O(n^2) factor comes from the fact that we are inserting an element into a list of size n, which takes O(n) time, and we are doing this for each of the n elements in the list.
#space complexity: O(n*n!) for the result list, where n is the length of the input array. The result list will take O(n*n!) space to store all permutations, but this is not counted towards the space complexity since it is part of the output.

#backtracking
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.backtrack(nums, 0)
        return self.res
    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return 
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]
#time complexity: O(n*n!) where n is the length of the input array. The number of permutations of a set of size n is n!, and for each permutation, we may take O(n) time to copy it to the result list.
#space complexity: O(n! * n) for the result list, where n is the length of the input array. The result list will take O(n! * n) space to store all permutations, but this is not counted towards the space complexity since it is part of the output. The recursion stack will take O(n) space, where n is the length of the input array.
