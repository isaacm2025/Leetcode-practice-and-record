'''You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100'''


from typing import List
#brute force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res
#time complexity: O(n^2) where n is the number of temperatures in the input list, O(n) for the outer loop and O(n) for the inner loop
#space complexity: O(n) which is the size of the output list

#stack
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
#time complexity: O(n) where n is the number of temperatures in the input list, each temperature is pushed and popped at most once from the stack
#space complexity: O(n) which is the size of the stack in the worst case when the input list is in decreasing order


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
            res[i] = 0 if j == n else j - i
        return res
#time complexity: O(n) where n is the number of temperatures in the input list, each temperature is processed at most once and we are skipping the temperatures that are less than or equal to the current temperature
#space complexity: O(n) which is the size of the output list, O(1) for the variables used in the loop