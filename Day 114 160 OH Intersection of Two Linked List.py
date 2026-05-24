'''Cannot modify the linked list.'''

public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> nodeSet = new HashSet<>();
        ListNode ptr = headA;

        //Add each node from listA to the set
        while (ptr != null) {
            nodeSet.add(ptr);
            ptr = ptr.next;
        }
        ptr = headB;
        while (ptr != null) {
            if (nodeSet.contains(ptr)) {
                return ptr;
            }
            nodeSet.add(ptr);
            ptr = ptr.next;
        }
        return null; // No intersection

    }
}