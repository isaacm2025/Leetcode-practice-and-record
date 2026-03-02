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
-1000 <= Node.val <= 1000'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#brute force
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if abs(leftHeight - rightHeight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
#time complexity: O(n^2) where n is the number of nodes in the binary tree, 
# because for each node, we are calculating the height of its left and right subtrees, which takes O(n) time in the worst case. 
# Since we are doing this for each node, the overall time complexity is O(n^2).
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the recursion stack can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes in any single path from root to leaf being log n.

#depth first search (DFS) with memoization
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
#time complexity: O(n) where n is the number of nodes in the binary tree, 
# because we need to visit each node once to check if the tree is balanced and to calculate the height of the tree.
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the recursion stack can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes in any single path from root to leaf being log  

