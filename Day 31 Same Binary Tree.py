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
-100 <= Node.val <= 100'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
#time complexity: O(n) where n is the number of nodes in the tree
#space complexity: O(n) in the worst case when the tree is completely unbalanced, and O(log n) in the best case when the tree is completely balanced.


