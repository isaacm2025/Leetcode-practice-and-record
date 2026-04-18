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

#optimal
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0 , 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if  visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            res += dist[nextNode]
            node = nextNode
            edges += 1
        return res
#time complexity: O(n^2) where n is the number of points
#space complexity: O(n) where n is the number of points