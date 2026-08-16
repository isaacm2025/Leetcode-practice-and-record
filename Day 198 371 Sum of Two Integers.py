'''Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000'''

#bf
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])
#time complexity: O(1)
#space complexity: O(1)

#optimal
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF
        while b!=0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= maxInt else ~(a ^ mask) # it means if a is greater than maxInt, then return the negative value of a, otherwise return a as it is.
#time complexity: O(1)
#space complexity: O(1)