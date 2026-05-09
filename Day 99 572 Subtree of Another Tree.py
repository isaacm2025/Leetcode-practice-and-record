'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:



Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true

Example 2:



Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
Constraints:

1 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
'''

# Definition for a binary tree node.
from typing import Optional
#dfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False
#time complexity: O(m*n) where m is the number of nodes in the root tree and n is the number of nodes in the subRoot tree. In the worst case, we may have to compare every node in the root tree with every node in the subRoot tree to check for a match.
#space complexity: O(m+n) in the worst case when both trees are skewed, and O(log m + log n) in the best case when both trees are balanced. This is because the maximum depth of the recursion will be equal to the height of the tree, which can be O(m) in the worst case and O(log m) in the best case for the root tree, and O(n) in the worst case and O(log n) in the best case for the subRoot tree.