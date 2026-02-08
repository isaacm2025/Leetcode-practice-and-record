'''You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-1,1,2], k = 2

Output: 4
Explanation: [2], [2,-1,1], [-1,1,2], [2] are the subarrays whose sum is equals to k.

Example 2:

Input: nums = [4,4,4,4,4,4], k = 4

Output: 6
Constraints:

1 <= nums.length <= 20,000
-1,000 <= nums[i] <= 1,000
-10,000,000 <= k <= 10,000,000
'''

from typing import List
#brute approach 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res
#time complexity: O(n^2)
#space complexity: O(1)

#hash map
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
 
        return res
#time complexity: O(n)
#space complexity: O(n)