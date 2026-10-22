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

1 <= n <= 45
'''

#recursion with memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
#time complexity: O(2^n) where n is the number of steps. In the worst case, we may explore all possible combinations of steps, leading to an exponential time complexity.
#space complexity: O(n) where n is the number of steps. The maximum depth of the recursion stack can go up to n in the worst case, leading to a space complexity of O(n).

#dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
#time complexity: O(n) where n is the number of steps. We iterate through the range from 3 to n, performing constant time operations for each step, leading to a linear time complexity.
#space complexity: O(n) where n is the number of steps. We use an array dp of size n + 1 to store the number of distinct ways to reach each step, leading to a space complexity of O(n).