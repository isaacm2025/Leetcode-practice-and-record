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

#recursive dfs
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left =left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        #base case: if root is None, return 0
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) #return 1 + max(left, right) where left and right are the depth of left and right subtree respectively.
    
#time complexity: O(n) where n is the number of nodes in the tree. We visit each node once.
#space complexity: O(h) where h is the height of the tree. 
#In the best case, the tree is balanced and the height is log(n), so the space complexity is O(log(n)).
#in the worst case, the space complexity is O(n) due to the recursive call stack.

#bfs
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        q = deque() #initialize a queue to store the nodes at each level of the tree.
        if root: #if root is not None, add it to the queue.
            q.append(root)
        level = 0 #initialize a variable to keep track of the current level of the tree.
        while q: #while the queue is not empty, we will process the nodes at the current level and add their children to the queue for the next level.
            for i in range(len(q)): #we will process all the nodes at the current level, which is given by the length of the queue.
                node = q.popleft() #pop the first node from the queue and add its children to the queue for the next level.
                if node.left: #if the left child of the node is not None, add it to the queue.
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1 #after processing all the nodes at the current level, we will increment the level variable by 1 to move to the next level of the tree.
        return level
#time complexity: O(n) where n is the number of nodes in the tree. We visit each node once.
#space complexity: O(n) in the worst case, when the tree is completely unbalanced and all nodes are on the same level, the queue will contain all the nodes at that level,
#which is O(n). In the best case, when the tree is completely balanced, the queue will contain at most 2^(h-1) nodes at the last level, where h is the height of the tree, which is O(2^(h-1)) = O(n/2) = O(n). Therefore, the space complexity is O(n) in both cases.