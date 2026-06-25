'''You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9'''

#recursion
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
#time complexity: O(N)
#space complexity: O(N)