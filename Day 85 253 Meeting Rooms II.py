'''Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
room1: (0,40)
room2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''

#min heap
from typing import List
import heapq
class Interval(object):
    def __init__(self, starrt, end):
        self.start = self.start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        min_heap = []
        for i in intervals:
            if min_heap and min_heap[0] <= i.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i.end)
        return len(min_heap)
#time complexity: O(n log n) where n is the number of intervals. This is because we sort the intervals and then for each interval, we perform a heap operation which takes O(log n) time.
#space complexity: O(n) in the worst case, if all intervals overlap, we will have to store all of them in the min heap. In the best case, if no intervals overlap, we will only have one interval in the min heap at any time, resulting in O(1) space complexity.