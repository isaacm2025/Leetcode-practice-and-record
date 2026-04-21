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
-1000 <= target <= 1000
'''

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
#time complexity: O(2^n) where n is the length of nums
#space complexity: O(n) where n is the length of nums

#dp space optimized
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
        return dp[target]
#time complexity: O(n * m) where n is the length of nums and m is the range of possible totals (which can be at most 2000 since nums[i] <= 1000 and target can be at most 1000)
#space complexity: O(m) where m is the range of possible totals (which can be at most 2000 since nums[i] <= 1000 and target can be at most 1000)