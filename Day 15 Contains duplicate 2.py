'''
You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

Example 1:

Input: nums = [1,2,3,1], k = 3

Output: true
Example 2:

Input: nums = [2,1,2], k = 1

Output: false
Constraints:

1 <= nums.length <= 100,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
0 <= k <= 100,000
'''
from typing import List
#brute force
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            for R in range(L + 1, min(len(nums), L + k + 1)):
                if nums[L] == nums[R]:
                    return True
        return False
    
#Time complexity: O(n * min(n,k))
#space com: O(1)

#Hash map
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        return False
#time complexity:O(n)
#space complexity: O(n)

#Hash set
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
#time complexity:O(n)
#space complexity: O(min(n,k))
