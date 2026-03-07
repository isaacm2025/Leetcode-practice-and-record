'''You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

1 <= tasks.length <= 1000
0 <= n <= 100
'''

#max heap
from collections import deque
from typing import Counter, List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    heapq.heappush(q, (cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q[0][0])
                heapq.heappop(q)
        return time
#time complexity: O(nlogk) where k is the number of unique tasks
#space complexity: O(k)

#greedy
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        max_count = count[25]
        idle_time = (max_count - 1) * n
        for i in range(24, -1, -1):
            idle_time -= min(count[i], max_count - 1)
        return len(tasks) + max(0, idle_time)
#time complexity: O(n)
#space complexity: O(1)