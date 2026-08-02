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
-1000 <= nums[i] <= 1000'''

#sorting
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
#time complexity: O(n log n) because we sort the list of numbers
#space complexity: O(n) because we store the numbers in a list

#minheap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
#time complexity: O(n log k) because we use a heap to store the numbers
#space complexity: O(k) because we store the numbers in a heap