'''You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.

Example 1:

Input: x = 1234

Output: 4321
Example 2:

Input: x = -1234

Output: -4321
Example 3:

Input: x = 1234236467

Output: 0
Constraints:

-2^31 <= x <= 2^31 - 1
'''
#bf
class Solution:
    def reverse(self, x: int) -> int:
        orginal = x
        x = abs(x)
        res = int(str(x)[:: -1])
        if orginal < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) -1:
            return 0
        return res
#time complexity: O(1) since the number of digits in a 32-bit integer is constant (at most 10 digits).
#space complexity: O(1) since we are using a constant amount of space for variables and the reversed string representation of the integer.