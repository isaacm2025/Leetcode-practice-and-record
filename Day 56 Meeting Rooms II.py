'''Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''


#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq
from typing import List
#min heap solution: sort intervals by start time, then use a min heap to keep track of end times of meetings currently using rooms. 
# For each interval, if the start time is greater than or equal to the minimum end time in the heap, we can reuse that room (pop from heap). 
# Then we add the current interval's end time to the heap. The size of the heap at any point will give us the number of rooms needed.
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        min_heap = []
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return len(min_heap)
#time complexity: O(nlogn) due to sorting and heap operations
#space complexity: O(n) in the worst case when all meetings overlap and we need a room for each meeting

#sweep line algorithm: create a list of all start and end times, sort them, 
# and then iterate through the sorted list to count how many meetings are currently ongoing at any time. 
# The maximum count at any time will give us the number of rooms needed.

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int: