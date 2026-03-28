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
#hash set
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit * digit
            output += digit
            n //= 10
        return output
#time complexity O(log n) for the sum of squares function and O(k) for the while loop where k is the number of iterations until we find a cycle or reach 1
#space complexity O(log n) for the hash set to store the visited numbers

#fast and slow pointers
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1
        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = self.sumOfSquares(fast)
            lam += 1
        return True if fast == 1 else False
    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit * digit
            output += digit
            n //= 10
        return output
#time complexity O(log n) for the sum of squares function and O(k) for the while loop where k is the number of iterations until we find a cycle or reach 1
#space complexity O(1) for the fast and slow pointers
        
        

