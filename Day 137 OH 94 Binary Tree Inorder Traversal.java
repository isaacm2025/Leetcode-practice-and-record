
import java.util.List;
import java.util.ArrayList;
import java.util.Stack;
import java.util.TreeNode;

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>(); // List to store the result
        if (root == null) {
            return result; // Return empty list if the tree is empty
        }
        Stack<TreeNode> stack = new Stack<>(); // Stack to keep track of nodes, use stack to simulate the recursive call stack

        while(root != null || !stack.isEmpty()) { //continue when root is not null or stack is not empty
            while(root != null) {
                stack.push(root); // Push the current node onto the stack
                root = root.left; // Move to the left child
            }
            TreeNode current = stack.pop(); // Pop the top node from the stack and set it as the current node
            result.add(current.val); // Add the value of the current node to the result list
            root = current.right; // Move to the right child of the current node
        }
        return result;
    }
}
//time complexity: O(n) where n is the number of nodes in the binary tree, as we visit each node exactly once.
//space complexity: O(h) where h is the height of the binary tree, as in the worst case (a skewed tree), the stack can hold all the nodes in the path from the root to the leaf. 
//In a balanced tree, the space complexity would be O(log n) because the height of the tree would be log n.