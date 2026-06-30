'''You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
Constraints:

1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length
'''

#bf
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums) - k + 1):
            maximum = nums[i]
            for j in range(i, i + k):
                maximum = max(maximum, nums[j])
            output.append(maximum)
        return output
#time complexity: O(n*k)
#space complexity: O(n - k + 1) space for output, O(1) space for maximum


#heap
from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
#time complexity: O(nlogk)
#space complexity: O(n)