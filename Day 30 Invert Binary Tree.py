'''You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]
Example 2:



Input: root = [3,2,1]

Output: [3,1,2]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#breadth first search
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
#time complexity: O(n) where n is the number of nodes in the binary tree, because we need to visit each node once to invert the tree.
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the queue can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes at any level being n/2.


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
#time complexity: O(n) where n is the number of nodes in the binary tree, because we need to visit each node once to invert the tree.
#space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), 
# the recursion stack can hold all the nodes at once. In the best case, when the binary tree is perfectly balanced, 
# the space complexity would be O(log n) due to the maximum number of nodes in any single path from root to leaf being log n.

