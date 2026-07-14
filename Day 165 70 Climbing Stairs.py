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

#recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
#time complexity: O(2^n) where n is the number of steps. The recursion tree has a branching factor of 2, leading to an exponential number of calls.
#space complexity: O(n) where n is the number of steps. The maximum depth of the recursion tree is n, which corresponds to the maximum number of recursive calls on the call stack.

#dp
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
#time complexity: O(n) where n is the number of steps. The algorithm iterates through the range from 3 to n, performing constant time operations for each step.
#space complexity: O(n) where n is the number of steps. The algorithm uses an array of size n + 1 to store the number of distinct ways to reach each step.

#dp optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
#time complexity: O(n) where n is the number of steps. The algorithm iterates through the range from 0 to n - 1, performing constant time operations for each step.
#space complexity: O(1) as the algorithm uses a constant amount of space to store the variables one and two, regardless of the input size n.