'''Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,4],[1,4]]

Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[2,4]]

Output: 0
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
-50000 <= starti < endi <= 50000'''


from typing import List
#recursion
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        def dfs(i, prev):
            if i == len(intervals):
                return 0
            res = dfs(i + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res
        return len(intervals) - dfs(0, -1)
#time complexity: O(nlogn) for sorting, O(2^n) for the recursion, overall O(nlogn + 2^n)
#space complexity: O(n) for sorting, O(n) for the recursion stack, overall O(n)

#dp top down
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1
            for j in range(i + 1, n):
                if intervals[i][1] <= intervals[j][0]:
                    res = max(res, 1 + dfs(j))
            memo[i] = res
            return res
        return n - max(dfs(i) for i in range(n))
#time complexity: O(nlogn) for sorting, O(n^2) for the recursion, overall O(nlogn + n^2)
#space complexity: O(n) for sorting, O(n) for the memoization, O(n) for the recursion stack, overall O(n)

#dp bottom up
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
        max_non_overlapping = max(dp)
        return n - max_non_overlapping
#time complexity: O(nlogn) for sorting, O(n^2) for the nested loops, overall O(nlogn + n^2)
#space complexity: O(n) for sorting, O(n) for the dp array, overall O(n)