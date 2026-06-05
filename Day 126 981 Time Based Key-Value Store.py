'''Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"
Constraints:

1 <= key.length, value.length <= 100
key and value only include lowercase English letters and digits.
0 <= timestamp <= 10^7
All the timestamps of set are strictly increasing.'''

#bs
from collections import defaultdict
from sortedcontainers import SortedDict
class TimeMap:
    def __init__(self):
        self.m = defaultdict(SortedDict)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1
        if idx >= 0:
            closestTimestamp = timestamps.iloc[idx]
            return timestamps[closestTimestamp]
        return ""
#time O(log n) because we are using binary search to find the closest timestamp
#space O(n *m) where n is the number of keys and m is the number of timestamps for each key


#iteration
from collections import defaultdict

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
#time O(n) because we are visiting each node once
#space O(1) because we are not using any extra space