'''You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3,null,4,null,5]

Output: [1,3,5]
Example 2:



Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]
Example 3:

Input: root = [1,null,2]

Output: [1,2]
Example 4:

Input: root = []

Output: []

Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
'''

#dfs
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, level):
            if not node:
                return None
            if len(res) == level:
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return res
#time complexity: O(n)
#space complexity: O(n) in worst case, O(log n) in best case