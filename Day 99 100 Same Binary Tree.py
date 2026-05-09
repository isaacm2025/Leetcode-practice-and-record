'''Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false

Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
from collections import deque
from typing import Optional
#dfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
#time complexity: O(n) where n is the number of nodes in the tree. We are visiting each node in the tree once to compare the values and structure of the two trees.
#space complexity: O(n) in the worst case when the tree is skewed, and O(log n) in the best case when the tree is balanced. This is because the maximum depth of the recursion will be equal to the height of the tree, which can be O(n) in the worst case and O(log n) in the best case.

#iteration
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        return True
#time complexity: O(n) where n is the number of nodes in the tree. We are visiting each node in the tree once to compare the values and structure of the two trees.
#space complexity: O(n) in the worst case when the tree is skewed, and O(log n) in the best case when the tree is balanced. This is because the maximum depth of the stack will be equal to the height of the tree, which can be O(n) in the worst case and O(log n) in the best case.

#bfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            for _ in range(len(q1)):
                nodeP, nodeQ = q1.popleft(), q2.popleft()
                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)
        return True
#time complexity: O(n) where n is the number of nodes in the tree. We are visiting each node in the tree once to compare the values and structure of the two trees.
#space complexity: O(n) in the worst case when the tree is skewed, and O(log n) in the best case when the tree is balanced. This is because the maximum number of nodes in the queue at any time will be equal to the maximum width of the tree, which can be O(n) in the worst case and O(log n) in the best case.