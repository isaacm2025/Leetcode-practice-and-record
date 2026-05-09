'''Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
'''

# Definition for a binary tree node.
from typing import Optional
#recursive
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
#time complexity: O(h) where h is the height of the tree. In the worst case, the tree is skewed and the height is equal to the number of nodes in the tree, resulting in O(n) time complexity. In the best case, the tree is balanced and the height is log(n), resulting in O(log n) time complexity.
#space complexity: O(h) in the worst case when the tree is skewed, and O(log n) in the best case when the tree is balanced. This is because the maximum depth of the recursion will be equal to the height of the tree, which can be O(n) in the worst case and O(log n) in the best case.


#iteration
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
#time complexity: O(h) where h is the height of the tree. In the worst case, the tree is skewed and the height is equal to the number of nodes in the tree, resulting in O(n) time complexity. In the best case, the tree is balanced and the height is log(n), resulting in O(log n) time complexity.
#space complexity: O(1) because we are using a constant amount of space to store the current node and the input parameters. We are not using any additional data structures that grow with the size of the input, and we are not using recursion, so the space complexity is constant.