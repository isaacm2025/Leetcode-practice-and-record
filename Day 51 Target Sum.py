'''You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.

Example 1:

Input: nums = [2,2,2], target = 2

Output: 3
Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
-1000 <= target <= 1000'''


from collections import defaultdict
from typing import List
#recursion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, total):
            if i == len(nums):
                return total == target
            return (backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i]))
        return backtrack(0, 0)

#time complexity: O(2^n)
#space complexity: O(n) for the recursion stack


#dp (top-down)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)
#time complexity: O(n * m)
#space complexity: O(n * m) where m is the range of possible sums (from -1000 to 1000)

#dp (bottom-up)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for total, count in dp[i - 1].items():
                dp[i][total + nums[i-1]] += count
                dp[i][total - nums[i-1]] += count
        return dp[n][target]
#time complexity: O(n * m)
#space complexity: O(n * m) where m is the range of possible sums (from -1000 to 1000)


