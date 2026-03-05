'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right'''

#brute force
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        arr.sort()
        return arr[k-1]
#time complexity: O(nlogn)
#space complexity: O(n)

#inorder traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k-1]
#time complexity: O(n)
#space complexity: O(n)

#iterative DFS optimal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
#time complexity: O(n)
#space complexity: O(n) in worst case when tree is skewed, O(logn) in average case when tree is balanced
