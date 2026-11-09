'''The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:



Input: root = [1,null,2,3,4,5]

Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2
Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
'''

#dfs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res
#time complexity: O(n)
#space complexity: O(log(n)) in average case, O(n) in worst case

#bfs
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        parent = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in (node.left, node.right):
                if child:
                    parent[child] = node
                    queue.append(child)

        def farthest(start):
            queue = deque([(start, 0)])
            visited = {start}
            farthest_node, distance = start, 0

            while queue:
                node, depth = queue.popleft()
                if depth > distance:
                    farthest_node, distance = node, depth

                neighbors = [node.left, node.right, parent[node]]
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))

            return farthest_node, distance

        endpoint, _ = farthest(root)
        _, diameter = farthest(endpoint)
        return diameter
#time complexity: O(n)
#space complexity: O(n)