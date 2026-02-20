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
0 <= heights[i] <= 1000
'''

#brute force:
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            height = heights[i]
            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1
            rightMost -= 1
            leftMost += 1
            max_area = max(max_area, height * (rightMost - leftMost + 1))
        return max_area
#time complexity: O(n^2) where n is the number of bars in the histogram
#space complexity: O(1)
        