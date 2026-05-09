'''Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: true

Example 2:



Input: root = [1,2,3,null,null,4,null,5]

Output: false
Example 3:

Input: root = []

Output: true
Constraints:

The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
from typing import Optional
#bf
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
#time complexity: O(n^2) where n is the number of nodes in the tree. We are calculating the height of the tree for each node, which takes O(n) time, and we are doing this for each node in the tree, resulting in O(n^2) time complexity.
#space complexity: O(n) in the worst case when the tree is skewed, and O(log n) in the best case when the tree is balanced. This is because the maximum depth of the recursion will be equal to the height of the tree, which can be O(n) in the worst case and O(log n) in the best case.