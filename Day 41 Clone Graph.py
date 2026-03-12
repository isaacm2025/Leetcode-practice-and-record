'''Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:



Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:



Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:

Input: adjList = []

Output: []
Explanation: The graph is empty.

Constraints:

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque
from typing import Optional
from xml.dom.minidom import Node

#DFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
#time complexity: O(N + M) where N is the number of nodes and M is the number of edges in the graph.
#space complexity: O(N) where N is the number of nodes in the graph. This is because we are storing a mapping of each original node to its corresponding cloned node in the oldToNew dictionary, which can potentially store an entry for each node in the graph. 
# Additionally, the recursive call stack can also grow up to O(N) in the worst case if the graph is a linear chain of nodes.

#BFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        oldToNew = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])
        return oldToNew[node]


