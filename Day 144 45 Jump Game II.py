'''You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:

j <= nums[i]
i + j < nums.length
You are initially positioned at nums[0].

Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

Example 1:

Input: nums = [2,4,1,1,1,1]

Output: 2
Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.

Example 2:

Input: nums = [2,1,2,1,0]

Output: 2
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 100
'''

#recursion
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            end = min(len(nums) - 1, i + nums[i])
            res = float('inf')
            for j in range(i + 1, end + 1):
                res = min(res, dfs(j)+ 1)
            return res
        return dfs(0)
#time complexity: O(n!) because in the worst case, we can jump to every index from the current index, and we have n indices to jump to.
#space complexity: O(n) because of the recursion stack.

#dp
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1000000] * n
        dp[-1] = 0
        for i in range(n -2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]
#time complexity: O(n^2) because for each index, we may have to check all the indices that can be reached from it.
#space complexity: O(n) because of the dp array.

#greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
#time complexity: O(n) because we are iterating through the array once.
#space complexity: O(1) because we are using a constant amount of space.