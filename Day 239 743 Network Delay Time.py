'''You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

Example 1:



Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

Output: 3
Example 2:

Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

Output: -1
Constraints:

1 <= k <= n <= 100
1 <= times.length <= 1000'''

#dfs
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        dist = {node: float('inf') for node in range(1, n + 1)}
        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else - 1
#time complexity: O(E + V) where E is the number of edges and V is the number of vertices. In the worst case, we may have to traverse all edges and vertices in the graph, leading to a time complexity of O(E + V).
#space complexity: O(V + E) where V is the number of vertices and E is the number of edges. We use an adjacency list to store the graph, which requires O(V + E) space. Additionally, we use a distance dictionary of size V to keep track of the minimum time to reach each node, which also requires O(V) space. Therefore, the overall space complexity is O(V + E).

#bellman ford
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n)
        dist[k - 1] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
        maxDist = max(dist)
        return maxDist if maxDist < float('inf') else - 1   
#time complexity: O(V * E) where V is the number of vertices and E is the number of edges. In the worst case, we may have to relax all edges for each vertex, leading to a time complexity of O(V * E).
#space complexity: O(V) where V is the number of vertices. We use a distance array of size V to keep track of the minimum time to reach each node, which requires O(V) space. Therefore, the overall space complexity is O(V).

#dijkstra
from collections import defaultdict
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
#time complexity: O(E log V) where E is the number of edges and V is the number of vertices. In the worst case, we may have to process all edges in the graph, and for each edge, we perform a heap operation that takes O(log V) time. Therefore, the overall time complexity is O(E log V).
#space complexity: O(V + E) where V is the number of vertices and E is the number of edges. We use an adjacency list to store the graph, which requires O(V + E) space. Additionally, we use a min-heap to keep track of the nodes to be processed, which can contain at most V nodes in the worst case. Therefore, the overall space complexity is O(V + E).