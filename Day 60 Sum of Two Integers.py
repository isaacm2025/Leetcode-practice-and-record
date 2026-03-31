'''Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000'''

#brute force
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a + b
#time complexity: O(1)
#space complexity: O(1)

