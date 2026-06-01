'''You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
'''

#bf
from ast import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        for i in range(n):
            leftMax = rightMax = height[i]
            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
            res += min(leftMax, rightMax) - height[i]
        return res
#time O(n^2) because we have two nested loops that iterate through the input array, where n is the length of the input array.
#space O(1) because we are using a constant amount of extra space to store the maximum area found so far and the variables used in the loops.

#stack
from ast import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        res= 0
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
#time O(n) because we have a single loop that iterates through the input array, where n is the length of the input array. Each element is pushed and popped from the stack at most once, which takes O(1) time on average.
#space O(n) because in the worst case, we could have all the bars in the input array being of increasing height, which would require us to store all n indices in the stack, where n is the length of the input array. 
# Each entry in the stack takes O(1) space, so the total space used by the stack can be O(n) in the worst case.