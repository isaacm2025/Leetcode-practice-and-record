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
-100 <= Node.val <= 100


'''

#recursion
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#time complexity: O(N) where N is the number of nodes in the binary tree.
#space complexity: O(H) where H is the height of the binary tree. In the worst case, the height of the binary tree can be N (when the tree is skewed), resulting in a space complexity of O(N).

#bfs
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
#time complexity: O(N) where N is the number of nodes in the binary tree.
#space complexity: O(W) where W is the maximum width of the binary tree. In the worst case, the maximum width of the binary tree can be N/2 (when the tree is a complete binary tree), resulting in a space complexity of O(N).