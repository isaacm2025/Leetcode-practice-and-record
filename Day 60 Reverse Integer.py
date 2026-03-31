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

-2^31 <= x <= 2^31 - 1'''

#brute force
class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        res = int(str(x)[::-1])
        if org < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res
#time complexity: O(n)
#space complexity: O(n)

#recursion
class Solution:
    def reverse(self, x: int) -> int:
        def rec(n: int, rev: int) -> int:
            if n == 0:
                return rev
            rev = rev * 10 + n % 10
            return rec(n // 10, rev)
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = rec(x, 0) * sign
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res
#time complexity: O(n)
#space complexity: O(n)

