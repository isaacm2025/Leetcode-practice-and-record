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
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) #return the maximum depth of the left and right subtrees, plus 1 for the current node
#time complexity: O(n)
#space complexity: O(n)

#stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]] #initialize a stack with the root node and its depth (1)
        res = 0
        while stack:
            node, depth = stack.pop() #pop a node and its depth from the stack
            if node:
                res = max(res, depth) #update the maximum depth if the current depth is greater
                stack.append([node.left, depth + 1]) #push the left child and its depth (current depth + 1) onto the stack
                stack.append([node.right, depth + 1]) #push the right child and its depth (current depth + 1) onto the stack
        return res
#time complexity: O(n)
#space complexity: O(n)