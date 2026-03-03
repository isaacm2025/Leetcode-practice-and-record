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
-100 <= Node.val <= 100'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
from ast import List
from ast import List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
#time complexity: O(n)
#space complexity: O(n)
