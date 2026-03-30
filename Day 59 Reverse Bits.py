'''Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.'''

#brute force
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res += 1 << i
        return res
#space complexity O(1)
#time complexity O(1) since we are always iterating 32 times

#bit manipulation
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res +=(bit << (31 - i)))
        return res
#space complexity O(1)
#time complexity O(1) since we are always iterating 32 times