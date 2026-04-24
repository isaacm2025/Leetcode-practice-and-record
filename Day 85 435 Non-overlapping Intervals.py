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

#recursion
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
#time complexity: O(2^n) in the worst case, where n is the number of intervals. This is because in the worst case, we may have to explore all possible combinations of intervals to find the maximum number of non-overlapping intervals.
#space complexity: O(n) in the worst case due to the recursion stack, where n is the number of intervals.

#bs
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        dp = [0] * n
        dp[0] = 1

        def bs(r, target):
            l = 0
            while l < r:
                mid = (l + r) >> 1
                if intervals[mid][1] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l
        for i in range(1, n):
            idx = bs(i, intervals[i][0])
            if idx == 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(dp[i - 1], dp[idx - 1] + 1)
        return n - dp[-1]
#time complexity: O(nlogn) due to sorting and binary search, where n is the number of intervals.
#space complexity: O(n) due to the dp array, where n is the number of intervals.

#greedy
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                res += 1
                prev = min(end, prev)
        return res
#time complexity: O(nlogn) due to sorting, where n is the number of intervals.
#space complexity: O(1) if we don't consider the space used for sorting, otherwise O(n) due to the space used for sorting, where n is the number of intervals.