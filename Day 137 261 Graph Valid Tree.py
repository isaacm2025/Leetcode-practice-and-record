'''Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2'''

#dfs
from collections import deque
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n
#time complexity: O(V + E) where V is the number of nodes and E is the number of edges
#space complexity: O(V + E) where V is the number of nodes and E is the number of edges

#bfs
from collections import deque
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit =set()
        q = deque([(0, -1)])
        visit.add(0)
        while q:
            node, par = q.popleft()
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
        return len(visit) == n
#time complexity: O(V + E) where V is the number of nodes and E is the number of edges
#space complexity: O(V + E) where V is the number of nodes and E is the number of edges