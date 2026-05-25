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
0 <= intervals[i].start < intervals[i].end <= 1,000,000'''

#minheap
from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
        return len(minHeap)
#time complexity: O(nlogn), where n is the number of intervals in the input list, due to the sorting step. The heap operations take O(logn) time, and we perform at most n heap operations, resulting in O(nlogn) time for the heap operations.
#space complexity: O(n), where n is the number of intervals in the input list, due to the space used for the minHeap, O(1) if we don't consider the space used for the minHeap.

#greedy
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        time.sort(key = lambda pair: (pair[0], pair[1]))
        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res
#time complexity: O(nlogn), where n is the number of intervals in the input list, due to the sorting step. The counting step takes O(n) time.
#space complexity: O(n), where n is the number of intervals in the input list, due to the space used for the time list, O(1) if we don't consider the space used for the time list.