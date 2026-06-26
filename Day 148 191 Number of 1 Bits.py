'''You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30
'''

#bit mask
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & (1 << i):
                count += 1
        return count
#time complexity: O(1)
#space complexity: O(1)