class Solution {
    List<Integer> numbers = new ArrrayList<>();
    public Solution(ListNode head) {
        ListNode ptr = head;
        while (ptr != null) {
            numbers.add(ptr.val);
            ptr = ptr.next;
        }
    }
    public int getRandom() {
        Random rand = new Random();
        int index = rand.nextInt(numbers.size());
        return numbers.get(index);
    }
}
