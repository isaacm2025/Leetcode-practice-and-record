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

0 <= intervals.length <= 100,000
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''

#minHeap
from typing import List
import heapq
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.start = end
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        minHeap = []
        for i in intervals:
            if minHeap and minHeap[0] <= i.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, i.end)
        return len(minHeap)
#time complexity: O(n log n), where n is the number of intervals. The sorting step takes O(n log n) time, and the heap operations (push and pop) take O(log n) time for each of the n intervals, resulting in a total of O(n log n) time complexity.
#space complexity: O(n), where n is the number of intervals. In the worst case, all intervals could overlap, and we would need to store all of them in the minHeap, resulting in a space complexity of O(n).