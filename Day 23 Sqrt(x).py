'''You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:

Input: x = 9

Output: 3
Example 2:

Input: x = 13

Output: 3
Constraints:

0 <= x <= ((2^31)-1)'''

#brute force:
from cmath import sqrt


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: #the square root of 0 is 0
            return 0 #the square root of 1 is 1
        
        res = 1 #initialize the result to 1, which is the smallest positive integer
        for i in range(1, x + 1): #iterate through the numbers from 1 to x
            if i * i > x: #if the square of the current number is greater than x, return the previous number
                return res
            res = i
        return res
#time complexity: O(sqrt(n))
#space complexity: O(1)

#build in function:
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
#time complexity: O(1)
#space complexity: O(1)