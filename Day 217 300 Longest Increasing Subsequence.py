'''Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
Example 1:

Input: nums = [9,1,4,2,3,3,7]

Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:

Input: nums = [0,3,1,3,2,3]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000'''

#recursion
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, prev):
            if i == len(nums):
                return 0
            LIS = dfs(i + 1, prev)
            if prev == -1 or nums[prev] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            return LIS
        return dfs(0, -1)
#time complexity: O(2^n) where n is the length of the input array
#space complexity: O(n) where n is the length of the input array

#dp
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
#time complexity: O(n^2) where n is the length of the input array
#space complexity: O(n) where n is the length of the input array

#dp + bs
from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]
        return LIS
#time complexity: O(nlogn) where n is the length of the input array
#space complexity: O(n) where n is the length of the input array