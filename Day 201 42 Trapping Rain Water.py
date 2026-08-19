'''You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the total amount of water that can be trapped between the bars.


Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 20,000
0 <= height[i] <= 100,000'''

#stack
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(left, right) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
#time: O(n)
#space: O(n)
