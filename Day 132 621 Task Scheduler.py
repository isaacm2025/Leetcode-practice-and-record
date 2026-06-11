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

#sorting
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1 #count the frequency of each task in the array, and store it in a list of size 26, where the index of the list corresponds to the ASCII value of the task character minus the ASCII value of 'A'
        task_counts.sort() #sort the list of task counts in non-decreasing order, so that the task with the maximum count is at the end of the list
        max_count = task_counts[-1] #the maximum count of any task is the last element in the sorted list of task counts
        max_count_tasks = task_counts.count(max_count) #count the number of tasks that have the maximum count, which is the number of tasks that will be executed in the last cycle
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks) 
    #the minimum number of CPU cycles required to complete all tasks is the maximum of the total number of tasks and the number of cycles required to execute the tasks with the maximum count, which is (max_count - 1) * (n + 1) + max_count_tasks, 
    #where (max_count - 1) is the number of cycles required to execute the tasks with the maximum count, (n + 1) is the number of cycles required to execute the tasks with the maximum count and the idle cycles, and max_count_tasks is the number of tasks that will be executed in the last cycle

#time complexity: O(n) for counting the frequency of each task in the array, where n is the number of tasks in the array, and O(1) for sorting the list of task counts, since the size of the list is fixed at 26
#space complexity: O(1) for storing the list of task counts, since the size of the list is fixed at 26