'''Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]

Output: [[1,5],[6,7]]
Example 2:

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000'''



from typing import List
#sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
#time complexity: O(nlogn) for sorting, O(n) for merging, overall O(nlogn)
#space complexity: O(n) for the output list, O(1) for the input list.

#sweep line algorithm
import heapq
from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        res = []
        interval = []
        have = 0
        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res
#time complexity: O(nlogn) for sorting the keys of the map, O(n) for iterating through the intervals, overall O(nlogn)
#space complexity: O(n) for the map, O(n) for the output list, O(1) for the interval list.

#greedy
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)
        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])
        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(have, mp[i] - 1)
            if have == i:
                res.append([interval_start, have])
                interval_start = -1
                have = -1
        if interval_start != -1:
            res.append([interval_start, have])
        return res
#time complexity: O(n) for iterating through the intervals, O(m) for iterating through the map, overall O(n + m) where m is the maximum value of the start intervals.
#space complexity: O(n) for the output list, O(m) for the map, O(1) for the interval list.