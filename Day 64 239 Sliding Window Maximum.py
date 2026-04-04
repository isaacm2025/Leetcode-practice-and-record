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

#brute force
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k):
                maxi = max(maxi, nums[j])
            output.append(maxi)
        return output
#time complexity: O(n * k) where n is the length of the input array and k is the size of the sliding window
#space complexity: O(n - k + 1) which is the size of the output list


#Heap
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
#time complexity: O(n log k) where n is the length of the input array and k is the size of the sliding window
#space complexity: O(k) which is the size of the heap

#dynamic programming
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        for j in range(n - 1, -1, -1):
            if j == n - 1 or (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output
#time complexity: O(n) where n is the length of the input array
#space complexity: O(n) which is the size of the left and right arrays