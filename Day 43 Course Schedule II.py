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

from typing import List
#DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visitSet, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visitSet:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visitSet.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
#time complexity: O(N + P) where N is the number of courses and P is the number of prerequisites
#space complexity: O(N + P) where N is the number of courses and P is the number of prerequisites

#DFS, topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        output = []

        def dfs(crs):
            output.append(crs)
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
        for c in range(numCourses):
            if indegree[c] == 0:
                dfs(c)
        return output if len(output) == numCourses else []
#time complexity: O(N + P) where N is the number of courses and P is the number of prerequisites
#space complexity: O(N + P) where N is the number of courses and P is the number of prerequisites