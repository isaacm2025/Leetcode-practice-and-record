'''A non-cyclical number is an integer defined by the following algorithm:

Given a positive integer, replace it with the sum of the squares of its digits.
Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
If it stops at 1, then the number is a non-cyclical number.
Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.

Example 1:

Input: n = 100

Output: true
Explanation: 1² + 0² + 0² = 1

Example 2:

Input: n = 101

Output: false
Explanation:
1² + 0² + 1² = 2
2² = 4
4² = 16
1² + 6² = 37
3² + 7² = 58
5² + 8² = 89
8² + 9² = 145
1² + 4² + 5² = 42
4² + 2² = 20
2² + 0² = 4 (This number has already been seen)

Constraints:

1 <= n <= 1000
'''

#hashset
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            res += digit
            n //= 10
        return res
#time complexity: O(log n), where n is the input number, due to the number of digits in n and the operations performed on them.
#space complexity: O(log n), where n is the input number, due to the space used for the hash set to store visited numbers, which can grow up to the number of unique sums of squares of digits encountered during the process.