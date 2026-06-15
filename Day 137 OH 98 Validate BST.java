import java.util.Stack;
import java.util.TreeNode;

class Solution {
    public boolean isValidBST(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode prev = null; // Variable to keep track of the previous node in the in-order traversal
        while (root != null || !stack.isEmpty()) { // Continue while there are nodes to process (either the current node is not null or there are nodes in the stack)
            while (root != null) {
                stack.push(root); // Push the current node onto the stack because we need to process it after its left subtree
                root = root.left; // Move to the left child to continue the in-order traversal
            }
            TreeNode mid = stack.pop(); // Pop the top node from the stack, which is the next node in the in-order traversal
            if (prev != null && mid.val <= prev.val) { //if the value of the current node is less than or equal to the value of the previous node, then the binary tree is not a valid BST
                return false; // Return false if the current node's value is not greater than the previous node's value, which violates the BST property
            }
            prev = mid; // Update the previous node to the current node for the next iteration
            root = mid.right; // Move to the right child of the current node to continue the in-order traversal
        }
        return true;
    }
}