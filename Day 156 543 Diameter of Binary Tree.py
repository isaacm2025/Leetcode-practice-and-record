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

#dfs
from typing import Optional

class Solution:
    def diameterOfBT(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res
#time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once to calculate the diameter.
#space complexity: O(h), where h is the height of the binary tree. The maximum space used by the recursion stack is equal to the height of the tree.
#best case: O(log(n)) for a balanced tree, worst case: O(n) for a skewed tree.
#worst case: O(n) for a skewed tree.