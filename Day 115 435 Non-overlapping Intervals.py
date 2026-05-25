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
-50000 <= starti < endi <= 50000
'''

#recursive
from typing import List
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
#time complexity: O(2^n), where n is the number of intervals in the input list, due to the recursive calls. The sorting step takes O(nlogn) time.
#space complexity: O(n), where n is the number of intervals in the input list, due to the space used for the recursive call stack, O(1) if we don't consider the space used for the recursive call stack.

#dp
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        n = len(intervals)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
        maxNonOverlap = max(dp)
        return n - maxNonOverlap
#time complexity: O(n^2), where n is the number of intervals in the input list, due to the nested loops. The sorting step takes O(nlogn) time.
#space complexity: O(n), where n is the number of intervals in the input list, due to the space used for the dp array, O(1) if we don't consider the space used for the dp array.