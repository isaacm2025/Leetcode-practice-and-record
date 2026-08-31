'''You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []
Explanation: It's impossible to finish all courses.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.'''

#topological sort
from collections import defaultdict, deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if finish != numCourses:
            return []
        return output[::-1] 
#time complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
#space complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.

#dfs
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            adj[pre].append(nxt)
            indegree[nxt] += 1
        output = []
        def dfs(node):
            output.append(node)
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        return output if len(output) == numCourses else []
#time complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
#space complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.