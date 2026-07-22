'''Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000
'''

#bf
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])
#time complexity: O(1)
#space complexity: O(1)

#bit manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) << 1 #it means (a & b) is the carry, and we need to shift it left by 1 to add it to the next bit
            a = (a ^ b) & mask #it means (a ^ b) is the sum without carry, and we need to mask it to 32 bits
            b = carry & mask #it means we need to mask the carry to 32 bits
        return a if a <= maxInt else ~(a ^ mask) #if a is less than or equal to maxInt, we return a, otherwise we return the negative of (a ^ mask) which is the two's complement of a, ~ means bitwise NOT, so ~(a ^ mask) is the two's complement of a, which is the negative of a
#time complexity: O(1)
#space complexity: O(1)