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


from typing import List
#DFS
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
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        return count
#time complexity: O(n + e) where n is the number of nodes and e is the number of edges
#space complexity: O(n + e) for the adjacency list and visited array

#BFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
        count = 0
        for node in range(n):
            if not visited[node]:
                bfs(node)
                count += 1
        return count
#time complexity: O(n + e) where n is the number of nodes and e is the number of edges
#space complexity: O(n + e) for the adjacency list and visited array, O(n) for the queue in the worst case


