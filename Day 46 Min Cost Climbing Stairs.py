'''You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Example 1:

Input: cost = [1,2,3]

Output: 2
Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.

Example 2:

Input: cost = [1,2,1,2,1,1,1]

Output: 4
Explanation: Start at index = 0.

Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
Pay the cost of cost[6] = 1 and take one step to reach the top.
The total cost is 4.
Constraints:

2 <= cost.length <= 100
0 <= cost[i] <= 100'''


from typing import List
#recursion
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i >= len(cost):
                return 0 
            return cost[i] + min(dfs(i + 1), dfs(i + 2))
        return min(dfs(0), dfs(1))
#time complexity: O(2^n)
#space complexity: O(n)


#dynamic programming
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0 
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        return min(dfs(0), dfs(1))
#time complexity: O(n)
#space complexity: O(n)

#dynamic programming with space optimization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
#time complexity: O(n)
#space complexity: O(1)