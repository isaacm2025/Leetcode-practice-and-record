'''You are given a list of flight tickets tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.

Each from_i and to_i consists of three uppercase English letters.

Reconstruct the itinerary in order and return it.

All of the tickets belong to someone who originally departed from "JFK". Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.

For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].
You may assume all the tickets form at least one valid flight path.

Example 1:



Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]

Output: ["JFK","BUF","HOU","SEA"]
Example 2:



Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

Output: ["JFK","HOU","JFK","SEA","JFK"]
Explanation: Another possible reconstruction is ["JFK","SEA","JFK","HOU","JFK"] but it is lexicographically larger.

Constraints:

1 <= tickets.length <= 300
from_i != to_i'''

from collections import defaultdict
from typing import List
#DFS
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                adj[src].insert(i, v)
            return False
        dfs("JFK")
        return res
#time complexity: O(E * V) where E is the number of edges and V is the number of vertices
#space complexity: O(E + V) for the adjacency list and the recursion stack

#Hierholzer's algorithm
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        res = []
        def dfs(node):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
        dfs("JFK")
        return res[::-1]
#time complexity: O(E log E) due to sorting the adjacency list and traversing all edges
#space complexity: O(E) for the adjacency list and O(V) for the recursion stack, where E is the number of edges and V is the number of vertices
