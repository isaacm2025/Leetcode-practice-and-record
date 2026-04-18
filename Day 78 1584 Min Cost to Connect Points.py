'''You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:



Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10
Constraints:

1 <= points.length <= 1000
-1,000,000 <= xi, yi <= 1,000,000
All pairs (xi, yi) are distinct.
'''

from collections import defaultdict
import heapq
from typing import List

#prim's algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0
        visited = set()
        minH = [[0, 0]]
        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return res
#time complexity: O(n^2 log n) where n is the number of points
#space complexity: O(n^2) where n is the number of points