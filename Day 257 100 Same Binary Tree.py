'''Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false

Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100

'''

#dfs
from collections import deque


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
#time complexity: O(min(m, n))
#space complexity: O(min(m, n))

#bfs
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            for _ in range(len(q1)):
                node1 = q1.popleft()
                node2 = q2.popleft()
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
        return True
#time complexity: O(min(m, n))
#space complexity: O(min(m, n))