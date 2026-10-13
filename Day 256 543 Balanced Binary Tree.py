'''Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: true
Example 2:



Input: root = [1,2,3,null,null,4,null,5]

Output: false

Example 3:

Input: root = []

Output: true
Constraints:

The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

#dfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: # if the current node is None, it is balanced and has height 0
                return [True, 0] # return a list with two elements: [is_balanced, height]
            left, right = dfs(root.left), dfs(root.right) # recursively check the left and right subtrees
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # the current node is balanced if both subtrees are balanced and their heights differ by at most 1
            return [balanced, 1 + max(left[1], right[1])] # return a list with two elements: [is_balanced, height], where height is 1 plus the maximum height of the left and right subtrees
        return dfs(root)[0] # return the first element of the list returned by dfs, which indicates whether the tree is balanced or not
#time complexity: O(n)
#space complexity: O(n)