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
-1000 <= Node.val <= 1000
'''

#DFS
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left =left
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
#time complexity: O(n) where n is the number of nodes in the tree.
#space complexity: O(n) in worst case when the tree is skewed, O(logn) in best case when the tree is balanced.

#BFS
from collections import deque
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
#time complexity: O(n) where n is the number of nodes in the tree.
#space complexity: O(n) in worst case when the tree is skewed, O(logn) in best case when the tree is balanced.

