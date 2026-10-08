'''You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 100,000.
1 <= temperatures[i] <= 100'''

#stack
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
#time complexity: O(n) where n is the length of the input array temperatures. Each element is pushed and popped from the stack at most once.
#space complexity: O(n) where n is the length of the input array temperatures. In the worst case, all elements could be pushed onto the stack if the temperatures are in decreasing order.

#dp
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] > 0:
                    j += res[j]
                else:
                    j = n
            if j < n:
                res[i] = j - i
        return res  
#time complexity: O(n) where n is the length of the input array temperatures. Each element is processed at most once.
#space complexity: O(n) where n is the length of the input array temperatures. The result array is used to store the number of days until a warmer temperature for each day.