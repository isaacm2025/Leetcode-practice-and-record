import java.util.Stack;
import java.util.TreeNode;
import java.util.Node;

class Solution {
    public Node treeToDoublyList(Node root) {
        if (root == null) { // If the input tree is empty, return null as there are no nodes to convert into a doubly linked list
            return root;
        }
        Stack<Node> stack = new Stack<>(); // Stack to keep track of nodes during the in-order traversal, use stack to simulate the recursive call stack
        Node head = null; // Variable to keep track of the head of the doubly linked list, it will be set to the leftmost node in the tree (the smallest value) during the traversal
        Node prevNode = null;
        while (root != null || !stack.isEmpty()) { // Continue while there are nodes to process (either the current node is not null or there are nodes in the stack)
            while (root != null) { // Traverse to the leftmost node of the current subtree, pushing nodes onto the stack as we go down the left side of the tree
                stack.push(root);
                root = root.left;

            }
            root = stack.pop(); // Pop the top node from the stack, which is the next node in the in-order traversal (the leftmost node of the current subtree)
            if (head == null) {
                head = root;
            }
            if (prevNode != null) { // If there is a previous node, link the current node with the previous node to form the doubly linked list. Set the left pointer of the current node to the previous node and the right pointer of the previous node to the current node
                root.left = prevNode;
                prevNode.right = root;
            }
            prevNode = root; // Update the previous node to the current node for the next iteration, so that we can link the next node in the in-order traversal to the current node
            root = root.right;
        }
        head.left = prevNode; // After the in-order traversal is complete, link the head of the doubly linked list to the last node (prevNode) to make the list circular. Set the left pointer of the head to the last node and the right pointer of the last node to the head
        prevNode.right = head; // Link the last node (prevNode) to the head of the doubly linked list to complete the circular structure. Set the right pointer of the last node to the head
        return head;
    }
}