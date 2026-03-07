'''Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2

Output: 4
Example 2:

Input: nums = [2,3,1,1,5,5,4], k = 3

Output: 4
Constraints:

1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000
'''

#sorting
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
#time complexity: O(nlogn)
#space complexity: O(1)

#min heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
#time complexity: O(nlogk)
#space complexity: O(k)

#quick select
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(left, right):
            pivot, p = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            if p > k:
                return quickSelect(left, p - 1)
            elif p < k:
                return quickSelect(p + 1, right)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)
#time complexity: O(n) on average, O(n^2) in worst case
#space complexity: O(1) on average, O(n) in worst case due to recursion stack
