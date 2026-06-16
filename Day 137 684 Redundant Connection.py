'''You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.

Example 1:



Input: edges = [[1,2],[1,3],[3,4],[2,4]]

Output: [2,4]
Example 2:



Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]

Output: [3,4]
Constraints:

n == edges.length
3 <= n <= 100
1 <= edges[i][0] < edges[i][1] <= edges.length
There are no repeated edges and no self-loops in the input.'''

#dfs
from collections import deque
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}
        def dfs(node, par, visit):
            if visit[node]:
                return True
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node, visit):
                    return True
            return False
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visit = [False] * (n + 1)
            if dfs(a, -1, visit):
                return [a,b]
        return []
#time complexity: O(E*(V+E)) where E is the number of edges and V is the number of vertices
#space complexity: O(V+E) where V is the number of vertices and E is the number of edges due to the adjacency list and the visited array

#topological sort
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        for a, b in reversed(edges):
            if indegree[a] == 2 and indegree[b]: # both nodes have indegree of 2, meaning they are part of the cycle
                return [a,b]
        return []
#time complexity: O(V+E) where V is the number of vertices and E is the number of edges
#space complexity: O(V+E) where V is the number of vertices and E is the number of edges due to the adjacency list and the indegree array