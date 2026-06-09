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

#dfs
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #if subRoot is None, we will return True indicating that the trees are equivalent. This is because an empty tree is a subtree of any tree, including itself.
            return True
        if not root: #if root is None and subRoot is not None, we will return False indicating that the trees are not equivalent. This is because a non-empty tree cannot be a subtree of an empty tree.
            return False
        if self.sameTree(root, subRoot): #if the current node in root is the same as the current node in subRoot, we will return True indicating that the trees are equivalent. This is because if the current node in root is the same as the current node in subRoot, then the left and right subtree of the current node in root must also be the same as the left and right subtree of the current node in subRoot for the trees to be equivalent.
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)) #if the left and right subtree of the current node in root is the same as the left and right subtree of the current node in subRoot, we will return True indicating that the trees are equivalent. Otherwise, we will return False.
        return False
#time complexity: O(m*n) where m and n are the number of nodes in the two trees. In the worst case, we will compare each node of the first tree with each node of the second tree.
#space complexity: O(m+n)
