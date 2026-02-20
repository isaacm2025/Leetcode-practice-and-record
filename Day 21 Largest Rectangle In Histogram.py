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
            rightMost = i + 1 #initialize the rightMost pointer to the index of the next bar to the right of the current bar
            while rightMost < n and heights[rightMost] >= height: #move rightMost pointer to the right until we find a bar that is shorter than the current bar
                rightMost += 1

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height: #move leftMost pointer to the left until we find a bar that is shorter than the current bar
                leftMost -= 1
            rightMost -= 1
            leftMost += 1
            max_area = max(max_area, height * (rightMost - leftMost + 1)) #calculate the area of the rectangle that can be formed with the current bar as the height and the width as the distance between the leftMost and rightMost pointers
        return max_area
#time complexity: O(n^2) where n is the number of bars in the histogram
#space complexity: O(1)

#stack optimal:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]): #while the stack is not empty and the current height is less than or equal to the height of the bar at the top of the stack
                heights = heights[stack.pop()] #pop the top of the stack and get the height of the bar at that index
                width = i if not stack else i - stack[-1] - 1 #calculate the width of the rectangle that can be formed with the height of the bar at the top of the stack
                max_area = max(max_area, heights * width)
            stack.append(i)
        return max_area
#time complexity: O(n) where n is the number of bars in the histogram
#space complexity: O(n) for the stack in the worst case when the histogram is in