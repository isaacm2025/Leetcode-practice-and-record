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
from collections import deque
import heapq
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
#time complexity: O(n*k) where n is the length of the input array nums and k is the size of the sliding window. We iterate through the array and for each window, we iterate through the k elements to find the maximum.
#space complexity: O(n-k+1)

#heap
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
#time complexity: O(n log k) where n is the length of the input array nums and k is the size of the sliding window. We iterate through the array and for each element, we perform a heap push and pop operation which takes O(log k) time.
#space complexity: O(k) where k is the size of the sliding window. We use a heap to store the elements in the current window, which can contain at most k elements.

#deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
#time complexity: O(n) where n is the length of the input array nums. We iterate through the array once, and each element is added and removed from the deque at most once.
#space complexity: O(k) where k is the size of the sliding window. We use a deque to store the indices of the elements in the current window, which can contain at most k elements.