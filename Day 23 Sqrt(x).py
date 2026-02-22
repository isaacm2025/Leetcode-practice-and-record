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

#binary search:
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x #the square root of x cannot be greater than x, so we can set the right pointer to x
        res = 0

        while left <= right:
            mid = left + (right - left) // 2 #calculate the middle point to avoid overflow

            if mid * mid > x: #if the square of the middle point is greater than x, we need to search in the left half
                right = mid - 1 #move the right pointer to the left of the middle point
            elif mid * mid < x: #if the square of the middle point is less than x, we need to search in the right half
                left = mid + 1
                res = mid
            else:
                return mid
        return res
#time complexity: O(log(n))
#space complexity: O(1)

#recursion:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = self.mySqrt(x >> 2) << 1 #divide x by 4 and multiply the result by 2 to get an estimate of the square root
        right = left + 1 #the square root of x can only be left or left + 1, so we check both possibilities
        return left if right ** 2 > x else right #if the square of right is greater than x, return left, otherwise return right
#time complexity: O(log(n))
#space complexity: O(log(n)) due to the recursive call stack