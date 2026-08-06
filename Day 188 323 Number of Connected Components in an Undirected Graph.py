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
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for i in range(n):
            if not visit[i]:
                res += 1
                visit[i] = True
                dfs(i)
        return res  
#time complexity: O(n + e), where n is the number of nodes and e is the number of edges. We visit each node and edge once.
#space complexity: O(n + e), where n is the number of nodes and e is the number of edges. We store the adjacency list and the visited array.

#bfs
from typing import List
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):
            queue = deque([node])
            visit[node] = True
            while queue:
                cur = queue.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        queue.append(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                res += 1
                bfs(node)
        return res
#time complexity: O(n + e), where n is the number of nodes and e is the number of edges. We visit each node and edge once.
#space complexity: O(n + e), where n is the number of nodes and e is the number of edges. We store the adjacency list and the visited array, and the queue can hold at most n nodes in the worst case
