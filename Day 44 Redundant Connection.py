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

from typing import List
#DFS
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        def dfs(node, par):
            if visited[node]:
                return True
            visted[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [False] * (n + 1)
            if dfs(u, -1):
                return [u, v]
        return []
#time complexity: O(E *(V + E)) where V is the number of vertices and E is the number of edges
#space complexity: O(V + E) for the adjacency list and visited array

#DFS optimal
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * (n + 1)
        cycle = set()
        cycleStart = -1
        def dfs(node, par):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            visited[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []
#time complexity: O(V + E) where V is the number of vertices and E is the number of edges
#space complexity: O(V + E) for the adjacency list and visited array and cycle set
            