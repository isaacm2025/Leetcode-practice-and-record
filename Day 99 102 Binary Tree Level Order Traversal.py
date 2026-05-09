'''Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000'''

# Definition for a binary tree node.
#dfs
from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res
#time complexity: O(n) where n is the number of nodes in the tree. We visit each node exactly once to add its value to the corresponding level in the result list.
#space complexity: O(n) in the worst case when the tree is completely unbalanced (e.g., a linked list), and O(log n) in the best case when the tree is balanced. This is because the maximum depth of the recursion will be equal to the height of the tree, which can be O(n) in the worst case and O(log n) in the best case. 
#Additionally, the result list will also take O(n) space to store the values of all nodes in the tree
