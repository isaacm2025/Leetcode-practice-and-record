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
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
            return True
        return dfs(0, -1) and len(visit) == n
#time complexity: O(V + E)
#space complexity: O(V + E)

#bfs
from collections import deque
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()
        queue = deque([0])
        while queue:
            node = queue.popleft()
            if node in visit:
                return False
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    queue.append(neighbor)
        return len(visit) == n
#time complexity: O(V + E)
#space complexity: O(V + E)