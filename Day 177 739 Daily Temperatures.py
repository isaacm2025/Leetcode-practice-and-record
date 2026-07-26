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
1 <= temperatures[i] <= 100


Topics

Recommended Time & Space Complexity

Hint 1
A brute force solution would involve iterating through the array with index i and checking how far is the next greater element to the right of i. This would be an O(n^2) solution. Can you think of a better way?'''

#bf
from typing import List
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
#time complexity: O(n^2)
#space complexity: O(n)