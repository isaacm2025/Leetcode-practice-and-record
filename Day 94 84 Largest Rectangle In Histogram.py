'''You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000'''

#bf
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            height = heights[i]
            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            leftMost = i - 1
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1
            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, height *(rightMost - leftMost + 1))
        return maxArea
#time complexity: O(n^2)
#space complexity: O(1)

#stack optimal
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
#time complexity: O(n)
#space complexity: O(n)