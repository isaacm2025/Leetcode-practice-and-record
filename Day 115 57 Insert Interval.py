'''You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

Output: [[1,6]]
Explanation: [2,5] overlaps with [1,3] and [4,6], so all three are merged into [1,6].

Example 2:

Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

Output: [[1,2],[3,5],[6,7],[9,10]]
Explanation: [6,7] does not overlap with any existing interval, so it is simply inserted between [3,5] and [9,10].

Constraints:

0 <= intervals.length <= 1000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 1000'''

#ls
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
#time complexity: O(n)
#space complexity: O(n), where n is the number of intervals in the input list, O(1) if we don't consider the space used for the output list.

#bs
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)
        target = newInterval[0]
        left, right= 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        intervals.insert(left, newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
#time complexity: O(n), where n is the number of intervals in the input list
#space complexity: O(n), where n is the number of intervals in the input list, O(1) if we don't consider the space used for the output list.
