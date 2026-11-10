'''Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:



Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:



Input: root = [-15,10,20,null,null,15,5,-5]

Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:

1 <= The number of nodes in the tree <= 30000.
-1000 <= Node.val <= 1000
'''

#dfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, node: TreeNode) -> int:
        res = -float('inf')
        def dfs(node):
            nonlocal res
            if not node:
                return
            left = self.getMax(node.left)
            right = self.getMax(node.right)
            res = max(res, left + right + node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(node)
        return res
    def getMax(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.getMax(node.left)
        right = self.getMax(node.right)
        path = node.val + max(left, right)
        return max(path, 0)