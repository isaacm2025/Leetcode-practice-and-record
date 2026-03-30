'''You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30'''

#bit mask
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 <<i) & n:
                res += 1
        return res
#time complexity: O(1)
#space complexity: O(1)

#bit mask
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n >>= 1
        return res
#time complexity: O(1)
#space complexity: O(1)

#build-in function
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
#time complexity: O(1)
#space complexity: O(1)