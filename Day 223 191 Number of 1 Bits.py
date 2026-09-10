'''You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.


Example 1:

Input: n = 23

Output: 4
Explanation: The binary representation of 23 is 10111, which contains four 1 bits.


Example 2:

Input: n = 2147483645

Output: 30
Explanation: The binary representation of 2147483645 is 1111111111111111111111111111101, which contains thirty 1 bits.


Constraints:

0 <= n <= 2^31 - 1.'''

#bit mask
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res
#time complexity: O(1)
#space complexity: O(1)

#optimal
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
#time complexity: O(1)
#space complexity: O(1)