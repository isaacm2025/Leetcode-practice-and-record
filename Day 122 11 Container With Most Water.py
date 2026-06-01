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
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
'''

#bf
from ast import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res= 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
#time O(n^2) because we have two nested loops that iterate through the input array, where n is the length of the input array.
#space O(1) because we are using a constant amount of extra space to store the maximum area found so far and the variables used in the loops.

#two pointers
from ast import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res
#time O(n) because we have a single loop that iterates through the input array, where n is the length of the input array.
#space O(1) because we are using a constant amount of extra space to store the maximum area found so far and the variables used in the loops.