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

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(root):
            nonlocal res
            if not root:
                return
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res = max(res, left + right + root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    def getMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        return max(left, right, 0) + root.val

#DFS optimal
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], leftMax + rightMax + root.val)
            return max(leftMax, rightMax, 0) + root.val
        dfs(root)
        return res[0]
#tiime complexity: O(n)
#space complexity: O(n) in worst case, O(log n) in best case
