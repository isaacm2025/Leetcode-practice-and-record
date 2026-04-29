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
            if (1 << i) & n:
                res += 1
        return res
#time complexity: O(1) since the loop runs a fixed number of times (32)
#space complexity: O(1) since we are using a constant amount of space

#bit mask optimal
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
#time coomplexity: O(1) since the number of iterations is at most 32 (the number of bits in the input)
#space complexity: O(1) since we are using a constant amount of space