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
#time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once to calculate the depth.
#space complexity: O(h), where h is the height of the binary tree. The maximum space used by the recursion stack is equal to the height of the tree. 
# In the worst case, the height of the tree can be equal to the number of nodes (n) in a skewed tree, resulting in O(n) space complexity. 
# In a balanced tree, the height would be log(n), resulting in O(log(n)) space complexity.