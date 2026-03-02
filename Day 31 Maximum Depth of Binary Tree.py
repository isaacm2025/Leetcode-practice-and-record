'''Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: 3
Example 2:

Input: root = []

Output: 0
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#time complexity: O(n) where n is the number of nodes in the binary tree, because we need to visit each node once to calculate the depth of the tree.
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the recursion stack can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes in any single path from root to leaf being log n.
