'''Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.

'''

#bf
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i): # if the ith bit is 1, << means left shift, so we are checking if the ith bit is 1, 1 << i equals 2^i, so n & 2^i checks if the ith bit is 1
                binary += "1"
            else:
                binary += "0"
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= 1 << i # if the ith bit is 1, we add 2^i to the result, 1 << i equals 2^i, |= means we are setting the ith bit to 1
        return res
#time complexity: O(1)
#space complexity: O(1)