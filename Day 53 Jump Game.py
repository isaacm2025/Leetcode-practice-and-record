'''You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:

Input: nums = [1,2,0,1,0]

Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

Example 2:

Input: nums = [1,2,1,0,1]

Output: false
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


from typing import List
#recursion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) -1:
                return True
            end = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True
            return False
        return dfs(0)
#time complexity: O(n!)
#space complexity: O(n)

#dp top down
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) -1:
                return True
            if nums[i] == 0:
                return False
            end = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)
#time complexity: O(n^2)
#space complexity: O(n)

#dp bottom up
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            end = min(n - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
#time complexity: O(n^2)
#space complexity: O(n)

#greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
#time complexity: O(n)
#space complexity: O(1)