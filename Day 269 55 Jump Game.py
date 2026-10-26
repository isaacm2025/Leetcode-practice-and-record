#greedy
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
#time complexity: O(n)
#space complexity: O(1)

#dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
#time complexity: O(n^2)
#space complexity: O(n)