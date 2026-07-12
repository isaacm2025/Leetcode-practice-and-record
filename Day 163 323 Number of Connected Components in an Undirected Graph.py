'''You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

Example 1:



Input:
n = 5, edges = [[0,1],[1,2],[3,4]]

Output: 2
Example 2:



Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.'''

#dfs
from collections import deque
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        count = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                count += 1
        return count
#time complexity: O(V+E) where V is the number of vertices and E is the number of edges. We visit each vertex and edge once in the DFS traversal.
#space complexity: O(V+E) for the adjacency list and O(V) for the visited array, resulting in a total space complexity of O(V+E).

#bfs
from collections import deque
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):
            queue = deque([node])
            visited[node] = True
            while queue:
                curr = queue.popleft()
                for nei in adj[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
        count = 0
        for node in range(n):
            if not visited[node]:
                bfs(node)
                count += 1
        return count
#time complexity: O(V+E) where V is the number of vertices and E is the number of edges. We visit each vertex and edge once in the BFS traversal.
#space complexity: O(V+E) for the adjacency list and O(V) for the visited array and the queue, resulting in a total space complexity of O(V+E).
