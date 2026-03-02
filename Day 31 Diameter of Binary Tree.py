'''The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:



Input: root = [1,null,2,3,4,5]

Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2
Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#brute force
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
    def maxHeight(self, root):
        if not root:
            return 0 
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
#time complexity: O(n^2) where n is the number of nodes in the binary tree, 
# because for each node, we are calculating the height of its left and right subtrees, which takes O(n) time in the worst case. 
# Since we are doing this for each node, the overall time complexity is O(n^2).
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the recursion stack can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes in any single path from root to leaf being log n.

#depth first search (DFS) with memoization
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            res = max(res, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return res
#time complexity: O(n) where n is the number of nodes in the binary tree, because we need to visit each node once to calculate the diameter of the tree.
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the recursion stack can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes in any single path from root to leaf being log n.