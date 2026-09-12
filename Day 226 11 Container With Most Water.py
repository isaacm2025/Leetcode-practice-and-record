'''You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.


Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.


Example 2:

Input: height = [2,2,2]

Output: 4

Constraints:

2 <= height.length <= 100,000
0 <= height[i] <= 10,000
'''

#bf
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res
#time complexity: O(n^2)
#space complexity: O(1)

#two pointer
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
#time complexity: O(n)
#space complexity: O(1)