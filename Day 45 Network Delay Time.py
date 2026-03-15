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



from collections import defaultdict
from typing import List
#DFS
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = {node: float("inf") for node in range(1, n + 1)}
        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time
            for neighbor, weight in adj[node]:
                dfs(neighbor, time + weight)
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float("inf") else - 1
#time complexity: O(n + e) where n is the number of nodes and e is the number of edges
#space complexity: O(n + e) for the adjacency list and the distance dictionary


#floyd warshall
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float("inf")
        dist = [[inf] * n for _ in range(n)]
        for u, v, w, in times:
            dist[u - 1][v - 1] = w
        for i in range(n):
            dist[i][i] = 0
        for mid in range(n):
            for src in range(n):
                for dst in range(n):
                    dist[src][dst] = min(dist[src][dst], dist[src][mid] + dist[mid][dst])
        res = max(dist[k - 1])
        return res if res < inf else - 1
#time complexity: O(n^3) due to the three nested loops for the Floyd-Warshall algorithm
#space complexity: O(n^2) for the distance matrix

        
