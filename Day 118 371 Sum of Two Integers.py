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
        return a + b
#time complexity: O(1) since we are performing a constant number of operations
#space complexity: O(1) since we are using a constant amount of space for the result

#bit manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            bitA = (a >> i) & 1
            bitB = (b >> i) & 1
            curBit = bitA ^ bitB ^ carry
            carry = (bitA + bitB + carry) >=2
            if curBit:
                res |= (1 << i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res
#time complexity: O(1) since we are always iterating through 32 bits
#space complexity: O(1) since we are using a constant amount of space for the result and the carry