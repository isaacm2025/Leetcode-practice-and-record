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
-100 <= Node.val <= 100
'''

#dfs
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
#time complexity: O(N) where N is the number of nodes in the binary tree.
#space complexity: O(H) where H is the height of the binary tree. In the worst case, the height of the binary tree can be N (when the tree is skewed), resulting in a space complexity of O(N).