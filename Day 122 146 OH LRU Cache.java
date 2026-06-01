import java.util.HashMap;
import java.util.Map;

class LRUCache {
    class Node{
        Node prev;
        Node next;
        int key, val;
        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
    Node head, tail;
    Map<Integer, Node> map;
    int capacity;

    public LRUCache(int capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        map = new HashMap<>();
        this.capacity = capacity;
    }

    public int get(int key) {
        if (!map.containsKey(key))
            return -1;
        Node node = map.get(key);
        remove(node);
        add(node);
        return node.val;
    }

    public void put(int key, int value) {
        Node newNode = new Node(key, value);
        if (map.containsKey(key)) {
            Node oldNode = map.get(key);
            remove(oldNode);
        }
        add(newNode);
        map.put(key, newNode);
        if (map.size() > capacity) {
            Node delNode = head.next;
            remove(delNode);
            remove(delNode);
            map.remove(delNode.key);
        }
    }
    public void add(Node node) {
        Node nodeBeforeEnd = tail.prev;
        nodeBeforeEnd.next = node;
        node.prev = nodeBeforeEnd;
        node.next = tail;
        tail.prev = node;
    }
    public void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}