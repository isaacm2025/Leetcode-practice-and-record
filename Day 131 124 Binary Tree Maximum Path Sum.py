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

#dfs optimal
from typing import Optional
#definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] #initialize res to the value of the root node
        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(root.left) #get the maximum path sum of the left subtree
            rightMax = dfs(root.right) #get the maximum path sum of the right subtree
            leftMax = max(leftMax, 0) #if the maximum path sum of the left subtree is negative, set it to 0
            rightMax = max(rightMax, 0) #if the maximum path sum of the
            res[0] = max(res[0], root.val + leftMax + rightMax) #update res to the maximum path sum found so far
            return root.val + max(leftMax, rightMax) #return the maximum path sum of the current node plus the maximum path sum of either the left or right subtree
        dfs(root) #start dfs traversal from root
        return res[0] #return the maximum path sum found in res
#time complexity: O(n)
#space complexity: O(n) in worst case, O(log n) in best case