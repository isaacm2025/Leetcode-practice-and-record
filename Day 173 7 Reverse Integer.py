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
        org = x
        x = abs(x)
        res = int(str(x)[::-1]) # [::-1] is used to reverse the string representation of the integer, this line means that we convert the integer to a string, reverse the string, and then convert it back to an integer. 
        #str(x) converts the integer x to its string representation, [::-1] reverses the string, and int(...) converts the reversed string back to an integer.
        if org < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) - 1: # (1 << 31) is equivalent to 2^31, and (1 << 31) - 1 is equivalent to 2^31 - 1. This line checks if the reversed integer is outside the signed 32-bit integer range.
            return 0
        return res
#time complexity: O(1)
#space complexity: O(1)