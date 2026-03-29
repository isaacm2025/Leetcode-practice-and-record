'''Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

You may not use any built-in library functions.

Example 1:

Input: x = 2.00000, n = 5

Output: 32.00000
Example 2:

Input: x = 1.10000, n = 10

Output: 2.59374
Example 3:

Input: x = 2.00000, n = -3

Output: 0.12500
Constraints:

-100.0 < x < 100.0
-1000 <= n <= 1000
n is an integer.
If x = 0, then n will be positive.'''


#brute force
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = 1
        for i in range(abs(n)):
            res *= x
        return res if n >= 0 else 1 / res
#time complexity O(n) where n is the absolute value of the exponent
#space complexity O(1) since we are using a constant amount of space to store the result

#recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x * x, n//2)
            return x *res if n % 2 else res
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
#time complexity O(log n) where n is the absolute value of the exponent
#space complexity O(log n) for the recursive call stack

#iteration
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = 1
        power = abs(n)
        while power:
            if power & 1:
                res * = x
            x *= x
            power >>= 1
        return res if n >= 0 else 1 / res
#time complexity O(log n) where n is the absolute value of the exponent
#space complexity O(1) since we are using a constant amount of space to store the result