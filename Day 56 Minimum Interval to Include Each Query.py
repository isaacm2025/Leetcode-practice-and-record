'''You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

Return an array output where output[j] is the result of query[j].

Note: The length of an interval is calculated as right_i - left_i + 1.

Example 1:

Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]

Output: [2,2,3,5,1,-1]
Explanation:

Query = 2: The interval [2,3] is the smallest one containing 2, it's length is 2.
Query = 3: The interval [2,3] is the smallest one containing 3, it's length is 2.
Query = 1: The interval [1,3] is the smallest one containing 1, it's length is 3.
Query = 7: The interval [3,7] is the smallest one containing 7, it's length is 5.
Query = 6: The interval [6,6] is the smallest one containing 6, it's length is 1.
Query = 8: There is no interval containing 8.
Constraints:

1 <= intervals.length <= 1000
1 <= queries.length <= 1000
1 <= left_i <= right_i <= 10000
1 <= queries[j] <= 10000'''

import heapq
from typing import List
#brute force
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        res = []
        for q in queries:
            cur = -1
            for l, r in intervals:
                if l <= q <= r:
                    if cur == -1 or (r - l + 1) < cur:
                        cur = r - l + 1
            res.append(cur)
        return res
#time complexity: O(n*m) where n is the number of intervals and m is the number of queries
#space complexity: O(m) for the result array

#min heap solution: sort intervals by start time, then for each query, we can use a min heap to keep track of the intervals that are currently active (i.e., those that have started but not yet ended). 
# For each query, we can pop from the heap any intervals that have ended before the query time, and then check the top of the heap for the smallest interval that contains the query.
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]
#time complexity: O(nlogn + mlogm) due to sorting and heap operations
#space complexity: O(n) for the heap and result dictionary