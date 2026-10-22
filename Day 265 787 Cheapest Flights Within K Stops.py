'''
There are n airports, labeled from 0 to n - 1, which are connected by some flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. You may assume there are no duplicate flights and no flights from an airport to itself.

You are also given three integers src, dst, and k where:

src is the starting airport
dst is the destination airport
src != dst
k is the maximum number of stops you can make (not including src and dst)
Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.


Example 1:



Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

Output: 500
Explanation:
The optimal path with at most 1 stop from airport 0 to 3 is shown in red, with total cost 200 + 300 = 500.
Note that the path [0 -> 1 -> 2 -> 3] costs only 400, and thus is cheaper, but it requires 2 stops, which is more than k.'''

#dijkstra
from typing import List
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float('inf')
        adj = [[] for _ in range(n)]
        dist = [[inf] * (k + 5) for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        dist[src][0] = 0
        minHeap = [(0, src, -1)]
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node:
                return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = stops + 1
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))
        return -1
#time complexity: O(E * log(V)) where E is the number of flights and V is the number of airports. In the worst case, we may visit all edges in the graph, and for each edge, we perform a heap operation that takes O(log(V)) time.
#space complexity: O(V + E) where V is the number of airports and E is the number of flights. We use an adjacency list to store the graph, which requires O(V + E) space. Additionally, we use a distance array of size V * (k + 5) to keep track of the minimum costs, which also requires O(V * (k + 5)) space.
