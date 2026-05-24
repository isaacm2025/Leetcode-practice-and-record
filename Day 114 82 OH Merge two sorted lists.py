class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(0); // Dummy node to simplify edge cases
        ListNode currentPtr = head; // Pointer to build the merged list


        while (list1 != null && list2 != null) { // While both lists have nodes to compare
            if (list1.val < list2.val) {
                currentPtr.next = list1; // Append the smaller node to the merged list
                list1 = list1.next; // Move to the next node in list1
            }
            else {
                currentPtr.next = list2;
                list2 = list2.next; // Move to the next node in list2
            }
            currentPtr = currentPtr.next; // Move the pointer to the next node in the merged list
        }
        if (list1 != null) {
            currentPtr.next = list1; // Append the remaining nodes of list1 or list2 to the merged list
        } else if (list2 != null) {
            currentPtr.next = list2; // Append the remaining nodes of list1 or list2 to the merged list
        }
        return head.next; // Return the merged list, skipping the dummy node
    }
}