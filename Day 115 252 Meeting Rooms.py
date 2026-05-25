'''Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000'''

#bf
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            A = intervals[i]
            for j in range(i + 1, n):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True
#time complexity: O(n^2), where n is the number of intervals in the input list, due to the nested loops.
#space complexity: O(1)


#sorting
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
            return True
#time complexity: O(nlogn), where n is the number of intervals in the input list, due to the sorting step. The checking step takes O(n) time, log(n) because we only need to check adjacent intervals after sorting.
#space complexity: O(1)