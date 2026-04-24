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
0 <= start <= end <= 1000
'''

#sorting
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
#time complexity: O(nlogn) due to sorting
#space complexity: O(n) in the worst case when there are no overlapping intervals, otherwise O(1) if we don't consider the output array.

#greedy
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        maxVal = max(interval[0] for interval in intervals)
        mp = [0] * (maxVal + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])
        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] !=0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1
        if interval_start != -1:
            res.append([interval_start, have])
        return res
#time complexity: O(n + m), where n is the number of intervals and m is the maximum value of the start of the intervals.
#space complexity: O(m), where m is the maximum value of the start of the intervals.
