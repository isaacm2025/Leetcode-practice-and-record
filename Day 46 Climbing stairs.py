'''You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
Constraints:

1 <= n <= 45'''

#recursion
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i > n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
#time complexity: O(2^n)
#space complexity: O(n)

#dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i]!= -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)
#time complexity: O(n)
#space complexity: O(n)

#dynamic programming with space optimization
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
#time complexity: O(n)
#space complexity: O(1)

#math
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n = n + 1
        return int((phi ** n - psi ** n) / sqrt5)
#time complexity: O(1)
#space complexity: O(1)