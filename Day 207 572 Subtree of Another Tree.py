'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Example 1:



Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true

Example 2:



Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
'''

#dfs
from typing import Optional
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
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False
#time complexity: O(n*m)
#space complexity: O(m + n)