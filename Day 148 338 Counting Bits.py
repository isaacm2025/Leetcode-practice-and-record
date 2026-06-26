'''Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000
'''

#Bit manipulation
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            count = 0
            for i in range(32): #iterate through all 32 bits of the integer
                if num & (1 << i): #if the ith bit is set, increment count, << means left shift, so 1 << i means 1 shifted left by i bits
                    count += 1
            res.append(count)
        return res
#time complexity: O(nlogn)
#space complexity: O(n)