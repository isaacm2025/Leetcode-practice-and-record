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

1 <= tasks.length <= 10000
0 <= n <= 100
'''

#greedy
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        maxCount = count[25]
        idleTime = (maxCount - 1) * n
        for i in range(24, -1, -1):
            idleTime -= min(maxCount - 1, count[i])
        return max(0, idleTime) + len(tasks)
#time com: O(n) where n is the length of the array
#space com: O(1) since the size of the count array is constant (26)

#math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        maxCount = max(count)
        maxCountTasks = 0
        for i in count:
            maxCountTasks += 1 if i == maxCount else 0
        time = (maxCount - 1) * (n + 1) + maxCountTasks
        return max(time, len(tasks))
#time com: O(n) where n is the length of the array
#space com: O(1) since the size of the count array is constant (26)
        