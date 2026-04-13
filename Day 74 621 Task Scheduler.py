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
0 <= n <= 100'''

from typing import List
#greedy
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        maxCount = count[25]
        idle = (maxCount - 1) * n
        for i in range(24, -1, -1):
            idle -= min(maxCount - 1, count[i])
        return max(0, idle) + len(tasks)
#time complexity: O(n) for counting the frequency of each task and O(1) for sorting the count array, O(1) for iterating through the count array.
#space complexity: O(1) for storing the count array, O(1) for storing the idle variable.

#math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0
        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
#time complexity: O(n) for counting the frequency of each task and O(1) for finding the maximum frequency and counting the number of tasks with the maximum frequency.
#space complexity: O(1) for storing the count array, O(1) for storing the maxf and maxCount variables.

